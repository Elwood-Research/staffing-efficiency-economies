# Inclusion and Exclusion Criteria: Staffing Mix Efficiency Study

## EXECUTIVE SUMMARY

This document specifies measurable, explicit inclusion and exclusion criteria for the research population. The study aims to generate a final analytic sample of **7,100–9,100 nursing home facilities** from an estimated starting population of **10,000–12,000 facilities per quarter**. All criteria are applied sequentially to generate the STROBE flow diagram.

---

## 1. INCLUSION CRITERIA (EXPLICIT AND MEASURABLE)

### 1.1 Criterion IC-1: Medicare Certification Status
**Criterion Statement**: Facility is Medicare-certified as of January 1, 2023 (first day of study period).

**Measurement**: Query CMS Medicare Enrollment Database (Provider of Services file) or PBJ database metadata for Medicare certification status indicator.

**Verification Method**:
- Confirmed by presence of valid 6-digit PROVNUM (Medicare provider number)
- Cross-referenced against CMS Provider of Services file (if available)

**Operationalization**: 
- PROVNUM is non-null and matches format: 6-digit numeric code
- Facility has continuous Medicare certification status throughout CY2023Q1-CY2024Q4

**Expected Outcome**: Excludes non-Medicare facilities and those with intermediate certification changes.

---

### 1.2 Criterion IC-2: Continuous Operation During Study Period
**Criterion Statement**: Facility maintains Medicare certification and submits PBJ reports continuously throughout the entire study period (January 1, 2023 – December 31, 2024).

**Measurement**: Check for data presence in all four study quarters (CY2023Q1, CY2023Q2, CY2023Q3, CY2023Q4, CY2024Q1, CY2024Q2, CY2024Q3, CY2024Q4).

**Operationalization**:
- Facility has ≥89 valid (non-missing) daily records per quarter (approximately 90 days/quarter; allows for holiday/weekend reporting exceptions)
- All four quarters present with no gaps (i.e., facility not closed mid-study)
- Data completeness: ≥89 days in each of 4 quarters = minimum 356 days across study period

**Verification Method**:
- For each facility-quarter combination, count rows in raw PBJ data file
- Verify date range covers expected quarter span (e.g., CY2023Q1 = Jan 1 – Mar 31, 2023)

**Expected Outcome**: Excludes facilities that close, merge, or suspend reporting mid-study.

---

### 1.3 Criterion IC-3: Complete Key Variable Data
**Criterion Statement**: Facility has complete, non-missing values for all key staffing variables across the study period.

**Measurement**: For each facility-quarter, check for missing (null or NA) values in core staffing variables.

**Key Variables Requiring Completeness**:
1. Daily Resident Census (`MDScensus`)
2. Registered Nurse Hours – Total (`Hrs_RN`)
3. Registered Nurse Hours – Employee (`Hrs_RN_emp`)
4. Registered Nurse Hours – Contract (`Hrs_RN_ctr`)
5. Licensed Practical Nurse Hours – Total (`Hrs_LPN`)
6. Licensed Practical Nurse Hours – Employee (`Hrs_LPN_emp`)
7. Licensed Practical Nurse Hours – Contract (`Hrs_LPN_ctr`)
8. Certified Nursing Assistant Hours – Total (`Hrs_CNA`)
9. Certified Nursing Assistant Hours – Employee (`Hrs_CNA_emp`)
10. Certified Nursing Assistant Hours – Contract (`Hrs_CNA_ctr`)

**Operationalization**:
- Missing value threshold: ≤10% of operating days per quarter may have missing values (allows for occasional reporting gaps)
- If >10% missing in any quarter or any variable → **EXCLUDE facility**
- Formula: 
  $$\text{Completeness Rate} = \frac{\text{Non-Missing Days}}{\text{Total Operating Days}} \times 100\%$$
  Requirement: ≥90% completeness per quarter

**Verification Method**:
- Query PBJ daily data for each facility-quarter
- Count non-null entries; calculate missing rate
- Flag facility if missing rate >10%

**Expected Outcome**: Excludes facilities with data quality issues (non-compliance, system errors, or periods of non-reporting).

---

### 1.4 Criterion IC-4: Valid Facility Identifiers
**Criterion Statement**: Facility has valid, non-missing identifiers that enable facility tracking and linkage.

**Required Identifiers**:
- **PROVNUM** (Medicare provider number): 6-digit numeric code; non-null
- **PROVNAME** (Facility name): Non-null text string
- **STATE** (State postal abbreviation): Valid 2-letter code (e.g., "AL", "CA", "NY"); non-null

**Operationalization**:
- PROVNUM format: matches regex `^\d{6}$` (exactly 6 digits)
- PROVNAME: non-null; length >3 characters
- STATE: matches valid U.S. state/territory code (50 states + DC + territories if applicable)

**Verification Method**:
- Check for null values in identifier fields
- Validate against state postal code reference list (USPS)

**Expected Outcome**: Excludes facilities with corrupted or missing identifiers, preventing data linkage issues.

---

### 1.5 Criterion IC-5: Minimum Facility Size (Bed Capacity)
**Criterion Statement**: Facility has a median daily resident census of at least 20 residents across the study period.

**Measurement**: Calculate median of daily resident census (MDScensus) across all operating days in study period.

**Operationalization**:
$$\text{Median Census}_i = \text{Median}(MDScensus_{i,1}, MDScensus_{i,2}, \ldots, MDScensus_{i,T})$$
where T ≈ 360 days across four quarters.

**Threshold**: 
- If Median Census ≥ 20 residents → **INCLUDE**
- If Median Census < 20 residents → **EXCLUDE**

**Rationale**: 
- Facilities <20 beds are extremely small assisted-living-equivalent facilities; staffing data quality is compromised by high day-to-day volatility
- Practical significance: <20 residents insufficient for meaningful staffing patterns
- Sample composition: Approximately 80% of PBJ facilities have ≥20 beds; this criterion excludes ~2,000–2,500 small facilities

**Verification Method**:
- For each facility, extract all MDScensus values across study period
- Calculate 50th percentile (median)
- Compare to threshold

**Expected Outcome**: Excludes approximately 500–800 very small facilities; sample becomes more homogeneous and comparable.

---

## 2. EXCLUSION CRITERIA (EXPLICIT AND MEASURABLE)

### 2.1 Criterion EC-1: Resident Census Too Low
**Criterion Statement**: Facility operates with a median daily resident census below 1 resident during any study quarter, indicating administrative errors or facility inactive status.

**Measurement**: For each facility-quarter, calculate median census.

**Operationalization**:
- If Median Census < 1 in any quarter → **EXCLUDE facility entirely**

**Rationale**: Indicates facility closure, data entry errors, or inactive status unsuitable for analysis.

**Expected Exclusion Count**: <50 facilities (<1% of sample).

---

### 2.2 Criterion EC-2: Incomplete Quarterly Data Submission
**Criterion Statement**: Facility fails to submit adequate daily staffing reports in any study quarter.

**Measurement**: Count valid daily records (non-null WorkDate and non-null staffing hours) per facility per quarter.

**Operationalization**:
- Minimum requirement: ≥89 valid daily records per quarter (approximately 90 days/quarter)
- If any quarter has <89 records → **EXCLUDE facility**
- Exception: Minor gaps (1-2 weeks) acceptable if facility documents holidays/temporary closure

**Rationale**: Ensures temporal continuity and data reliability for facility-level aggregation.

**Expected Exclusion Count**: 400–600 facilities (~5–7% of sample).

---

### 2.3 Criterion EC-3: High Missingness on Key Variables
**Criterion Statement**: Facility has >10% missing values on any required staffing variable in any quarter.

**Measurement**: For each facility-quarter and each key variable, calculate missing rate:
$$\text{Missing Rate} = \frac{\text{Number of Missing Days}}{{\text{Total Valid Days}}} \times 100\%$$

**Key Variables**:
- MDScensus
- Hrs_RN, Hrs_RN_emp, Hrs_RN_ctr
- Hrs_LPN, Hrs_LPN_emp, Hrs_LPN_ctr
- Hrs_CNA, Hrs_CNA_emp, Hrs_CNA_ctr

**Operationalization**:
- If missing rate >10% for **any** variable in **any** quarter → **EXCLUDE facility**
- Equivalently: Completeness must be ≥90% for all key variables in all quarters

**Rationale**: Incomplete data leads to biased facility-level aggregates; 10% threshold balances data quality with sample retention.

**Expected Exclusion Count**: Overlaps partially with IC-3; combined effect 400–600 facilities (~5–7%).

---

### 2.4 Criterion EC-4: Missing Facility Identifiers
**Criterion Statement**: Facility lacks valid, non-missing PROVNUM, PROVNAME, or STATE.

**Measurement**: Check for null/NA values in identifier fields.

**Operationalization**:
- PROVNUM null or non-6-digit → **EXCLUDE**
- PROVNAME null or very short (<3 characters) → **EXCLUDE**
- STATE null or invalid postal code → **EXCLUDE**

**Rationale**: Cannot reliably track or verify facility identity; impairs data linkage to external sources.

**Expected Exclusion Count**: <100 facilities (<1% of sample); most PBJ data are well-curated.

---

### 2.5 Criterion EC-5: Statistical Outliers (Univariate)
**Criterion Statement**: Facility exhibits extreme values on continuous variables that are inconsistent with typical nursing home operations (|z-score| > 4.0).

**Measurement**: For each facility, calculate z-scores on the following continuous variables:

**Variables Screened for Outliers**:
1. Median daily resident census
2. Mean RN hours per day
3. Mean LPN hours per day
4. Mean CNA hours per day
5. RN-to-LPN ratio (derived)
6. Contract CNA proportion (derived)
7. Staffing efficiency index (derived)

**Operationalization**:
$$z_i = \frac{x_i - \bar{x}}{s_x}$$

where $\bar{x}$ = sample mean, $s_x$ = sample SD

**Outlier Threshold**: |z| > 4.0 (equivalent to >4 standard deviations from mean; probability <0.01%)

**Decision Rule**:
- If **any** variable has |z| > 4.0 → **FLAG facility for potential exclusion**
- Before exclusion, investigate whether extreme value represents legitimate operational variation (e.g., specialized dementia care facility with very high staffing)
- If legitimate, retain facility; if data error or artifact, exclude
- Final decision documented in data cleaning log

**Expected Exclusion Count**: 200–300 facilities (~2–3% of sample) after investigation.

---

### 2.6 Criterion EC-6: Categorical Stratum Size Too Small
**Criterion Statement**: For stratified analyses (by state, census division), exclude facilities whose stratum membership would result in <5% of the analytic sample.

**Measurement**: After all other exclusions, calculate stratum membership distribution.

**Operationalization**:
- If a stratum (e.g., specific state or census division) contains <5% of remaining sample:
  - Option A: Exclude all facilities in that stratum, or
  - Option B: Collapse stratum into adjacent/related categories
- Example: If a state contains <355 facilities in a 7,100-facility sample, consider collapsing into regional category

**Decision**: Made during analysis phase; documented in methods.

**Expected Impact**: Minimal; most states have adequate representation in PBJ.

---

## 3. INCLUSION/EXCLUSION FLOW CHART WITH EXPECTED SAMPLE SIZES

```
┌──────────────────────────────────────────────────────────────────────┐
│ STEP 0: All Medicare-Certified Nursing Homes Reporting to PBJ         │
│ CY2023Q1 through CY2024Q4                                             │
│                                                                        │
│ STARTING POPULATION: ~10,000–12,000 facilities/quarter                │
│ Total person-quarters: ~40,000–48,000 (facility-quarter records)      │
└──────────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────────┐
│ STEP 1: Apply IC-1 & IC-2 (Medicare Certification & Continuous Op)   │
│                                                                        │
│ Exclude: Facilities with any quarter missing or non-continuous status │
│ Decision: Must have data in all 4 quarters (CY2023Q1, Q2, Q3, Q4,     │
│           CY2024Q1, Q2, Q3, Q4)                                       │
│                                                                        │
│ EXCLUSION: ~1,500–2,000 facilities (~15% of population)              │
│ REMAINING: ~8,500–10,500 facilities                                  │
└──────────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────────┐
│ STEP 2: Apply IC-5 (Minimum Facility Size ≥20 Beds)                  │
│                                                                        │
│ Exclude: Facilities with median daily resident census <20             │
│ Decision: Median Census ≥ 20 required                                 │
│                                                                        │
│ EXCLUSION: ~500–800 facilities (~5–8% of remaining)                  │
│ REMAINING: ~8,000–10,000 facilities                                  │
└──────────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────────┐
│ STEP 3: Apply IC-3 & EC-3 (Staffing Data Completeness ≥90%)          │
│                                                                        │
│ Exclude: Facilities with >10% missing on any key staffing variable   │
│ Decision: ≥89 days per quarter with complete key variable data       │
│           in ALL key variables (Hrs_RN, Hrs_LPN, Hrs_CNA, etc.)      │
│                                                                        │
│ EXCLUSION: ~400–600 facilities (~4–6% of remaining)                  │
│ REMAINING: ~7,400–9,400 facilities                                   │
└──────────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────────┐
│ STEP 4: Apply IC-4 (Valid Identifiers)                               │
│                                                                        │
│ Exclude: Facilities with missing/invalid PROVNUM, PROVNAME, or STATE │
│ Decision: All three identifiers must be present and valid             │
│           PROVNUM = 6-digit code                                      │
│           STATE = valid postal abbreviation                           │
│                                                                        │
│ EXCLUSION: <100 facilities (<1% of remaining)                        │
│ REMAINING: ~7,400–9,400 facilities                                   │
└──────────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────────┐
│ STEP 5: Apply EC-1 (Minimum Census Level >0)                         │
│                                                                        │
│ Exclude: Facilities with median daily census <1 in any quarter       │
│ Decision: Indicates facility closure or data error                    │
│                                                                        │
│ EXCLUSION: <50 facilities (<1% of remaining)                         │
│ REMAINING: ~7,400–9,400 facilities                                   │
└──────────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────────┐
│ STEP 6: Aggregate to Facility-Level & Apply EC-5 (Statistical        │
│         Outliers, |z| > 4)                                            │
│                                                                        │
│ Compute facility-level aggregates:                                    │
│   • Mean daily census                                                 │
│   • Mean RN hours per day                                             │
│   • Mean LPN hours per day                                            │
│   • Mean CNA hours per day                                            │
│   • RN-to-LPN ratio                                                   │
│   • Contract CNA proportion                                           │
│   • Staffing efficiency index                                         │
│                                                                        │
│ Calculate z-scores for each variable; flag |z| > 4.0                 │
│ Investigate and decide: legitimate outlier (retain) or data          │
│ artifact (exclude)                                                    │
│                                                                        │
│ EXCLUSION: ~200–300 facilities (~2–3% of remaining)                  │
│                                                                        │
│ ★★ FINAL ANALYTIC SAMPLE: ~7,100–9,100 facilities ★★                │
└──────────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────────┐
│ STEP 7 (Optional): Apply EC-6 (Stratum Size Threshold)               │
│                                                                        │
│ If stratified analyses reveal strata with <5% membership, apply      │
│ collapsing or exclusion rules                                         │
│                                                                        │
│ FINAL STRATIFIED ANALYTIC SAMPLE: ≥7,000 facilities (may vary        │
│ depending on collapsing decisions)                                    │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 4. EXPECTED SAMPLE SIZE AT EACH STEP (DETAILED)

| Step | Criterion(s) | Exclusion Description | Exclusion Count | % of Previous | Remaining N | % of Original |
|------|-------------|---------------------|-----------------|--------------|------------|-----|
| 0 | — | Starting population | — | — | 10,000–12,000 | 100% |
| 1 | IC-1, IC-2 | Non-continuous Medicare certification or missing quarters | 1,500–2,000 | 15% | 8,500–10,500 | 85% |
| 2 | IC-5 | Median census <20 residents | 500–800 | 6% | 8,000–10,000 | 80% |
| 3 | IC-3, EC-3 | >10% missing staffing data in any quarter | 400–600 | 5% | 7,400–9,400 | 74% |
| 4 | IC-4 | Missing/invalid PROVNUM, PROVNAME, or STATE | <100 | <1% | 7,400–9,400 | 74% |
| 5 | EC-1 | Median census <1 (facility closure/error) | <50 | <1% | 7,400–9,400 | 74% |
| 6 | EC-5 | Statistical outliers (\|z\| > 4) | 200–300 | 2–3% | **7,100–9,100** | **71–73%** |
| 7 | EC-6 | Stratum size <5% (if applicable) | 0–100 | 0–1% | 7,000–9,100 | 70–73% |

**Final Analytic Sample**: **7,100–9,100 nursing home facilities** with complete data across all four study quarters (CY2023Q1–CY2024Q4).

---

## 5. STRATUM-SPECIFIC SAMPLE SIZES

### 5.1 By Daily Resident Census Decile

After final sample determination (N = 7,100–9,100), facilities are stratified by median daily resident census into 10 equal-sized groups (deciles):

| Decile | Census Range (Estimated) | Facility Count | % of Sample | Role in Analysis |
|--------|--------------------------|-----------------|-------------|------------------|
| 1 (Smallest) | 20–38 | 710–910 | 10% | Reference group for RN-to-LPN ratio regression |
| 2 | 39–49 | 710–910 | 10% | Comparison for size effects |
| 3 | 50–59 | 710–910 | 10% | Comparison for size effects |
| 4 | 60–70 | 710–910 | 10% | Predicted peak contract CNA proportion (H2) |
| 5 | 71–82 | 710–910 | 10% | Predicted peak contract CNA proportion (H2) |
| 6 | 83–100 | 710–910 | 10% | Predicted peak contract CNA proportion (H2) |
| 7 | 101–125 | 710–910 | 10% | Predicted peak contract CNA proportion (H2) |
| 8 | 126–160 | 710–910 | 10% | Comparison for size effects |
| 9 | 161–220 | 710–910 | 10% | Comparison for size effects |
| 10 (Largest) | 221–1,500+ | 710–910 | 10% | Reference for large-facility comparison |

**Note**: Exact census ranges depend on the observed distribution in the final sample; these are estimates based on typical nursing home census patterns.

---

### 5.2 By Geographic Region (U.S. Census Division)

| Census Division | States Included | Expected N | % of Sample | Geographic Stratification Role |
|-----------------|-----------------|-----------|-------------|-------------------------------|
| Northeast | ME, NH, VT, MA, RI, CT, NY, NJ, PA | 800–1,000 | 11–14% | Sensitivity analysis for geographic heterogeneity (H4) |
| Midwest | OH, MI, IN, IL, WI, MN, IA, MO, ND, SD, NE, KS | 1,200–1,500 | 17–21% | Largest region; primary geographic control |
| South | DE, MD, VA, WV, KY, TN, NC, SC, GA, FL, AL, MS, LA, AR, OK, TX | 3,000–4,000 | 42–56% | Most facilities; additional regional sub-stratification possible |
| West | MT, ID, WY, CO, NM, AZ, UT, NV, CA, OR, WA, AK, HI | 1,100–1,600 | 15–22% | Sensitivity analysis for geographic heterogeneity (H4) |

**Expected Distribution**: South dominates (40–50% of sample); Northeast and West smaller but adequate for stratification.

---

## 6. RATIONALE FOR INCLUSION/EXCLUSION THRESHOLDS

### 6.1 Why Minimum 20-Bed Threshold (IC-5)?

| Justification | Evidence |
|---------------|----------|
| **Data Quality** | Facilities <20 beds have high day-to-day census volatility (±50%); aggregation less reliable |
| **Representativeness** | Excludes assisted-living-equivalent facilities; analysis focuses on traditional nursing homes |
| **Sample Homogeneity** | Reduces confounding from facility type variation |
| **Statistical Power** | Larger facilities (≥20 beds) have more stable estimates for regression analysis |
| **Prior Literature** | CMS and research databases typically exclude <20-bed facilities from analyses |
| **Expected Effect** | ~80% of PBJ facilities are ≥20 beds; loss of ~500–800 facilities is manageable |

---

### 6.2 Why 10% Missingness Threshold (IC-3, EC-3)?

| Justification | Evidence |
|---------------|----------|
| **Bias Concern** | Complete-case analysis is unbiased if missingness is random (MCAR); 10% threshold acceptable |
| **Sample Retention** | Stricter thresholds (e.g., 5%) would lose 1,000+ facilities; less than 10% allows moderate data quality gaps |
| **Precedent** | Published nursing home research typically allows 5–10% missingness |
| **Facility Compliance** | PBJ reporting is mandated; >10% missingness indicates non-compliance or system failure |
| **Aggregation Effect** | Missing occasional days (≤10%) minimally biases facility-level means; larger gaps problematic |

---

### 6.3 Why |z| > 4.0 for Outlier Threshold (EC-5)?

| Justification | Evidence |
|---------------|----------|
| **Statistical Rigor** | |z| > 4.0 = probability <0.01% under normal distribution; extreme by any standard |
| **False Positive Avoidance** | Less stringent thresholds (e.g., |z| > 3.0) would exclude legitimate specialized facilities |
| **Data Integrity** | Extreme outliers often represent data entry errors rather than true variation |
| **Sensitivity Analysis** | Primary analysis excludes |z| > 4.0; secondary analysis includes to test robustness |
| **Published Practice** | Health services research commonly uses |z| > 4.0 threshold for outlier detection |

---

## 7. SENSITIVITY ANALYSES FOR INCLUSION CRITERIA

### 7.1 Sensitivity Analysis 1: Varying Minimum Census Threshold

**Rationale**: Test robustness of findings to definition of "small facility."

**Procedure**: Refit primary models using alternative minimum census thresholds:
- Primary (IC-5): Median census ≥20
- Sensitivity A: Median census ≥30 (stricter)
- Sensitivity B: Median census ≥10 (more inclusive)

**Expected Outcome**: Findings should be robust across threshold variations; if results change substantially, report both and discuss implications.

---

### 7.2 Sensitivity Analysis 2: Varying Missingness Threshold

**Rationale**: Test robustness to data quality standards.

**Procedure**: Refit models using alternative missingness thresholds:
- Primary (IC-3): ≤10% missingness
- Sensitivity A: ≤5% missingness (stricter)
- Sensitivity B: ≤15% missingness (more inclusive)

**Expected Outcome**: Results should be qualitatively similar; if not, discuss what sample subset is driving differences.

---

### 7.3 Sensitivity Analysis 3: Outlier Handling

**Rationale**: Test whether extreme outliers drive findings.

**Procedure**:
- Primary analysis (EC-5): Exclude |z| > 4.0 outliers
- Sensitivity A: Exclude |z| > 3.0 outliers (more aggressive)
- Sensitivity B: Include all outliers; report model with and without outlier-robust standard errors

**Expected Outcome**: Coefficients and confidence intervals should remain stable; if they change, outliers are influential and should be discussed.

---

## 8. DOCUMENTATION AND REPORTING

For all exclusion decisions, maintain a detailed **data cleaning log** documenting:

| Field | Content | Example |
|-------|---------|---------|
| Facility ID (PROVNUM) | 6-digit code | 010001 |
| Facility Name | Formal name | Example Nursing Home, Inc. |
| Exclusion Step | Which criterion applied | EC-5 (statistical outlier) |
| Exclusion Reason | Specific reason | RN-to-LPN ratio z = 5.2 |
| Count Excluded | Number of facilities at this step | 1 |
| Cumulative Excluded | Running total | 234 |
| Investigator Notes | Additional context | Reviewed – appears to be legitimate specialized facility; retained on reconsideration |

**Final Report Requirement**: In manuscript Methods section, report:
1. Starting population size
2. Exclusion count at each step (with percentages)
3. Final analytic sample size and characteristics
4. STROBE flow diagram (visual)
5. Sensitivity analyses on inclusion criteria thresholds

---

## 9. STROBE FLOW DIAGRAM (TEXT-BASED TEMPLATE)

```
┌─────────────────────────────────────────────────────────────────────┐
│ Assessed for Eligibility (CY2023Q1–CY2024Q4)                        │
│                                                                      │
│ All Medicare-certified nursing homes reporting to PBJ               │
│                                                                      │
│ N = 10,000–12,000 facilities (~40K–48K facility-quarters)           │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
                    [Exclusion Decisions]
                              ↓
                    ┌──────────┴──────────┐
                    ↓                     ↓
            [Excluded N=]         [Included N=]
       
        1,500–2,000 excluded    8,500–10,500 included
        • Missing quarters           • All 4 quarters present
        • Non-continuous            • Continuous operation
          operation
                                  ↓
                        [Exclusion Decisions]
                                  ↓
                        ┌──────────┴──────────┐
                        ↓                     ↓
                [Excluded N=]         [Included N=]
           
            500–800 excluded      8,000–10,000 included
            • Census <20 beds     • Census ≥20 beds
                                  ↓
                        [Exclusion Decisions]
                                  ↓
                        ┌──────────┴──────────┐
                        ↓                     ↓
                [Excluded N=]         [Included N=]
           
            400–600 excluded      7,400–9,400 included
            • >10% missing data   • ≥90% complete data
            • Invalid identifiers • Valid identifiers
            • Minimum census <1   • Median census ≥1
                                  ↓
                        [Exclusion Decisions]
                                  ↓
                        ┌──────────┴──────────┐
                        ↓                     ↓
                [Excluded N=]         [Included N=]
           
            200–300 excluded      7,100–9,100 included
            • Outliers |z|>4.0    ★ FINAL ANALYTIC SAMPLE ★
                                  
                                  Stratified by:
                                  • Census decile (10 groups)
                                  • Geographic region
                                  • Time period (4 quarters)
```

---

## 10. CHECKLIST FOR INCLUSION/EXCLUSION APPLICATION

Before analysis, confirm:

- [ ] All six inclusion criteria (IC-1 through IC-5) applied systematically
- [ ] All six exclusion criteria (EC-1 through EC-6) applied systematically
- [ ] Data cleaning log maintained for all exclusion decisions
- [ ] Final analytic sample size calculated (target: 7,100–9,100)
- [ ] Decile stratification completed (each decile ~710–910 facilities)
- [ ] Geographic distribution verified (South ~40–50%, other regions balanced)
- [ ] Sensitivity analyses on thresholds planned
- [ ] STROBE flow diagram prepared
- [ ] Methods section includes complete exclusion reporting

---

**End of Inclusion and Exclusion Criteria Document**
