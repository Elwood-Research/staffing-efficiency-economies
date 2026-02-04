#!/usr/bin/env python3
"""
Script 2: Descriptive Statistics and Table 1
Objective: Generate facility characteristics stratified by census decile
Output: LaTeX Table 1, histograms, correlation matrix
"""

import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURATION
# ============================================================================
OUTPUT_DIR = Path('/study/04-analysis/outputs')
TABLES_DIR = OUTPUT_DIR / 'tables'
FIGURES_DIR = OUTPUT_DIR / 'figures'

# ============================================================================
# LOAD DATA
# ============================================================================
print("=" * 80)
print("STEP 1: Loading aggregated facility data")
print("=" * 80)

df = pd.read_csv(OUTPUT_DIR / 'facility_data.csv')
print(f"Facilities loaded: {len(df):,}")

# ============================================================================
# TABLE 1: FACILITY CHARACTERISTICS BY DECILE
# ============================================================================
print("\n" + "=" * 80)
print("STEP 2: Creating Table 1 - Facility Characteristics by Census Decile")
print("=" * 80)

# Calculate statistics by decile
table1_data = []

for decile in sorted(df['census_decile'].unique()):
    subset = df[df['census_decile'] == decile]
    n = len(subset)
    
    census_median = subset['mean_census'].median()
    census_q1 = subset['mean_census'].quantile(0.25)
    census_q3 = subset['mean_census'].quantile(0.75)
    
    rn_mean = subset['mean_rn_hrs'].mean()
    rn_sd = subset['mean_rn_hrs'].std()
    
    lpn_mean = subset['mean_lpn_hrs'].mean()
    lpn_sd = subset['mean_lpn_hrs'].std()
    
    cna_mean = (subset['mean_cna_hrs'] + subset['mean_cna_ctr_hrs']).mean()
    cna_sd = (subset['mean_cna_hrs'] + subset['mean_cna_ctr_hrs']).std()
    
    rn_lpn_ratio_mean = subset['rn_to_lpn_ratio'].mean()
    rn_lpn_ratio_sd = subset['rn_to_lpn_ratio'].std()
    
    contract_cna_mean = subset['contract_cna_prop'].mean()
    contract_cna_sd = subset['contract_cna_prop'].std()
    
    eff_index_mean = subset['staffing_efficiency_index'].mean()
    eff_index_sd = subset['staffing_efficiency_index'].std()
    
    table1_data.append({
        'Decile': f'Decile {int(decile)}',
        'N': n,
        'Census_Median': f'{census_median:.0f}',
        'Census_IQR': f'{census_q1:.0f}-{census_q3:.0f}',
        'RN_Mean': f'{rn_mean:.2f}',
        'RN_SD': f'{rn_sd:.2f}',
        'LPN_Mean': f'{lpn_mean:.2f}',
        'LPN_SD': f'{lpn_sd:.2f}',
        'CNA_Mean': f'{cna_mean:.2f}',
        'CNA_SD': f'{cna_sd:.2f}',
        'RN_LPN_Ratio_Mean': f'{rn_lpn_ratio_mean:.2f}',
        'RN_LPN_Ratio_SD': f'{rn_lpn_ratio_sd:.2f}',
        'Contract_CNA_Mean': f'{contract_cna_mean:.3f}',
        'Contract_CNA_SD': f'{contract_cna_sd:.3f}',
        'Eff_Index_Mean': f'{eff_index_mean:.3f}',
        'Eff_Index_SD': f'{eff_index_sd:.3f}'
    })

# Add overall row
overall_subset = df
table1_data.append({
    'Decile': 'Overall',
    'N': len(overall_subset),
    'Census_Median': f'{overall_subset["mean_census"].median():.0f}',
    'Census_IQR': f'{overall_subset["mean_census"].quantile(0.25):.0f}-{overall_subset["mean_census"].quantile(0.75):.0f}',
    'RN_Mean': f'{overall_subset["mean_rn_hrs"].mean():.2f}',
    'RN_SD': f'{overall_subset["mean_rn_hrs"].std():.2f}',
    'LPN_Mean': f'{overall_subset["mean_lpn_hrs"].mean():.2f}',
    'LPN_SD': f'{overall_subset["mean_lpn_hrs"].std():.2f}',
    'CNA_Mean': f'{(overall_subset["mean_cna_hrs"] + overall_subset["mean_cna_ctr_hrs"]).mean():.2f}',
    'CNA_SD': f'{(overall_subset["mean_cna_hrs"] + overall_subset["mean_cna_ctr_hrs"]).std():.2f}',
    'RN_LPN_Ratio_Mean': f'{overall_subset["rn_to_lpn_ratio"].mean():.2f}',
    'RN_LPN_Ratio_SD': f'{overall_subset["rn_to_lpn_ratio"].std():.2f}',
    'Contract_CNA_Mean': f'{overall_subset["contract_cna_prop"].mean():.3f}',
    'Contract_CNA_SD': f'{overall_subset["contract_cna_prop"].std():.3f}',
    'Eff_Index_Mean': f'{overall_subset["staffing_efficiency_index"].mean():.3f}',
    'Eff_Index_SD': f'{overall_subset["staffing_efficiency_index"].std():.3f}'
})

df_table1 = pd.DataFrame(table1_data)

# Create LaTeX table
latex_table1 = r"""
\begin{table}[htbp]
\centering
\caption{Facility Characteristics Stratified by Resident Census Decile}
\label{tab:facility_chars}
\small
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{lccccccccc}
\toprule
\textbf{Census Decile} & \textbf{N} & \textbf{Median Census [IQR]} & \textbf{RN Hrs/PRD} & \textbf{LPN Hrs/PRD} & \textbf{CNA Hrs/PRD} & \textbf{RN-to-LPN Ratio} & \textbf{Contract CNA Prop.} & \textbf{Staffing Eff. Index} \\
\midrule
"""

for idx, row in df_table1.iterrows():
    if row['Decile'] == 'Overall':
        latex_table1 += r"\midrule" + "\n"
    
    latex_table1 += f"{row['Decile']} & {row['N']} & {row['Census_Median']} [{row['Census_IQR']}] & "
    latex_table1 += f"{row['RN_Mean']}±{row['RN_SD']} & "
    latex_table1 += f"{row['LPN_Mean']}±{row['LPN_SD']} & "
    latex_table1 += f"{row['CNA_Mean']}±{row['CNA_SD']} & "
    latex_table1 += f"{row['RN_LPN_Ratio_Mean']}±{row['RN_LPN_Ratio_SD']} & "
    latex_table1 += f"{row['Contract_CNA_Mean']}±{row['Contract_CNA_SD']} & "
    latex_table1 += f"{row['Eff_Index_Mean']}±{row['Eff_Index_SD']} \\\\\n"

latex_table1 += r"""
\bottomrule
\end{tabular}
\end{adjustbox}
\begin{tablenotes}
\small
\item \textit{Note}: PRD = per resident day. RN = Registered Nurse; LPN = Licensed Practical Nurse; CNA = Certified Nursing Assistant. 
All staffing hours represent mean ± standard deviation across facilities in each decile. Contract CNA proportion is the proportion 
of total CNA hours (direct hire + contract) provided by contract staff. Staffing Efficiency Index is a composite metric 
(0-1 scale) combining RN-to-LPN ratio, contract CNA reliance, and total staffing hours per resident.
\end{tablenotes}
\end{table}
"""

# Save LaTeX table
table1_file = TABLES_DIR / 'table1_facility_chars.tex'
with open(table1_file, 'w') as f:
    f.write(latex_table1)
print(f"Saved: {table1_file}")

# ============================================================================
# FIGURES: DISTRIBUTION HISTOGRAMS
# ============================================================================
print("\n" + "=" * 80)
print("STEP 3: Creating distribution figures")
print("=" * 80)

# Set plotting style
sns.set_style("whitegrid")
plt.rcParams['font.size'] = 11

# Figure 1a: Daily Resident Census (log scale)
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(df['mean_census'], bins=50, color='steelblue', edgecolor='black', alpha=0.7)
ax.set_xlabel('Daily Resident Census', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Facilities', fontsize=12, fontweight='bold')
ax.set_title('Distribution of Daily Resident Census Across Facilities', fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3)
# Add statistics
median_census = df['mean_census'].median()
ax.axvline(median_census, color='red', linestyle='--', linewidth=2, label=f'Median = {median_census:.0f}')
ax.legend()
plt.tight_layout()
fig1a_file = FIGURES_DIR / 'figure1a_census_histogram.png'
plt.savefig(fig1a_file, dpi=300, bbox_inches='tight')
print(f"Saved: {fig1a_file}")
plt.close()

# Figure 1b: RN-to-LPN Ratio
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(df['rn_to_lpn_ratio'], bins=50, color='darkgreen', edgecolor='black', alpha=0.7)
ax.set_xlabel('RN-to-LPN Ratio', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Facilities', fontsize=12, fontweight='bold')
ax.set_title('Distribution of RN-to-LPN Ratio Across Facilities', fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3)
# Add statistics
median_ratio = df['rn_to_lpn_ratio'].median()
ax.axvline(median_ratio, color='red', linestyle='--', linewidth=2, label=f'Median = {median_ratio:.2f}')
ax.legend()
plt.tight_layout()
fig1b_file = FIGURES_DIR / 'figure1b_rn_to_lpn_histogram.png'
plt.savefig(fig1b_file, dpi=300, bbox_inches='tight')
print(f"Saved: {fig1b_file}")
plt.close()

# Figure 1c: Contract CNA Proportion
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(df['contract_cna_prop'], bins=50, color='darkorange', edgecolor='black', alpha=0.7)
ax.set_xlabel('Contract CNA Proportion (0-1)', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Facilities', fontsize=12, fontweight='bold')
ax.set_title('Distribution of Contract CNA Proportion Across Facilities', fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3)
# Add statistics
median_contract = df['contract_cna_prop'].median()
ax.axvline(median_contract, color='red', linestyle='--', linewidth=2, label=f'Median = {median_contract:.3f}')
ax.legend()
plt.tight_layout()
fig1c_file = FIGURES_DIR / 'figure1c_contract_cna_histogram.png'
plt.savefig(fig1c_file, dpi=300, bbox_inches='tight')
print(f"Saved: {fig1c_file}")
plt.close()

# ============================================================================
# CORRELATION MATRIX
# ============================================================================
print("\n" + "=" * 80)
print("STEP 4: Creating correlation matrix")
print("=" * 80)

corr_vars = [
    'mean_census', 'mean_rn_hrs', 'mean_lpn_hrs', 
    'mean_cna_hrs', 'mean_cna_ctr_hrs',
    'rn_to_lpn_ratio', 'contract_cna_prop', 'staffing_efficiency_index'
]

corr_df = df[corr_vars].corr()

# Save correlation matrix
corr_file = OUTPUT_DIR / 'correlation_matrix.csv'
corr_df.to_csv(corr_file)
print(f"Saved: {corr_file}")
print("\nCorrelation with Census:")
print(corr_df.loc['mean_census', :].sort_values(ascending=False))

# ============================================================================
# DISTRIBUTION DIAGNOSTICS
# ============================================================================
print("\n" + "=" * 80)
print("STEP 5: Distribution diagnostics")
print("=" * 80)

from scipy.stats import skew, kurtosis

diag_data = []
for col in corr_vars:
    diag_data.append({
        'Variable': col,
        'N': df[col].notna().sum(),
        'Mean': f'{df[col].mean():.3f}',
        'SD': f'{df[col].std():.3f}',
        'Min': f'{df[col].min():.3f}',
        'Max': f'{df[col].max():.3f}',
        'Skewness': f'{skew(df[col].dropna()):.3f}',
        'Kurtosis': f'{kurtosis(df[col].dropna()):.3f}'
    })

df_diag = pd.DataFrame(diag_data)
print(df_diag.to_string(index=False))

diag_file = OUTPUT_DIR / 'distribution_diagnostics.csv'
df_diag.to_csv(diag_file, index=False)
print(f"\nSaved: {diag_file}")

# ============================================================================
# MARKDOWN SUMMARY
# ============================================================================
print("\n" + "=" * 80)
print("STEP 6: Creating markdown summary")
print("=" * 80)

markdown_summary = f"""
# Descriptive Statistics Summary

## Overall Sample Characteristics
- **Total Facilities**: {len(df):,}
- **States Represented**: {df['STATE'].nunique()}

## Resident Census
- **Mean (±SD)**: {df['mean_census'].mean():.1f} ± {df['mean_census'].std():.1f} residents/day
- **Median [IQR]**: {df['mean_census'].median():.0f} [{df['mean_census'].quantile(0.25):.0f}-{df['mean_census'].quantile(0.75):.0f}]
- **Range**: {df['mean_census'].min():.0f} to {df['mean_census'].max():.0f}

## Staffing Hours per Resident Day
- **RN Hours**: {df['mean_rn_hrs'].mean():.3f} ± {df['mean_rn_hrs'].std():.3f}
- **LPN Hours**: {df['mean_lpn_hrs'].mean():.3f} ± {df['mean_lpn_hrs'].std():.3f}
- **CNA Hours (Direct Hire)**: {df['mean_cna_hrs'].mean():.3f} ± {df['mean_cna_hrs'].std():.3f}
- **CNA Hours (Contract)**: {df['mean_cna_ctr_hrs'].mean():.4f} ± {df['mean_cna_ctr_hrs'].std():.4f}
- **Total Staffing Hours**: {(df['mean_rn_hrs'] + df['mean_lpn_hrs'] + df['mean_cna_hrs'] + df['mean_cna_ctr_hrs']).mean():.2f} ± {(df['mean_rn_hrs'] + df['mean_lpn_hrs'] + df['mean_cna_hrs'] + df['mean_cna_ctr_hrs']).std():.2f}

## Key Outcomes
### RN-to-LPN Ratio
- **Mean (±SD)**: {df['rn_to_lpn_ratio'].mean():.2f} ± {df['rn_to_lpn_ratio'].std():.2f}
- **Median [IQR]**: {df['rn_to_lpn_ratio'].median():.2f} [{df['rn_to_lpn_ratio'].quantile(0.25):.2f}-{df['rn_to_lpn_ratio'].quantile(0.75):.2f}]

### Contract CNA Proportion
- **Mean (±SD)**: {df['contract_cna_prop'].mean():.3f} ± {df['contract_cna_prop'].std():.3f}
- **Median [IQR]**: {df['contract_cna_prop'].median():.3f} [{df['contract_cna_prop'].quantile(0.25):.3f}-{df['contract_cna_prop'].quantile(0.75):.3f}]
- **Min-Max**: {df['contract_cna_prop'].min():.3f} to {df['contract_cna_prop'].max():.3f}

### Staffing Efficiency Index
- **Mean (±SD)**: {df['staffing_efficiency_index'].mean():.3f} ± {df['staffing_efficiency_index'].std():.3f}
- **Range**: {df['staffing_efficiency_index'].min():.3f} to {df['staffing_efficiency_index'].max():.3f}

## Census Decile Distribution
"""

for decile in sorted(df['census_decile'].unique()):
    subset = df[df['census_decile'] == decile]
    n = len(subset)
    markdown_summary += f"\n- **Decile {int(decile)}**: {n:,} facilities (median census: {subset['mean_census'].median():.0f})"

print(markdown_summary)

summary_file = OUTPUT_DIR / 'descriptive_summary.md'
with open(summary_file, 'w') as f:
    f.write(markdown_summary)
print(f"\nSaved: {summary_file}")

print("\n" + "=" * 80)
print("DESCRIPTIVE STATISTICS COMPLETE")
print("=" * 80)
