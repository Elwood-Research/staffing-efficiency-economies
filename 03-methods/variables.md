# Variable Definitions and Measurement: Staffing Mix Efficiency Study

## 1. VARIABLE MAPPING TABLE: PBJ VARIABLES TO HUMAN-READABLE LABELS

### 1.1 Facility Identifiers

| PBJ Variable | Human-Readable Label | Type | Description | Role | Units | Expected Range |
|--------------|---------------------|------|-------------|------|-------|-----------------|
| PROVNUM | Facility Provider Number | String | Medicare 6-digit provider identification number | Identifier | N/A | 000001–999999 |
| PROVNAME | Facility Name | String | Official registered nursing home name | Identifier | N/A | Text (50-100 chars typical) |
| STATE | State Postal Code | String | Two-letter postal abbreviation for facility state | Covariate (Geographic) | N/A | AL, AK, AZ, ..., WY (50 states + DC) |
| CITY | City | String | City where facility is located | Identifier | N/A | Text |
| COUNTY_NAME | County Name | String | County where facility is located | Covariate (Geographic) | N/A | Text |
| COUNTY_FIPS | County FIPS Code | Integer | Federal Information Processing Standards code (3 digits) for county | Covariate (Geographic) | Numeric | 001–999 (within state) |

### 1.2 Time Period Variables

| PBJ Variable | Human-Readable Label | Type | Description | Role | Units | Expected Range |
|--------------|---------------------|------|-------------|------|-------|-----------------|
| CY_Qtr | Study Quarter | String | Calendar year and quarter (format: YYYYQ#) | Covariate (Temporal) | N/A | 2023Q1, 2023Q2, 2023Q3, 2023Q4, 2024Q1, 2024Q2, 2024Q3, 2024Q4 |
| WorkDate | Reporting Date | Integer | Day for which staffing hours are reported (format: YYYYMMDD) | Identifier (Daily) | Date | 20230101 – 20241231 |

### 1.3 Facility Census (Exposure Variable)

| PBJ Variable | Human-Readable Label | Type | Description | Role | Units | Expected Range | Distributional Characteristics |
|--------------|---------------------|------|-------------|------|-------|-----------------|-------------------------------|
| MDScensus | Daily Resident Census | Integer | Number of nursing home residents present on reporting date (source: Minimum Data Set assessment) | **Exposure** | Residents per day | 1 – 1,500+ | Approximately normally distributed; slight right skew for very large facilities |

**Facility-Level Aggregates (Derived):**
- **Mean Daily Resident Census** = Average MDScensus across all operating days in study period per facility
- **Median Daily Resident Census** = Median MDScensus across all operating days in study period per facility
- **Census Decile** = Facility's rank-ordered position in deciles of median census distribution (Decile 1 = smallest; Decile 10 = largest)

---

## 2. NURSING STAFF HOURS VARIABLES (RAW AND AGGREGATED)

### 2.1 Registered Nurses (RN)

#### A. Director of Nursing (RN-DON)

| PBJ Variable | Human-Readable Label | Type | Source | Description | Role | Units | Notes |
|--------------|---------------------|------|--------|-------------|------|-------|-------|
| Hrs_RNDON | RN Director of Nursing – Total Hours | Numeric | PBJ Daily | Total paid hours for RN serving as Director of Nursing (employee + contract) | Component of RN total | Hours per day | Includes administrative and clinical duties |
| Hrs_RNDON_emp | RN Director of Nursing – Employee Hours | Numeric | PBJ Daily | Paid hours for RN-DON employed directly by facility (W2/regular payroll) | Subcomponent | Hours per day | |
| Hrs_RNDON_ctr | RN Director of Nursing – Contract Hours | Numeric | PBJ Daily | Paid hours for contracted/temporary RN-DON | Subcomponent | Hours per day | Per diem, agency, temporary; not permanently employed |

#### B. Registered Nurse (Administrative Duties)

| PBJ Variable | Human-Readable Label | Type | Source | Description | Role | Units | Notes |
|--------------|---------------------|------|--------|-------------|------|-------|-------|
| Hrs_RNadmin | RN with Administrative Duties – Total Hours | Numeric | PBJ Daily | Total paid hours for RN with administrative duties not including DON (e.g., compliance officer, nursing supervisor) | Component of RN total | Hours per day | |
| Hrs_RNadmin_emp | RN with Administrative Duties – Employee Hours | Numeric | PBJ Daily | Employee hours for RN with administrative duties | Subcomponent | Hours per day | |
| Hrs_RNadmin_ctr | RN with Administrative Duties – Contract Hours | Numeric | PBJ Daily | Contract hours for RN with administrative duties | Subcomponent | Hours per day | |

#### C. Registered Nurse (Clinical, Direct Care)

| PBJ Variable | Human-Readable Label | Type | Source | Description | Role | Units | Notes |
|--------------|---------------------|------|--------|-------------|------|-------|-------|
| Hrs_RN | Registered Nurse (Total) – Total Hours | Numeric | PBJ Daily | Total paid hours for all RNs providing direct patient care (clinical RNs; excludes RN-DON and RN with admin duties) | **Outcome Component** | Hours per day | Primary measure of RN staffing intensity |
| Hrs_RN_emp | Registered Nurse (Total) – Employee Hours | Numeric | PBJ Daily | Employee hours for clinical RNs | Subcomponent | Hours per day | Permanent, W2-employed RNs |
| Hrs_RN_ctr | Registered Nurse (Total) – Contract Hours | Numeric | PBJ Daily | Contract hours for clinical RNs | Subcomponent | Hours per day | Temporary, agency RNs |

**Aggregated RN Variables (Facility-Level):**
- **Mean RN Hours per Day** = Mean of (Hrs_RN + Hrs_RNadmin + Hrs_RNDON) across all operating days for each facility
- **Total RN Hours per Resident-Day** = (Sum of all RN hours across study period) ÷ (Total resident-days across study period) for each facility

---

### 2.2 Licensed Practical Nurses (LPN)

#### A. Licensed Practical Nurse (Administrative Duties)

| PBJ Variable | Human-Readable Label | Type | Source | Description | Role | Units | Notes |
|--------------|---------------------|------|--------|-------------|------|-------|-------|
| Hrs_LPNadmin | LPN with Administrative Duties – Total Hours | Numeric | PBJ Daily | Total paid hours for LPN with administrative duties (e.g., nursing supervisor, charge nurse) | Component of LPN total | Hours per day | |
| Hrs_LPNadmin_emp | LPN with Administrative Duties – Employee Hours | Numeric | PBJ Daily | Employee hours for LPN with administrative duties | Subcomponent | Hours per day | |
| Hrs_LPNadmin_ctr | LPN with Administrative Duties – Contract Hours | Numeric | PBJ Daily | Contract hours for LPN with administrative duties | Subcomponent | Hours per day | |

#### B. Licensed Practical Nurse (Clinical, Direct Care)

| PBJ Variable | Human-Readable Label | Type | Source | Description | Role | Units | Notes |
|--------------|---------------------|------|--------|-------------|------|-------|-------|
| Hrs_LPN | Licensed Practical Nurse – Total Hours | Numeric | PBJ Daily | Total paid hours for LPN providing direct patient care (excludes LPN with admin duties) | **Outcome Component** | Hours per day | Primary measure of LPN staffing intensity |
| Hrs_LPN_emp | Licensed Practical Nurse – Employee Hours | Numeric | PBJ Daily | Employee hours for clinical LPNs | Subcomponent | Hours per day | Permanent, W2-employed LPNs |
| Hrs_LPN_ctr | Licensed Practical Nurse – Contract Hours | Numeric | PBJ Daily | Contract hours for clinical LPNs | Subcomponent | Hours per day | Temporary, agency LPNs |

**Aggregated LPN Variables (Facility-Level):**
- **Mean LPN Hours per Day** = Mean of (Hrs_LPN + Hrs_LPNadmin) across all operating days for each facility
- **Total LPN Hours per Resident-Day** = (Sum of all LPN hours across study period) ÷ (Total resident-days across study period) for each facility

---

### 2.3 Certified Nursing Assistants (CNA)

| PBJ Variable | Human-Readable Label | Type | Source | Description | Role | Units | Notes |
|--------------|---------------------|------|--------|-------------|------|-------|-------|
| Hrs_CNA | Certified Nursing Assistant – Total Hours | Numeric | PBJ Daily | Total paid hours for CNA (employee + contract) providing direct care assistance | **Outcome Component** | Hours per day | Largest component of frontline care staff; primary support for ADL assistance |
| Hrs_CNA_emp | Certified Nursing Assistant – Employee Hours | Numeric | PBJ Daily | Employee hours for directly employed CNA | Subcomponent | Hours per day | Permanent, W2-employed CNAs |
| Hrs_CNA_ctr | Certified Nursing Assistant – Contract Hours | Numeric | PBJ Daily | Contract/per diem hours for CNA (temporary agency or per diem staff) | **Outcome Component** | Hours per day | **Primary measure for Hypothesis 2 (contract CNA reliance)** |

**Aggregated CNA Variables (Facility-Level):**
- **Mean CNA Hours per Day** = Mean of Hrs_CNA across all operating days for each facility
- **Mean Contract CNA Hours per Day** = Mean of Hrs_CNA_ctr across all operating days for each facility
- **Mean Employee CNA Hours per Day** = Mean of Hrs_CNA_emp across all operating days for each facility
- **Total CNA Hours per Resident-Day** = (Sum of all CNA hours across study period) ÷ (Total resident-days across study period) for each facility

---

### 2.4 Nurse Aide in Training (NAtrn)

| PBJ Variable | Human-Readable Label | Type | Source | Description | Role | Units | Notes |
|--------------|---------------------|------|--------|-------------|------|-------|-------|
| Hrs_NAtrn | Nurse Aide in Training – Total Hours | Numeric | PBJ Daily | Total paid hours for Nursing Aide in Training (employee + contract); these are individuals pursuing CNA certification | Supplementary | Hours per day | Typically small contribution; often 0 hours |
| Hrs_NAtrn_emp | Nurse Aide in Training – Employee Hours | Numeric | PBJ Daily | Employee hours for NAtrn | Subcomponent | Hours per day | |
| Hrs_NAtrn_ctr | Nurse Aide in Training – Contract Hours | Numeric | PBJ Daily | Contract hours for NAtrn | Subcomponent | Hours per day | |

**Note**: NAtrn hours are included in facility-level caregiving calculations for completeness but are not a primary focus of this study.

---

### 2.5 Medication Aide / Technician (MedAide)

| PBJ Variable | Human-Readable Label | Type | Source | Description | Role | Units | Notes |
|--------------|---------------------|------|--------|-------------|------|-------|-------|
| Hrs_MedAide | Medication Aide/Technician – Total Hours | Numeric | PBJ Daily | Total paid hours for Medication Aide or Medical Technician (employee + contract) | Supplementary | Hours per day | Specialized support role; may be LPN-trained or CNA-trained; varies by state regulations |
| Hrs_MedAide_emp | Medication Aide/Technician – Employee Hours | Numeric | PBJ Daily | Employee hours for MedAide | Subcomponent | Hours per day | |
| Hrs_MedAide_ctr | Medication Aide/Technician – Contract Hours | Numeric | PBJ Daily | Contract hours for MedAide | Subcomponent | Hours per day | |

**Note**: MedAide hours are used in supplementary caregiving calculations but are not a primary focus of this study.

---

## 3. DERIVED OUTCOME VARIABLES (FACILITY-LEVEL AGGREGATES)

### 3.1 Primary Outcome 1: Registered Nurse-to-Licensed Practical Nurse Ratio

**Definition:**
$$\text{RN-to-LPN Ratio}_i = \frac{\text{Mean RN Hours}_i}{\text{Mean LPN Hours}_i}$$

where:
- Mean RN Hours = Average daily hours for all RNs (clinical + administrative + DON) across study period
- Mean LPN Hours = Average daily hours for all LPNs (clinical + administrative) across study period
- Subscript i denotes individual facility

**Type:** Numeric (continuous)

**Units:** Ratio (dimensionless)

**Expected Range:** 0.2 to 2.5 (typical range across nursing homes)
- **Low ratio (0.2-0.4)**: Facilities with proportionally more LPNs than RNs; cost-focused staffing
- **Mid ratio (0.5-1.0)**: Balanced RN and LPN staffing
- **High ratio (1.5-2.5)**: Facilities with proportionally more RNs; quality-focused staffing

**Distributional Characteristics:** Right-skewed (some facilities with very high RN reliance); log-transformation may be applied for regression modeling.

**Outlier Screening:** Facilities with |z-score| > 4.0 on this ratio are excluded before analysis.

**Hypothesis 1 Prediction:** Mean RN-to-LPN ratio **increases** with facility median daily resident census (positive monotonic relationship).

---

### 3.2 Primary Outcome 2: Contract Certified Nursing Assistant Proportion

**Definition:**
$$\text{Contract CNA Proportion}_i = \frac{\text{Mean Contract CNA Hours}_i}{\text{Mean Total CNA Hours}_i}$$

where:
- Mean Contract CNA Hours = Average daily contract CNA hours across study period
- Mean Total CNA Hours = Average daily total CNA hours (employee + contract) across study period
- Subscript i denotes individual facility

**Type:** Numeric (continuous, bounded)

**Units:** Proportion (0 to 1, or 0% to 100%)

**Expected Range:** 0.0 to 1.0
- **Low proportion (0.0-0.15)**: Facilities rely exclusively on permanent employee CNAs
- **Mid proportion (0.20-0.50)**: Facilities use mixed permanent + contract CNA staffing
- **High proportion (0.60-1.0)**: Facilities rely heavily or exclusively on contract CNAs

**Distributional Characteristics:** Likely to be bimodal or multimodal (many facilities cluster at extremes: all-employee or all-contract); logit-transformation may improve model fit.

**Outlier Screening:** Facilities with |z-score| > 4.0 on this proportion are excluded before analysis.

**Hypothesis 2 Prediction:** Contract CNA proportion follows an **inverted-U (quadratic) pattern** with facility median daily resident census, peaking in mid-sized facilities (census 50-150).

---

### 3.3 Secondary Outcome 1: Staffing Efficiency Index

**Definition:**
$$\text{Staffing Efficiency Index}_i = \frac{\text{Mean RN Hours}_i + \text{Mean LPN Hours}_i}{\text{Mean RN Hours}_i + \text{Mean LPN Hours}_i + \text{Mean CNA Hours}_i}$$

**Interpretation:** Proportion of total direct caregiving staff hours provided by licensed nurses (RN + LPN) versus unlicensed assistants (CNA). Higher values indicate more licensed (higher-credentialed) staffing; lower values indicate more assistant-heavy staffing.

**Type:** Numeric (continuous, bounded)

**Units:** Index (0 to 1)

**Expected Range:** 0.20 to 0.70 (typical range across nursing homes)
- **Low efficiency (0.20-0.35)**: Predominantly CNA-staffed facilities; cost-minimized
- **Mid efficiency (0.35-0.50)**: Mixed licensed and assistant staffing
- **High efficiency (0.50-0.70)**: Predominantly licensed nurse staffing; quality-focused

**Distributional Characteristics:** Approximately normally distributed; slight bimodality possible.

**Outlier Screening:** Facilities with |z-score| > 4.0 are excluded before analysis.

---

### 3.4 Secondary Outcome 2: Total Hours per Resident-Day

**Definition (for each staffing category):**
$$\text{Total Hours per Resident-Day}_{category,i} = \frac{\sum_{t=1}^{T} \text{Staffing Hours}_{category,t}}{\sum_{t=1}^{T} \text{MDScensus}_{t}}$$

where:
- Staffing category ∈ {RN, LPN, CNA, Total Nursing}
- t indexes days across study period
- T ≈ 360 days

**Interpretation:** Staffing intensity; higher values indicate more staff per resident.

**Type:** Numeric (continuous)

**Units:** Hours of staff time per resident-day

**Expected Range:** 
- RN hours per resident-day: 0.05 to 0.50
- LPN hours per resident-day: 0.10 to 0.60
- CNA hours per resident-day: 0.50 to 1.50
- Total nursing hours per resident-day: 1.0 to 2.5

---

## 4. COVARIATE VARIABLES

### 4.1 Temporal Covariates

| Variable | Type | Values | Role | Rationale |
|----------|------|--------|------|-----------|
| Study Quarter | Categorical | 2023Q1, Q2, Q3, Q4; 2024Q1, Q2, Q3, Q4 | Control for seasonal variation | Q4 (October-December) often has higher staffing challenges; Q1-Q3 may differ |
| Calendar Year | Categorical | 2023, 2024 | Control for year-over-year changes | Captures any staffing policy changes between years |

---

### 4.2 Geographic Covariates

| Variable | Type | Values | Role | Rationale |
|----------|------|--------|------|-----------|
| State | Categorical | 50 states + DC (51 levels) | Control for state regulatory & labor market variation | State staffing regulations, nursing wage differentials, Medicaid payment rates vary significantly |
| Census Division | Categorical | Northeast, Midwest, South, West (9 divisions) | Higher-level geographic clustering | Reduces dimensionality for geographic heterogeneity testing |
| FIPS County Code | Numeric | 001-999 | Optional: County-level clustering (modeling) | Enables account for county-level labor market conditions |

---

### 4.3 Facility Characteristics (Contingent on Data Linkage)

The following variables are **not present in the raw PBJ daily staffing data** but may be linked via supplementary CMS data files if obtained:

| Variable | Type | Source | Role | Notes |
|----------|------|--------|------|-------|
| Ownership Type | Categorical | CMS Provider of Services (POS) File | Stratification (H3) | For-profit vs. Non-profit vs. Government |
| Chain Affiliation | Categorical | CMS POS File or proprietary databases | Stratification (optional) | Member of multi-facility chain vs. independent |
| Medicare Star Rating | Ordinal | CMS Care Compare | Sensitivity analysis (optional) | Facility quality indicator; may confound staffing-outcome relationships |
| Occupancy Rate | Numeric | Derived from MDScensus and bed count | Control variable | Proportion of licensed beds occupied; affects staffing decisions |

**Status:** These variables will be included **only if** successfully linked to PBJ data. Analyses without these linkages are feasible and are primary; analyses including these are secondary/sensitivity.

---

## 5. INCLUSION AND EXCLUSION CRITERIA: OPERATIONAL DEFINITIONS

### 5.1 Variable-Based Exclusion Criteria

#### Criterion 1: Minimum Facility Size
- **Operationalization**: Calculate median daily resident census (MDScensus) across all operating days in study period for each facility.
- **Threshold**: Median census < 20 residents → **EXCLUDE**
- **Rationale**: Very small facilities (<20 beds) have unreliable data quality due to high daily volatility and may not be representative of meaningful staffing patterns.

#### Criterion 2: Minimum Census Level
- **Operationalization**: Calculate median daily resident census for each facility.
- **Threshold**: Median census < 1 resident during any study quarter → **EXCLUDE**
- **Rationale**: Indicates facility closure, administrative error, or inactive status.

#### Criterion 3: Missing Staffing Data
- **Operationalization**: For each facility-quarter, count days with missing values for key variables (Hrs_RN, Hrs_LPN, Hrs_CNA, Hrs_CNA_ctr).
- **Threshold**: >10% missing days in any quarter → **EXCLUDE**
- **Rationale**: Data quality concerns; incomplete reporting indicates non-compliance or system issues.

#### Criterion 4: Missing Key Identifiers
- **Operationalization**: Check for missing or invalid PROVNUM, STATE, PROVNAME.
- **Threshold**: Any missing on these fields → **EXCLUDE**
- **Rationale**: Cannot reliably link or track facility records.

#### Criterion 5: Statistical Outliers (Multivariate)
- **Operationalization**: Calculate z-scores for all continuous facility-level variables (median census, mean RN hours, mean LPN hours, mean CNA hours, RN-to-LPN ratio, contract CNA proportion).
- **Threshold**: |z-score| > 4.0 on **any** continuous variable → **FLAG for exclusion**
- **Decision**: Extreme outliers excluded unless they represent legitimate operational variation (e.g., very specialized facilities). Final exclusion decision made during data cleaning phase with documentation.

---

### 5.2 Temporal Inclusion Criteria

#### Criterion 6: Complete Four-Quarter Data
- **Operationalization**: Check that each facility has data present for all four quarters (CY2023Q1, Q2, Q3, Q4, CY2024Q1, Q2, Q3, Q4).
- **Threshold**: Missing any complete quarter → **EXCLUDE**
- **Rationale**: Ensures temporally stable facility-level aggregates; excludes facilities with mid-study operational changes.

#### Criterion 7: Minimum Operating Days per Quarter
- **Operationalization**: Count days with non-missing staffing data per facility per quarter.
- **Threshold**: <89 days in any quarter (approximately 3 months) → **EXCLUDE**
- **Rationale**: Allows for ~1 week of holiday reporting gaps but excludes facilities with substantial non-reporting.

---

## 6. OUTLIER SCREENING AND REMOVAL PROTOCOL

### 6.1 Univariate Outlier Screening

**Procedure**: For each continuous variable, calculate z-scores:
$$z_i = \frac{x_i - \bar{x}}{s_x}$$

where $\bar{x}$ is the mean and $s_x$ is the standard deviation across all facilities.

**Threshold**: |z| > 4.0 indicates extreme outlier.

**Variables Screened**:
1. Median daily resident census
2. Mean RN hours per day
3. Mean LPN hours per day
4. Mean CNA hours per day
5. RN-to-LPN ratio
6. Contract CNA proportion
7. Staffing efficiency index
8. Total nursing hours per resident-day

**Action**: Facilities with |z| > 4.0 on **any** variable are flagged and excluded prior to regression analysis. Number of excluded facilities documented.

### 6.2 Multivariate Outlier Screening

**Procedure**: Optional; if sample includes highly multivariate outliers not detected by univariate screening, apply Mahalanobis distance test (if modeling allows).

**Threshold**: Mahalanobis distance > 99th percentile of χ² distribution with k degrees of freedom.

**Decision**: If multivariate outliers are detected, conduct primary analysis with and without these facilities to assess robustness.

---

## 7. CATEGORICAL VARIABLE THRESHOLD FOR STRATIFICATION

For categorical variables used in stratification (state, census division, quarter), apply minimum cell size rule:

**Criterion**: Exclude a facility from stratum if its cell would contain <5% of the sample in that stratum.

**Example**: If a particular state contains <5% of the analytic sample (e.g., <355 facilities in a 7,100-facility sample), analyses stratified by state may exclude or collapse this state.

**Decision**: Document any such collapsing or exclusions in methods section and sensitivity analyses.

---

## 8. SUMMARY TABLE: VARIABLE ROLES IN ANALYSIS

| Variable | Role | Measurement | Notes |
|----------|------|-------------|-------|
| **Daily Resident Census (MDScensus)** | **Exposure** (Primary) | Continuous | Facility-level aggregates: mean, median, deciles |
| **RN-to-LPN Ratio** | **Outcome 1** (Primary) | Continuous (ratio) | Hypothesis 1 tests monotonic increase with census |
| **Contract CNA Proportion** | **Outcome 2** (Primary) | Continuous (bounded 0-1) | Hypothesis 2 tests inverted-U pattern with census |
| **Staffing Efficiency Index** | **Outcome 3** (Secondary) | Continuous (bounded 0-1) | Exploratory; assesses overall staffing composition |
| **Study Quarter** | Covariate | Categorical (8 levels) | Controls for seasonal variation |
| **State** | Covariate | Categorical (51 levels) | Controls for state regulatory/labor market variation |
| **Census Division** | Covariate | Categorical (9 levels) | Higher-level geographic control |
| **Ownership Type** | Stratification/Covariate | Categorical (3 levels) | For Hypothesis 3 (if data available) |
| **Facility Provider Number** | Identifier | String | Used for data linkage; not included in models |
| **Facility Name** | Identifier | String | Used for data verification; not included in models |

---

## 9. AGGREGATION FORMULA SUMMARY

All facility-level variables are calculated using the following template:

$$\text{Facility-Level Variable}_{i} = f\left(\frac{1}{T} \sum_{t=1}^{T} \text{Daily Variable}_{i,t}\right)$$

where:
- $i$ indexes facilities
- $t$ indexes operating days within study period
- $T$ ≈ 360 days across four quarters
- $f(\cdot)$ is an aggregation function (mean, sum, ratio, etc.)

**Specific Aggregation Functions**:
- **Mean aggregates**: RN hours per day, LPN hours per day, CNA hours per day, contract CNA hours per day
- **Ratio aggregates**: RN-to-LPN ratio (computed from means), Contract CNA proportion (computed from means)
- **Indices**: Staffing efficiency index (computed from aggregated components)
- **Resident-day rates**: Total staffing hours per resident-day (sum of hours ÷ sum of census across period)

---

## 10. DATA PREPARATION CHECKLIST

Before analysis, verify:
- [ ] All PBJ daily data files present (CY2023Q1 through CY2024Q4)
- [ ] All documentation and data dictionaries present for selected quarters
- [ ] Facility-level variables successfully aggregated from daily data
- [ ] Outlier screening applied; count of excluded facilities documented
- [ ] No missing values remain in key variables (or missing data approach documented)
- [ ] Final analytic sample size calculated and verified (expected: 7,100-9,100 facilities)
- [ ] Variable distributions examined (histograms, summary statistics)
- [ ] Facility characteristics table (Table 1) prepared
- [ ] Stratum-specific sample sizes calculated (e.g., per census decile)

---

**End of Variables Document**
