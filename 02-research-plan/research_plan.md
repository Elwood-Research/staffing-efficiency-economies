# Research Plan: Staffing Mix Efficiency and Economies of Scale in Nursing Homes

## 1. STUDY DESIGN AND RATIONALE

### 1.1 Study Design
This is a **cross-sectional analysis** examining the relationship between nursing home facility size and staffing composition. The study investigates whether larger facilities achieve economies of scale through more efficient staffing mix (characterized by higher Registered Nurse-to-Licensed Practical Nurse ratios) or whether they rely more heavily on contract Certified Nursing Assistants to manage scale. The analysis aggregates daily staffing hours across a four-quarter study period to generate facility-level staffing metrics for comparison.

### 1.2 Rationale
Nursing home staffing decisions represent a critical intersection of clinical quality, financial sustainability, and labor economics. While prior literature demonstrates that nursing home staffing levels correlate with resident outcomes and facility financial performance, less is known about *how* staffing is composed across facility sizes. Larger facilities may benefit from greater specialization and economies of scale in recruiting and retaining higher-credentialed nursing staff (Registered Nurses). Conversely, they may rely more heavily on contract Certified Nursing Assistants to achieve flexibility in scaling the care workforce. This study leverages the Centers for Medicare & Medicaid Services Payroll-Based Journal, a comprehensive daily staffing reporting system for all Medicare-certified nursing homes, to examine whether facility size systematically predicts staffing mix efficiency.

### 1.3 Theoretical Framework

#### Transaction Cost Economics (TCE) Perspective
Transaction Cost Economics posits that organizations choose between internalization of functions (employee hiring) and externalization (contract labor) based on asset specificity, uncertainty, and frequency of transactions. Smaller facilities may face high per-unit costs of recruiting, training, and retaining full-time clinical staff, incentivizing contract labor use. Medium-sized facilities may experience the highest contract reliance if they lack the scale to justify full-time investment but face high volatility in resident census. Larger facilities achieve sufficient scale to amortize recruitment and training costs across more residents, enabling full-time staffing. This framework predicts a **non-monotonic relationship** between facility size and contract CNA proportion.

#### Donabedian Structure-Process-Outcome Model
This foundational health services framework organizes the relationship between facility resources (structure—staffing), clinical practices (process), and resident outcomes. Facility size directly affects staffing structure through labor market access, financial capacity, and management infrastructure. The structure of staffing—particularly the ratio of higher-credentialed (RN) to lower-credentialed (LPN) staff—reflects institutional choices about quality versus cost. This study examines the structural dimension, documenting how facility size predicts staffing composition choices.

#### Agency Theory
Agency Theory describes the principal-agent relationship between facility owners (principals) and management (agents). For-profit and non-profit nursing homes may exhibit different staffing composition choices due to differing incentive structures. For-profit facilities may more aggressively pursue cost minimization through contract labor and lower RN-to-LPN ratios, while non-profit facilities with mission-driven governance may invest more heavily in permanent RN staffing to improve quality. Facility size may moderate these effects: larger for-profit facilities achieve sufficient scale to negotiate favorable contract terms, while larger non-profits may have greater philanthropic revenue to support higher nursing staffing. This framework predicts ownership-size interactions in staffing composition.

## 2. POPULATION DEFINITION AND SAMPLING

### 2.1 Target Population
All Medicare-certified nursing homes operating continuously during the study period (Calendar Year 2023 Quarter 1 through Calendar Year 2024 Quarter 4). The study population consists of approximately **10,000 to 12,000 facilities per quarter** reporting to the Centers for Medicare & Medicaid Services Payroll-Based Journal system.

### 2.2 Study Period
**January 1, 2023 through December 31, 2024** (four contiguous quarters: CY2023Q1, CY2023Q2, CY2023Q3, CY2023Q4, CY2024Q1, CY2024Q2, CY2024Q3, CY2024Q4)

**Justification for Study Period Selection:**
- **Post-pandemic stability**: 2023 represents the first full calendar year following the acute COVID-19 pandemic workforce disruptions, providing more stable staffing patterns for analysis.
- **Data completeness**: All quarters (CY2023Q1 through CY2024Q4) have complete documentation and verified data files.
- **Temporal sufficiency**: Four contiguous quarters provide adequate aggregation to smooth daily volatility in staffing patterns while maintaining sufficient temporal granularity.
- **Recent relevance**: The 2023-2024 period reflects contemporary nursing home staffing practices and provides immediately actionable findings for current policy and management decisions.

### 2.3 Unit of Analysis
The facility is the unit of analysis. Daily staffing hours are aggregated across the four-quarter study period to compute facility-level summary statistics (mean, total, ratio). This aggregation approach yields cross-sectional facility-level variables suitable for investigating facility-size associations.

### 2.4 Sampling Strategy
No sampling is employed. The study is a **complete enumeration** of all Medicare-certified nursing homes reporting to the PBJ system during the study period and meeting inclusion criteria.

## 3. INCLUSION AND EXCLUSION CRITERIA

### 3.1 Inclusion Criteria
1. **Medicare Certification**: Facility is Medicare-certified as of the first day of the study period (January 1, 2023).
2. **Operational Continuity**: Facility operates for the entire study period without changes in Medicare certification status. All four quarters of daily data are present (minimum of 89 operating days per quarter, allowing for holiday reporting variations).
3. **Key Variable Completeness**: For each facility-quarter combination, complete non-missing values are present for:
   - Daily Resident Census (MDScensus)
   - Registered Nurse Hours (Hrs_RN, employee and contract components)
   - Licensed Practical Nurse Hours (Hrs_LPN, employee and contract components)
   - Certified Nursing Assistant Hours (Hrs_CNA, employee and contract components)
4. **Valid Facility Identifiers**: PROVNUM (Medicare provider number) and STATE are non-missing and valid (PROVNUM is 6-character numeric; STATE is valid 2-character postal abbreviation).
5. **Minimum Facility Size**: Facility reports a median daily resident census of at least 20 residents across the study period. This threshold excludes very small facilities (<20 beds) that may have data quality or reliability concerns due to high day-to-day volatility.

### 3.2 Exclusion Criteria
1. **Incomplete Census Data**: Median daily resident census is <1 resident during any study quarter, indicating administrative errors or inactive facilities.
2. **Incomplete Staffing Reporting**: More than 10% of days within the study period have missing values for any key staffing variable (Hrs_RN, Hrs_LPN, Hrs_CNA, Hrs_CNA_ctr).
3. **Missing Facility Information**: PROVNUM, PROVNAME, or STATE are missing or invalid.
4. **Non-Medicare Status**: Facility lacks Medicare certification at any point during the study period, or PBJ reporting is discontinued.
5. **Severe Outliers (Statistical Screening)**: After aggregation to facility-level summaries, facilities with extreme values on continuous variables (absolute z-score > 4.0) are excluded from analysis. Continuous variables screened: mean daily resident census, total RN hours per resident-day, total LPN hours per resident-day, total CNA hours per resident-day, RN-to-LPN ratio, contract CNA proportion.
6. **Categorical Variable Imbalance**: For stratification variables (e.g., state), if a facility's state assignment would result in <5% representation in a stratum, the facility's stratum assignment is reconsidered or the facility is included only in collapsed analyses.

### 3.3 Exclusion Flow Chart and Expected Sample Sizes

```
Step 1: All Medicare-certified nursing homes reporting to PBJ, CY2023Q1-CY2024Q4
        ├─ Estimated population: 10,000-12,000 facilities/quarter
        └─ Total person-quarters: ~40,000-48,000 facility-quarter combinations

Step 2: Exclude facilities with non-continuous Medicare certification or missing quarters
        ├─ Estimated exclusion: ~1,500-2,000 facilities (1 or more missing quarters)
        └─ Remaining: ~8,500-10,500 facilities

Step 3: Exclude facilities with median census <20 residents
        ├─ Estimated exclusion: ~500-800 facilities (very small providers)
        └─ Remaining: ~8,000-10,000 facilities

Step 4: Exclude facilities with >10% missing daily staffing data in any quarter
        ├─ Estimated exclusion: ~400-600 facilities (data quality issues)
        └─ Remaining: ~7,400-9,400 facilities

Step 5: Exclude missing facility identifiers (PROVNUM, STATE, PROVNAME)
        ├─ Estimated exclusion: <100 facilities
        └─ Remaining: ~7,400-9,400 facilities

Step 6: Aggregate to facility level; exclude extreme outliers (|z| > 4 on key variables)
        ├─ Estimated exclusion: ~200-300 facilities (statistical outliers)
        └─ **Final Analytic Sample: ~7,100-9,100 facilities**

Step 7: Stratify final sample by daily resident census deciles for comparison tables
        └─ Each decile: ~710-910 facilities
```

**Expected Final Analytic Sample Size: 7,100-9,100 nursing home facilities** with complete data across all four study quarters (CY2023Q1-CY2024Q4).

## 4. DATA COLLECTION PROCEDURES AND QUARTERS SELECTED

### 4.1 Data Source: Payroll-Based Journal
All data are extracted from the Centers for Medicare & Medicaid Services Payroll-Based Journal (PBJ) system, a mandatory daily staffing reporting platform for all Medicare and Medicaid-participating nursing homes. The PBJ captures detailed paid hours for nursing, therapy, and administrative staff by staffing category and employment status (employee vs. contract/per diem). Data are reported daily by each facility to CMS and are made available for research through secure data-sharing agreements.

### 4.2 Quarters Selected and Justification
**Primary Study Period: CY2023Q1, CY2023Q2, CY2023Q3, CY2023Q4, CY2024Q1, CY2024Q2, CY2024Q3, CY2024Q4**

All selected quarters have complete documentation (Data Dictionary CSV files and Documentation Markdown files) confirming variable definitions, data quality standards, and reporting requirements. The four-quarter span:
- Provides ~360 daily observations per facility, adequate for reliable facility-level aggregation
- Captures two full calendar years, enabling detection of seasonal patterns if present
- Falls entirely within the post-pandemic period (2023 onward), ensuring contemporary relevance
- Excludes periods of acute pandemic workforce disruptions (2020-2022), which would confound the analysis

### 4.3 Data Access and Processing
Raw daily PBJ data are extracted from secure CMS databases and processed locally to ensure data privacy and compliance with HIPAA requirements. All analysis operates on facility-level aggregated statistics (means, totals, ratios) rather than individual daily records. Facility-level data contain no individually identifiable resident health information and fall outside HIPAA's minimum necessary scope.

## 5. VARIABLE DEFINITIONS AND MEASUREMENT

### 5.1 Primary Exposure Variable
**Exposure: Daily Resident Census (continuous and stratified)**

| Variable | Definition | Unit | Range | Notes |
|----------|-----------|------|-------|-------|
| Daily Resident Census | Number of residents in the facility each day, derived from Minimum Data Set (MDS) assessments | Count per day | 1-1,500+ | Objective census metric from federal MDS assessment system; highly reliable. |

**Aggregated Exposure (Facility-Level):**
- **Mean Daily Census**: Average daily resident count across all days in the study period per facility
- **Median Daily Census**: Median daily resident count; robust to outliers
- **Decile Stratification**: Facilities ranked into 10 equal-sized groups (deciles) based on median daily census for comparison table construction

### 5.2 Primary Outcome Variables

#### Outcome 1: Registered Nurse-to-Licensed Practical Nurse Ratio
| Component | Definition | Unit | Notes |
|-----------|-----------|------|-------|
| RN Hours (Total) | Sum of paid hours for Registered Nurses (employee + contract) | Hours per day | Aggregated daily across study period |
| LPN Hours (Total) | Sum of paid hours for Licensed Practical Nurses (employee + contract) | Hours per day | Aggregated daily across study period |
| **RN-to-LPN Ratio** | RN Hours ÷ LPN Hours | Ratio | Calculated at facility level; values >1 indicate RN predominance |

**Hypothesis 1 Prediction**: RN-to-LPN ratio increases monotonically with facility size (positive association with daily resident census).

#### Outcome 2: Contract Certified Nursing Assistant Proportion
| Component | Definition | Unit | Notes |
|-----------|-----------|------|-------|
| Contract CNA Hours | Sum of paid hours for contract/per diem Certified Nursing Assistants | Hours per day | `Hrs_CNA_ctr` aggregated daily |
| Total CNA Hours | Sum of all paid hours for CNAs (employee + contract) | Hours per day | `Hrs_CNA` total aggregated daily |
| **Contract CNA Proportion** | Contract CNA Hours ÷ Total CNA Hours | Proportion (0-1) | Facility-level; 0 = all employee CNAs; 1 = all contract CNAs |

**Hypothesis 2 Prediction**: Contract CNA proportion follows an inverted-U (quadratic) pattern with facility size, peaking in mid-sized facilities (median daily census 50-150 residents).

#### Outcome 3: Staffing Efficiency Index (Derived)
| Component | Definition | Unit | Notes |
|-----------|-----------|------|-------|
| **Staffing Efficiency Index** | (RN Hours + LPN Hours) ÷ Total Caregiving Hours | Index (0-1) | Numerator: Higher-credentialed staff; Denominator: RN + LPN + CNA hours. Range [0,1]; higher values = more RN/LPN intensive; lower values = more CNA intensive. |

**Theoretical Basis**: Reflects the proportion of direct care delivered by credentialed nurses versus assistants; higher values indicate efficiency gains through skill substitution or task reorganization.

### 5.3 Covariates (Facility-Level Characteristics)

#### Temporal and Geographic Indicators
| Covariate | Definition | Type | Category |
|-----------|-----------|------|----------|
| Study Quarter | Calendar quarter (2023Q1 through 2024Q4) | Categorical | Temporal control; captures seasonal patterns |
| State | Facility state of location (two-letter postal abbreviation) | Categorical | Geographic control; captures state-level regulatory variation |
| Census Division | Nine-region U.S. Census Bureau division | Categorical | Geographic control; higher-level regional aggregation |

#### Facility Characteristics
| Covariate | Definition | Type | Data Source | Notes |
|-----------|-----------|------|-------------|-------|
| Facility Provider Number | Medicare provider identification number | Identifier | PBJ | Used for linkage to external facility characteristics databases (if available) |
| Facility Name | Official facility name | Identifier | PBJ | Used for verification and facility matching |

**Note on Ownership Variables**: The PBJ daily staffing data do not include direct ownership (for-profit vs. non-profit) or chain affiliation variables. If ownership data become available through supplementary CMS databases (e.g., Care Compare, CMS Provider of Services file), these will be linked by PROVNUM to enable stratified analyses. Analyses including ownership will be conducted as sensitivity/secondary analyses.

### 5.4 Facility-Level Aggregation Formula
For each facility, the following aggregations are computed from daily data:

$$\text{Mean Daily Census} = \frac{1}{T} \sum_{t=1}^{T} \text{MDScensus}_t$$

$$\text{Mean RN Hours} = \frac{1}{T} \sum_{t=1}^{T} (\text{Hrs\_RN\_emp}_t + \text{Hrs\_RN\_ctr}_t)$$

$$\text{Mean LPN Hours} = \frac{1}{T} \sum_{t=1}^{T} (\text{Hrs\_LPN\_emp}_t + \text{Hrs\_LPN\_ctr}_t)$$

$$\text{Mean CNA Hours (Employee)} = \frac{1}{T} \sum_{t=1}^{T} \text{Hrs\_CNA\_emp}_t$$

$$\text{Mean CNA Hours (Contract)} = \frac{1}{T} \sum_{t=1}^{T} \text{Hrs\_CNA\_ctr}_t$$

$$\text{RN-to-LPN Ratio} = \frac{\text{Mean RN Hours}}{\text{Mean LPN Hours}}$$

$$\text{Contract CNA Proportion} = \frac{\text{Mean CNA Hours (Contract)}}{\text{Mean CNA Hours (Total)}}$$

where $T$ = number of operating days across the study period (approximately 360 days).

## 6. DATA QUALITY AND MISSING DATA PLAN

### 6.1 Data Quality Standards
The PBJ system is subject to CMS mandated reporting standards and periodic audits. All facilities are required to certify accuracy of submitted data. Nevertheless, we implement facility-level data quality screening:

1. **Completeness Check**: For each facility-quarter, assess the proportion of days with non-missing values for key variables. Facilities with >10% missingness in any quarter are excluded.
2. **Logical Consistency**: Verify that total hours (employee + contract) equal reported combined hours for each staffing category. Discrepancies indicate data entry errors; affected facility-quarters are flagged for exclusion.
3. **Range Validation**: Check that daily census values fall within expected range (≥0 and ≤1,500). Flag and exclude outliers.
4. **Temporal Continuity**: Verify that each facility has data spanning all four quarters with minimum coverage (89 days/quarter). Gaps indicate discontinued reporting or operational closure.

### 6.2 Missing Data Handling
**Daily-Level Missing Data (Within Facility-Quarter):**
- If a specific day is missing staffing data, that day is excluded from the facility's aggregation calculation (complete-case analysis).
- If >10% of days in a quarter are missing, the entire facility is excluded from analysis.

**Facility-Level Missing Data (After Aggregation):**
- If a facility has complete data for only 1, 2, or 3 quarters (not all 4), the facility is excluded.
- If a facility's aggregated variables (census decile, RN-to-LPN ratio, etc.) cannot be computed due to missing components (e.g., no LPN staff recorded in any day), the facility is excluded.

**Categorical Variable Missingness:**
- If state or facility identifiers are missing, the entire facility record is excluded (expected <1% of sample).

### 6.3 Sensitivity Analyses for Missing Data
If substantial missingness (5-10%) emerges in the final sample for specific variables, we will conduct sensitivity analyses:
1. **Complete-case analysis** (primary): Exclude facilities with any missingness (reported above).
2. **Imputation analysis** (sensitivity): Multiply-impute missing daily values using predictive mean matching within facility-state-quarter strata and refit models.
3. **Missing indicator method** (sensitivity): Create indicator variables for any missingness and include in regression models to assess whether patterns of missingness predict outcomes.

## 7. ANALYSIS PLAN OVERVIEW

### 7.1 Descriptive Statistics
**Table 1: Facility Characteristics Stratified by Daily Resident Census Deciles**

Primary descriptive table presenting:
- Number of facilities per decile
- Facility-level summary statistics by decile:
  - Mean daily resident census (and range)
  - Mean RN hours per facility per day (and SD)
  - Mean LPN hours per facility per day (and SD)
  - Mean CNA hours per facility per day (and SD)
  - Mean RN-to-LPN ratio (and SD)
  - Mean contract CNA proportion (and SD)
  - Staffing efficiency index (and SD)
- Geographic distribution (# states represented per decile; # Northeast/Midwest/South/West)
- Temporal coverage (# facilities with complete 4-quarter data)

This table provides visual evidence of whether staffing composition varies systematically by facility size (census decile).

### 7.2 Primary Regression Analyses
**Analysis 1: RN-to-LPN Ratio vs. Facility Size (Hypothesis 1)**

Fit restricted cubic spline (RCS) models with 3-4 internal knots positioned at quantiles of the daily census distribution. Model specification:

$$\text{RN-to-LPN Ratio}_i = \alpha + \beta_1 f(\text{Census}_i) + \beta_2 \text{State}_i + \beta_3 \text{Quarter}_i + \epsilon_i$$

where:
- $f(\text{Census}_i)$ = restricted cubic spline basis expansion of mean daily resident census
- Knots positioned at 25th, 50th, 75th percentiles of census distribution
- $\text{State}_i$ = indicator variables for state (50 levels)
- $\text{Quarter}_i$ = indicator variables for study quarter (4 levels: 2023Q1, Q2, Q3, Q4 [reference], 2024Q1, Q2, Q3, Q4)
- $\epsilon_i$ = residual error, assumed independent, normally distributed

**Expected Result (Hypothesis 1)**: Spline curve monotonically increases, with RN-to-LPN ratio rising as facility census increases, consistent with transaction cost economics predictions of scale economies in recruiting and retaining higher-credentialed nurses.

---

**Analysis 2: Contract CNA Proportion vs. Facility Size (Hypothesis 2)**

Fit restricted cubic spline models (same specification as Analysis 1) with contract CNA proportion as dependent variable:

$$\text{Contract CNA Proportion}_i = \alpha + \beta_1 f(\text{Census}_i) + \beta_2 \text{State}_i + \beta_3 \text{Quarter}_i + \epsilon_i$$

**Expected Result (Hypothesis 2)**: Spline curve exhibits an inverted-U (concave) shape, with contract CNA reliance peaking in mid-sized facilities (median daily census 50-150 residents) and declining at both smaller and larger sizes. This pattern reflects transaction cost economics: small facilities cannot justify full-time CNA hiring (high contract reliance); medium facilities face maximum workforce volatility (peak contract reliance); large facilities amortize permanent CNA hiring costs (lower contract reliance).

---

**Analysis 3: Staffing Efficiency Index vs. Facility Size**

Fit analogous spline model with staffing efficiency index as outcome. This composite measure captures the joint effect of facility size on the overall skill composition of the care workforce.

### 7.3 Model Diagnostics and Assumptions
1. **Linearity/Functional Form**: Spline basis expansions relax linearity assumptions and are chosen over polynomial terms to avoid extrapolation artifacts.
2. **Residual Normality**: Examine Q-Q plots and Shapiro-Wilk tests. Log transformation of skewed outcomes (e.g., contract CNA proportion) applied if needed.
3. **Heteroscedasticity**: Conduct Breusch-Pagan tests; if significant, fit robust standard errors clustered by state.
4. **Multicollinearity**: Examine variance inflation factors (VIF) for included covariates; VIF <5 indicates acceptable collinearity.
5. **Outlier Influence**: Examine residuals for extreme values (|z| > 4); flagged observations are excluded prior to final model fit.

### 7.4 Stratified Analyses
**Stratification 1: Ownership Type**
If ownership data (for-profit vs. non-profit) are successfully linked, repeat primary analyses separately within each ownership stratum. Test for ownership × census size interaction using:

$$\text{Outcome}_i = \alpha + \beta_1 f(\text{Census}_i) + \beta_2 \text{Ownership}_i + \beta_3 f(\text{Census}_i) \times \text{Ownership}_i + \ldots$$

**Stratification 2: Census Division (Geographic)**
Repeat primary analyses separately within each of nine U.S. Census divisions (Northeast, Midwest, South, West subdivisions). Fit a meta-analytic fixed-effects model to test for geographic heterogeneity:

$$\text{Effect Size}_d = \beta_d + \nu_d$$

where $\beta_d$ is the division-specific effect and $\nu_d$ is sampling error. Conduct Q-statistic test for heterogeneity across divisions.

### 7.5 Sensitivity Analyses

**Sensitivity 1: Extreme Outlier Exclusion (|z| > 4)**
Refit all primary models after excluding facilities with extreme values (|z| > 4 on any continuous outcome or exposure variable). Compare regression coefficients and confidence intervals to primary results.

**Sensitivity 2: Minimum Census Threshold Variation**
Refit models after excluding facilities with median daily census <30, <40, or <50 to assess robustness to small-facility exclusion threshold.

**Sensitivity 3: Quarterly Aggregation Method**
Instead of averaging across four quarters, fit models separately for each quarter and examine temporal consistency of facility size effects.

**Sensitivity 4: Ratio Stability (Alternative Outcome Specification)**
For the RN-to-LPN ratio, fit models with log-transformed ratio to normalize skewed distributions and ensure robustness of conclusions to functional form specification.

### 7.6 Data Envelopment Analysis (Secondary)
If resources permit, conduct non-parametric Data Envelopment Analysis (DEA) to estimate staffing efficiency frontiers. Inputs: daily resident census; Outputs: total RN + LPN hours (quality output) and total CNA hours (quantity output). Categorize facilities into efficiency quintiles and examine distribution of efficiency scores by facility size decile.

## 8. TIMELINE AND MILESTONES

| Phase | Milestone | Target Date | Duration |
|-------|-----------|-------------|----------|
| **Phase 1** | Literature review complete; 20+ citations collected | Week 1-2 | 2 weeks |
| **Phase 2** | Research plan finalized; hypotheses specified; variables confirmed | Week 3 | 1 week |
| **Phase 3** | Methods document and statistical analysis plan finalized | Week 4 | 1 week |
| **Phase 4** | Data preparation and descriptive statistics completed | Week 5-6 | 2 weeks |
| **Phase 4 (cont.)** | Primary regression analyses and STROBE flow diagram completed | Week 7 | 1 week |
| **Phase 5** | Manuscript draft completed (methods, results, discussion) | Week 8-9 | 2 weeks |
| **Phase 5 (cont.)** | Manuscript revisions and finalization; PDF generated | Week 10 | 1 week |
| **Phase 6** | Presentation slides prepared (10 slides, LaTeX Beamer format) | Week 11 | 1 week |
| **Phase 7** | Git repository initialized; files committed and pushed to GitHub | Week 12 | 1 week |
| **Publication** | Manuscript published on GitHub; repository made public | Week 12 | Same day |

**Total Timeline**: 12 weeks from literature review initiation to publication.

## 9. BUDGET AND RESOURCES

### 9.1 Data Resources
- **PBJ Data Access**: Secured through CMS research data repository; no licensing fees.
- **Facility Characteristics**: Optional supplementary linkage to CMS Provider of Services file (publicly available; no cost).

### 9.2 Computational Resources
- **Docker Container (pbj-analysis-vault)**: Python-based analysis environment; containerized for data security and reproducibility.
- **Required Python Libraries**: pandas, numpy, scipy, statsmodels, matplotlib, seaborn (all open-source).
- **Statistical Software**: R or Python (open-source); RCS models via statsmodels or rms packages.
- **Document Preparation**: LaTeX with natbib for bibliography management; pdf generation via latexmk or pdflatex.

### 9.3 Personnel and Time
- **Analyst (Full-Time Equivalent)**: 0.3 FTE × 12 weeks = ~3.6 weeks effort for data preparation, analysis, manuscript, and publication.
- **Senior Researcher (Oversight)**: ~0.1 FTE × 12 weeks for quality assurance and substantive interpretation.

### 9.4 Quality Assurance Checkpoints
1. **Data Validation (Week 6)**: Confirm sample sizes, distribution of key variables, and absence of anomalies.
2. **Analysis Validation (Week 7)**: Peer review of regression model specifications, assumption checking, and result interpretation.
3. **Manuscript Review (Week 10)**: Final peer review for clarity, accuracy, and adherence to APA formatting standards.
4. **Publication Readiness (Week 12)**: Verification of GitHub repository structure, file completeness, and public accessibility.

---

**End of Research Plan**
