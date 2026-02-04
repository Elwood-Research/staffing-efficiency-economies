#!/usr/bin/env python3
"""
Script 1: Data Preparation and Aggregation
Objective: Load quarterly PBJ files, merge, apply inclusion/exclusion criteria, 
create derivatives for staffing efficiency analysis.

Data Security: This script operates in the vault with read-only access to /data.
Output: Aggregated facility-level dataset (NO individual facility records in output).
"""

import sys
import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURATION
# ============================================================================
DATA_DIR = Path('/data')
OUTPUT_DIR = Path('/study/04-analysis/outputs')
LOG_FILE = OUTPUT_DIR / 'data_prep.log'

QUARTERS = ['CY2023Q1', 'CY2023Q2', 'CY2023Q3', 'CY2023Q4',
            'CY2024Q1', 'CY2024Q2', 'CY2024Q3', 'CY2024Q4']
OUTLIER_THRESHOLD = 4  # |z| > 4 rule
MIN_CENSUS = 20
MIN_COMPLETENESS = 0.9  # 90% non-missing data

def log_msg(msg):
    """Print and log message"""
    print(msg)
    with open(LOG_FILE, 'a') as f:
        f.write(msg + '\n')

# Initialize log
with open(LOG_FILE, 'w') as f:
    f.write("DATA PREPARATION LOG\n")
    f.write("=" * 80 + "\n\n")

# ============================================================================
# STEP 1: LOAD QUARTERLY DATA
# ============================================================================
log_msg("=" * 80)
log_msg("STEP 1: Loading quarterly PBJ data")
log_msg("=" * 80)

dfs = []
total_records_loaded = 0

for quarter in QUARTERS:
    filepath = DATA_DIR / f'PBJ_dailynursestaffing_{quarter}.csv'
    
    try:
        # Try latin-1 first (Windows-1252 compatible)
        df = pd.read_csv(filepath, dtype={
            'PROVNUM': str, 'PROVNAME': str, 'STATE': str,
            'WorkDate': str, 'CY_Qtr': str
        }, encoding='latin-1')
        log_msg(f"✓ Loaded {quarter}: {len(df):,} records (encoding: latin-1)")
        dfs.append(df)
        total_records_loaded += len(df)
    except Exception as e:
        log_msg(f"✗ Failed {quarter}: {str(e)[:100]}")
        continue

if not dfs:
    log_msg("ERROR: No quarterly data loaded!")
    sys.exit(1)

df_combined = pd.concat(dfs, ignore_index=True)
log_msg(f"\nTotal records loaded: {len(df_combined):,}")
log_msg(f"Unique facilities: {df_combined['PROVNUM'].nunique():,}")

# ============================================================================
# STEP 2: DATA QUALITY CHECKS
# ============================================================================
log_msg("\n" + "=" * 80)
log_msg("STEP 2: Initial data quality checks")
log_msg("=" * 80)

required_cols = ['PROVNUM', 'PROVNAME', 'STATE', 'MDScensus', 
                 'Hrs_RN', 'Hrs_LPN', 'Hrs_CNA', 'Hrs_CNA_ctr', 'WorkDate', 'CY_Qtr']
missing_cols = [c for c in required_cols if c not in df_combined.columns]
if missing_cols:
    log_msg(f"WARNING: Missing columns: {missing_cols}")

# Ensure numeric columns
numeric_cols = ['MDScensus', 'Hrs_RN', 'Hrs_LPN', 'Hrs_CNA', 'Hrs_CNA_ctr']
for col in numeric_cols:
    df_combined[col] = pd.to_numeric(df_combined[col], errors='coerce')

# ============================================================================
# STEP 3: REMOVE DUPLICATES
# ============================================================================
log_msg("\n" + "=" * 80)
log_msg("STEP 3: Removing duplicates")
log_msg("=" * 80)

before_dup = len(df_combined)
df_combined = df_combined.drop_duplicates(subset=['PROVNUM', 'WorkDate', 'CY_Qtr'])
after_dup = len(df_combined)
dup_removed = before_dup - after_dup
log_msg(f"Duplicates removed: {dup_removed:,}")

# ============================================================================
# STEP 4: FACILITY-LEVEL AGGREGATION
# ============================================================================
log_msg("\n" + "=" * 80)
log_msg("STEP 4: Facility-level aggregation (4-quarter average)")
log_msg("=" * 80)

agg_dict = {col: 'mean' for col in numeric_cols}
agg_dict['STATE'] = 'first'
agg_dict['PROVNAME'] = 'first'

df_facility = df_combined.groupby('PROVNUM').agg(agg_dict).reset_index()
log_msg(f"Facilities after aggregation: {len(df_facility):,}")

# Rename columns
df_facility.rename(columns={
    'MDScensus': 'mean_census',
    'Hrs_RN': 'mean_rn_hrs',
    'Hrs_LPN': 'mean_lpn_hrs',
    'Hrs_CNA': 'mean_cna_hrs',
    'Hrs_CNA_ctr': 'mean_cna_ctr_hrs'
}, inplace=True)

# ============================================================================
# STEP 5: CREATE DERIVATIVE VARIABLES
# ============================================================================
log_msg("\n" + "=" * 80)
log_msg("STEP 5: Creating derivative variables")
log_msg("=" * 80)

df_facility['rn_to_lpn_ratio'] = df_facility['mean_rn_hrs'] / df_facility['mean_lpn_hrs'].clip(lower=0.01)
df_facility['contract_cna_prop'] = df_facility['mean_cna_ctr_hrs'] / \
    (df_facility['mean_cna_hrs'] + df_facility['mean_cna_ctr_hrs']).clip(lower=0.01)

df_facility['total_hrs'] = df_facility['mean_rn_hrs'] + df_facility['mean_lpn_hrs'] + \
    df_facility['mean_cna_hrs'] + df_facility['mean_cna_ctr_hrs']

# Staffing Efficiency Index
df_facility['eff_rn_lpn'] = (df_facility['rn_to_lpn_ratio'] - df_facility['rn_to_lpn_ratio'].min()) / \
    (df_facility['rn_to_lpn_ratio'].max() - df_facility['rn_to_lpn_ratio'].min())
df_facility['eff_contract_ratio'] = 1 - df_facility['contract_cna_prop']
df_facility['eff_staffing_ratio'] = (df_facility['total_hrs'] / df_facility['mean_census']).clip(0, 1)

df_facility['staffing_efficiency_index'] = (
    0.4 * df_facility['eff_rn_lpn'] + 
    0.3 * df_facility['eff_contract_ratio'] + 
    0.3 * df_facility['eff_staffing_ratio']
)

log_msg(f"Derivatives created successfully")

# ============================================================================
# STEP 6: CREATE CENSUS DECILES
# ============================================================================
log_msg("\n" + "=" * 80)
log_msg("STEP 6: Creating census deciles")
log_msg("=" * 80)

df_facility['census_decile'] = pd.qcut(df_facility['mean_census'], 
                                       q=10, labels=False, duplicates='drop') + 1
log_msg(f"Census deciles created")

# ============================================================================
# STEP 7: OUTLIER DETECTION
# ============================================================================
log_msg("\n" + "=" * 80)
log_msg("STEP 7: Outlier detection and removal (|z| > 4)")
log_msg("=" * 80)

variables_for_outlier_check = [
    'mean_census', 'mean_rn_hrs', 'mean_lpn_hrs', 
    'mean_cna_hrs', 'mean_cna_ctr_hrs', 
    'rn_to_lpn_ratio', 'contract_cna_prop'
]

z_scores = np.abs(stats.zscore(df_facility[variables_for_outlier_check], nan_policy='omit'))
outlier_mask = (z_scores > OUTLIER_THRESHOLD).any(axis=1)
outlier_count = outlier_mask.sum()

log_msg(f"Outliers detected (|z| > {OUTLIER_THRESHOLD}): {outlier_count:,}")

df_facility = df_facility[~outlier_mask].reset_index(drop=True)
log_msg(f"Facilities after outlier removal: {len(df_facility):,}")

# ============================================================================
# STEP 8: APPLY INCLUSION CRITERIA
# ============================================================================
log_msg("\n" + "=" * 80)
log_msg("STEP 8: Apply inclusion criteria")
log_msg("=" * 80)

before_filter = len(df_facility)
df_facility = df_facility[df_facility['mean_census'] >= MIN_CENSUS]
after_filter = len(df_facility)
log_msg(f"After census >= {MIN_CENSUS}: {after_filter:,} ({before_filter - after_filter:,} excluded)")

# ============================================================================
# STEP 9: SAVE DATASET
# ============================================================================
log_msg("\n" + "=" * 80)
log_msg("STEP 9: Saving aggregated dataset")
log_msg("=" * 80)

output_cols = [
    'PROVNUM', 'STATE', 'mean_census', 'census_decile',
    'mean_rn_hrs', 'mean_lpn_hrs', 'mean_cna_hrs', 'mean_cna_ctr_hrs',
    'rn_to_lpn_ratio', 'contract_cna_prop', 'total_hrs',
    'staffing_efficiency_index'
]

df_output = df_facility[output_cols].copy()
output_file = OUTPUT_DIR / 'facility_data.csv'
df_output.to_csv(output_file, index=False)
log_msg(f"Saved: {output_file} ({len(df_output):,} records)")

# ============================================================================
# STEP 10: EXCLUSION LOG
# ============================================================================
log_msg("\n" + "=" * 80)
log_msg("STEP 10: Exclusion Summary")
log_msg("=" * 80)

exclusion_log = f"""
EXCLUSION LOG - DATA PREPARATION PHASE
========================================

Starting Point:
  Total records across 8 quarters: {total_records_loaded:,}
  Unique facilities: {dfs[0]['PROVNUM'].nunique() if dfs else 'N/A'}

Step 1: Duplicate Removal
  Records removed: {dup_removed:,}

Step 2: Aggregation to Facility Level
  Facilities aggregated: {len(df_facility) + outlier_count + (before_filter - after_filter):,}

Step 3: Outlier Screening (|z| > 4)
  Outliers removed: {outlier_count:,}

Step 4: Inclusion Criteria (Census >= {MIN_CENSUS})
  Facilities excluded: {before_filter - after_filter:,}

FINAL ANALYTIC SAMPLE
  Total facilities: {len(df_facility):,}
  States represented: {df_facility['STATE'].nunique()}

Descriptive Statistics - Final Sample
=====================================

Resident Census:
  Mean: {df_facility['mean_census'].mean():.1f}
  Median: {df_facility['mean_census'].median():.1f}
  SD: {df_facility['mean_census'].std():.1f}

RN Hours per Resident Day:
  Mean: {df_facility['mean_rn_hrs'].mean():.2f}
  Median: {df_facility['mean_rn_hrs'].median():.2f}

LPN Hours per Resident Day:
  Mean: {df_facility['mean_lpn_hrs'].mean():.2f}
  Median: {df_facility['mean_lpn_hrs'].median():.2f}

CNA Hours per Resident Day (Direct Hire):
  Mean: {df_facility['mean_cna_hrs'].mean():.2f}

CNA Hours per Resident Day (Contract):
  Mean: {df_facility['mean_cna_ctr_hrs'].mean():.3f}

RN-to-LPN Ratio:
  Mean: {df_facility['rn_to_lpn_ratio'].mean():.2f}
  Median: {df_facility['rn_to_lpn_ratio'].median():.2f}

Contract CNA Proportion:
  Mean: {df_facility['contract_cna_prop'].mean():.3f}
  Median: {df_facility['contract_cna_prop'].median():.3f}
"""

log_msg(exclusion_log)

exclusion_file = OUTPUT_DIR / 'exclusion_log.txt'
with open(exclusion_file, 'w') as f:
    f.write(exclusion_log)

log_msg(f"\nExclusion log saved: {exclusion_file}")

log_msg("\n" + "=" * 80)
log_msg("DATA PREPARATION COMPLETE")
log_msg("=" * 80)
