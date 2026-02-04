# Methods: Staffing Mix Efficiency and Economies of Scale in Nursing Homes

## 1. Study Design and Setting

This study employs a **cross-sectional facility-level design** to examine the relationship between nursing home facility size and staffing composition efficiency. Cross-sectional analysis is appropriate for this research question because the primary objective is to characterize the association between facility size (measured by daily resident census) and staffing mix variables at a single time point, aggregated across a four-quarter study period. Unlike longitudinal designs that follow individual facilities over time to detect changes, this cross-sectional approach capitalizes on the wide variation in facility size across the Medicare-certified nursing home universe to test structural hypotheses about economies of scale in staffing decisions.

The study setting comprises all Medicare-certified nursing homes in the United States reporting daily staffing data to the Centers for Medicare & Medicaid Services Payroll-Based Journal system during the study period. Nursing homes were selected because they represent a standardized care environment where staffing composition is regulated (minimum staffing ratios), yet significant discretion exists in the use of registered nurses versus licensed practical nurses and in the proportion of contract versus employee-based nursing assistants. The geographic scope is national, encompassing all 50 states and the District of Columbia, which enables investigation of both within-facility and regional heterogeneity in staffing practices.

The study period spans **Calendar Year 2023 through Calendar Year 2024**, specifically the four contiguous quarters: CY2023 Quarter 1 (Q1), Q2, Q3, and Q4; and CY2024 Q1, Q2, Q3, and Q4. This eight-quarter timeframe was selected because it falls entirely within the post-acute COVID-19 pandemic period (after 2022), during which nursing home staffing patterns have stabilized following the acute workforce disruptions of 2020–2022. Furthermore, all eight quarters have complete and verified data documentation (Data Dictionary CSV files and Documentation Markdown files) confirming variable definitions, data quality standards, and reporting requirements. A four-quarter aggregation window (approximately 360 operating days per facility) provides adequate statistical power to smooth daily volatility in staffing while maintaining sufficient temporal granularity to detect facility-level patterns.

The unit of analysis is the individual nursing home facility. Daily staffing hours reported by each facility are aggregated across the entire study period to compute facility-level summary statistics: means, totals, ratios, and proportions. This aggregation approach yields cross-sectional facility-level variables suitable for regression analysis and facilitates interpretation of results in terms of typical staffing patterns by facility size.

---

## 2. Study Population

### 2.1 Target Population and Sampling

The target population comprises all Medicare-certified nursing homes operating continuously during the study period (January 1, 2023 through December 31, 2024). Based on CMS administrative records, approximately 10,000 to 12,000 Medicare-certified nursing homes report daily staffing data to the PBJ system each quarter. No sampling is employed for this study; the analysis is a **complete enumeration** of all facilities meeting inclusion criteria, subject to post-hoc exclusion screening described below.

The rationale for complete enumeration, rather than random sampling, is threefold. First, the accessible universe of nursing homes (those reporting to PBJ) is finite and well-defined, making enumeration feasible and efficient. Second, complete enumeration maximizes statistical power to detect associations and enables stratification into facility size deciles while maintaining adequate cell sizes within each stratum. Third, enumeration avoids selection bias that could arise from a sampling frame that systematically excludes certain types of facilities (e.g., very small or rural facilities), thereby compromising external validity.

### 2.2 Inclusion Criteria

Facilities are included in the study if they meet the following operational criteria:

**Criterion 1: Medicare Certification Status.** The facility must be Medicare-certified as of January 1, 2023 (the first day of the study period) according to CMS records. Medicare certification is verified via the facility's Centers for Medicare & Medicaid Services provider number (PROVNUM), which is a six-character numeric identifier assigned to each certified nursing home.

**Criterion 2: Operational Continuity Across Study Period.** The facility must operate continuously throughout the entire study period without changes in Medicare certification status (e.g., no facility closures, no changes from certified to non-certified status). Additionally, the facility must report staffing data for all four study quarters, with a minimum of 89 operating days per quarter (approximately three calendar months). This threshold allows for approximately one week of holiday reporting gaps or temporary closures while excluding facilities with substantial non-reporting periods that would compromise data quality.

**Criterion 3: Complete Key Variable Data.** For each facility-quarter combination, all key variables must have non-missing values: (a) Daily Resident Census (MDScensus), (b) Registered Nurse Hours (Hrs_RN and contract components), (c) Licensed Practical Nurse Hours (Hrs_LPN and contract components), and (d) Certified Nursing Assistant Hours (Hrs_CNA and contract components). These variables form the basis of both exposure and outcome definitions; missing values on any would prevent calculation of facility-level summaries.

**Criterion 4: Valid Facility Identifiers.** The facility must have valid, non-missing values for (a) PROVNUM (Medicare provider number, verified as a six-character numeric identifier), (b) STATE (two-character postal abbreviation), and (c) PROVNAME (facility name). These identifiers are essential for data linkage, verification, and stratification.

**Criterion 5: Minimum Facility Size.** The facility must report a median daily resident census of at least 20 residents across the study period. This threshold is employed to exclude very small facilities (< 20 beds) that exhibit high day-to-day census volatility and may have unreliable data quality due to small sample sizes and high proportional variability. Small facilities may also operate under substantially different business models (e.g., specialized care units, assisted living facilities misclassified as nursing homes) that are not comparable to the broader population of interest.

### 2.3 Exclusion Criteria

Facilities are excluded from the study if they meet any of the following criteria:

**Criterion 1: Inactive or Non-Operating Status.** If the median daily resident census falls below 1 resident during any study quarter, the facility is excluded. This criterion identifies administrative errors, facility closures, or inactive status during reporting periods.

**Criterion 2: Incomplete Staffing Data Reporting.** If more than 10% of days within any study quarter have missing values for any key staffing variable (Hrs_RN, Hrs_LPN, Hrs_CNA, Hrs_CNA_ctr), the facility is excluded from analysis. This threshold balances the need for data completeness with the recognition that rare days of missing data may occur due to technical issues or administrative delays. A 10% threshold corresponds to approximately 9 days per quarter, allowing for exceptional circumstances while screening out facilities with systematic non-compliance or data transmission failures.

**Criterion 3: Missing Facility Identifiers or Invalid Location Data.** Facilities with missing or invalid PROVNUM, STATE, or PROVNAME are excluded (expected to represent < 1% of the population) because these identifiers are essential for data verification and linkage to external facility characteristics.

**Criterion 4: Statistical Outliers (Multivariate Screening).** After aggregation to the facility level, facilities with extreme values (absolute z-score > 4.0) on any continuous variable are excluded. Continuous variables subjected to outlier screening include: (a) median daily resident census, (b) total registered nurse hours per resident-day, (c) total licensed practical nurse hours per resident-day, (d) total certified nursing assistant hours per resident-day, (e) registered nurse-to-licensed practical nurse ratio, and (f) contract certified nursing assistant proportion. The |z| > 4.0 threshold corresponds to values more than four standard deviations from the mean and is chosen to exclude extreme statistical outliers that likely represent data errors or highly specialized facilities not comparable to the general population. Application of this rule is expected to exclude approximately 200–300 facilities (2–4% of the sample).

**Criterion 5: Categorical Variable Imbalance (Rare Categories).** For stratification by categorical variables (e.g., state, census division), if a facility's stratum assignment would result in < 5% representation within that stratum, the facility's stratum assignment is reconsidered or the facility is included only in collapsed (higher-level) analyses. This criterion prevents analyses of extremely rare categories where inference becomes unreliable.

### 2.4 Expected Sample Size

After applying inclusion and exclusion criteria sequentially, the expected final analytic sample comprises **7,100 to 9,100 nursing home facilities** with complete data across all four study quarters. The expected sample size is calculated based on the hierarchical exclusion flow described in Table 1 below. Each stratum (census decile) is expected to contain approximately 710–910 facilities, enabling robust stratified analyses and decile-based comparisons.

#### Table 1: Expected Exclusion Flow and Final Sample Size

| Step | Inclusion/Exclusion Criterion | Expected Exclusions | Cumulative Remaining |
|------|-------------------------------|-------------------|-----------------------|
| 1 | All Medicare-certified nursing homes, CY2023Q1–CY2024Q4 | – | ~10,000–12,000 |
| 2 | Exclude: Non-continuous Medicare certification or missing quarters | ~1,500–2,000 | ~8,500–10,500 |
| 3 | Exclude: Median daily census < 20 residents | ~500–800 | ~8,000–10,000 |
| 4 | Exclude: > 10% missing daily staffing data in any quarter | ~400–600 | ~7,400–9,400 |
| 5 | Exclude: Missing facility identifiers (PROVNUM, STATE, PROVNAME) | < 100 | ~7,400–9,400 |
| 6 | Exclude: Statistical outliers (abs z-score > 4.0 on any continuous variable) | ~200–300 | ~7,100–9,100 |
| **Final** | **Complete analytic sample** | – | **~7,100–9,100 facilities** |

The expected sample represents approximately 70–75% of all Medicare-certified nursing homes reporting to PBJ during the study period. Facilities excluded due to incomplete data or missing quarters are expected to differ systematically from included facilities in terms of size, geographic region, and organizational characteristics; this potential selection bias is discussed in the Limitations section of the manuscript.

---

## 3. Data Sources and Collection Procedures

### 3.1 Payroll-Based Journal System Overview

All data for this study derive from the **Centers for Medicare & Medicaid Services Payroll-Based Journal (PBJ) system**, a mandatory daily staffing reporting platform for all Medicare and Medicaid-participating nursing homes. The PBJ was implemented by CMS in 2018 as a successor to the earlier quarterly Nursing Home Compare reporting system, with the explicit goal of improving data accuracy, timeliness, and granularity in nursing home staffing accountability. Each nursing home facility is required by regulatory statute to report daily paid staffing hours for all nursing and non-nursing personnel, stratified by employment status (employee vs. contract/per diem) and job category.

The PBJ system captures **paid hours only**; it does not include unpaid hours (e.g., on-call time, unpaid training, volunteer hours). Paid hours are those for which the facility compensates staff through payroll, agency payments, or contractual fees. This limitation is important for interpretation: the study reflects staffing hours that incur direct labor costs to the facility, not total time spent on-site or total work effort.

### 3.2 Data Quality Procedures

The PBJ system is subject to CMS mandated reporting standards and periodic audits. Each facility must certify the accuracy of submitted data, and CMS applies automated consistency checks to identify implausible values or logical errors. Facilities with identified data quality issues are notified and required to submit corrections. For this study, we implement additional facility-level data quality screening:

1. **Completeness Check**: For each facility-quarter, we calculate the proportion of operating days with non-missing values for key staffing variables (Hrs_RN, Hrs_LPN, Hrs_CNA, Hrs_CNA_ctr). Facilities with > 10% missingness in any quarter are excluded (described above).

2. **Logical Consistency Verification**: We verify that reported total hours (employee + contract combined hours) for each staffing category match or exceed component hours. Discrepancies exceeding 5% are flagged for review and may result in facility exclusion.

3. **Range Validation**: We check that daily census values fall within the plausible range (≥ 0 and ≤ 1,500 residents). Values outside this range are flagged as data entry errors; affected facility-quarters are excluded.

4. **Temporal Continuity Assessment**: We verify that each facility reports data spanning all four study quarters with minimum coverage (89 days per quarter). Facilities with gaps indicating discontinued reporting or operational changes are excluded.

### 3.3 Facility-Level Aggregation Procedure

Daily staffing hours reported by each facility are aggregated to the facility level using arithmetic means calculated across all operating days in the study period (approximately 360 days). For each facility, the following aggregation formulas are applied:

**Mean Daily Resident Census**: 
$$\text{Mean Census}_{i} = \frac{1}{T} \sum_{t=1}^{T} \text{MDScensus}_{i,t}$$

**Mean Registered Nurse Hours**:
$$\text{Mean RN Hours}_{i} = \frac{1}{T} \sum_{t=1}^{T} (\text{Hrs\_RN\_emp}_{i,t} + \text{Hrs\_RN\_ctr}_{i,t})$$

(This includes all RN hours: clinical RNs, administrative RNs, and RN Directors of Nursing.)

**Mean Licensed Practical Nurse Hours**:
$$\text{Mean LPN Hours}_{i} = \frac{1}{T} \sum_{t=1}^{T} (\text{Hrs\_LPN\_emp}_{i,t} + \text{Hrs\_LPN\_ctr}_{i,t})$$

(This includes all LPN hours: clinical and administrative.)

**Mean Certified Nursing Assistant Hours (Total and Contract)**:
$$\text{Mean CNA Hours (Total)}_{i} = \frac{1}{T} \sum_{t=1}^{T} \text{Hrs\_CNA}_{i,t}$$

$$\text{Mean CNA Hours (Contract)}_{i} = \frac{1}{T} \sum_{t=1}^{T} \text{Hrs\_CNA\_ctr}_{i,t}$$

where $i$ indexes individual facilities, $t$ indexes operating days, and $T \approx 360$ days across the four-quarter study period.

Missing daily values (rare, screened via the completeness check) are excluded from facility-level calculations using a complete-case approach. Facility-level summary statistics represent the average (mean) staffing composition across the study period, smoothing daily volatility and representing typical facility-level staffing patterns.

### 3.4 Data Linkages and External Facility Characteristics

The raw PBJ daily staffing data do not include variables for facility ownership type (for-profit vs. non-profit vs. government) or chain affiliation. If such supplementary data become available through CMS Provider of Services files or other data partners, these will be linked to the PBJ data via the facility's Medicare provider number (PROVNUM) to enable stratified and secondary analyses (see Section 7.4 below). Ownership and chain affiliation will be treated as **optional covariates** for secondary stratification; all primary analyses are conducted without these variables to ensure robustness to data linkage failures.

---

## 4. Variable Definitions and Measurement

### 4.1 Exposure Variable: Daily Resident Census (Facility Size)

The **primary exposure variable** in this study is the **Daily Resident Census**, defined as the number of nursing home residents present on each reporting date, derived from Minimum Data Set (MDS) assessments conducted by each facility. The MDS is a federally mandated, standardized comprehensive assessment tool completed for all nursing home residents; resident counts derived from MDS assessments represent an objective, validated measure of facility census and are far more reliable than administrative bed counts, which may not reflect actual occupancy.

For facility-level analysis, the daily resident census is aggregated to the facility level using two approaches: (a) **mean daily census** (arithmetic average across all operating days in the study period), and (b) **median daily census** (the median across all operating days). The median is more robust to extreme day-to-day fluctuations and is used as the primary basis for facility size classification. The expected range for daily resident census is 20–1,500 residents per facility; the distribution is approximately normal with a slight right skew reflecting the presence of very large specialized facilities.

**Census Decile Stratification**: Facilities are ranked and stratified into 10 equal-sized groups (deciles) based on median daily resident census. Decile 1 represents the smallest 10% of facilities (lowest median census); Decile 10 represents the largest 10% (highest median census). This decile-based stratification is used for descriptive comparisons in Table 1 (Facility Characteristics) and enables visual presentation of staffing patterns across the full range of facility sizes.

### 4.2 Primary Outcome Variable 1: Registered Nurse-to-Licensed Practical Nurse Ratio

The **first primary outcome variable** is the **Registered Nurse-to-Licensed Practical Nurse (RN-to-LPN) Ratio**, defined as the mean daily hours of registered nurses divided by the mean daily hours of licensed practical nurses, calculated at the facility level:

$$\text{RN-to-LPN Ratio}_{i} = \frac{\text{Mean RN Hours}_{i}}{\text{Mean LPN Hours}_{i}}$$

This ratio is dimensionless (a simple numeric ratio) and represents the staffing composition along the credential dimension. A ratio greater than 1.0 indicates that the facility employs proportionally more RN hours than LPN hours; a ratio less than 1.0 indicates greater reliance on LPNs.

**Justification for this outcome**: The RN-to-LPN ratio serves as a proxy for staffing quality composition. Registered nurses possess broader clinical training and licensure scope than licensed practical nurses, enabling RNs to undertake more complex clinical assessments, medication administration, wound care, and care coordination. In the Transaction Cost Economics framework, larger facilities with greater operational stability and financial capacity may invest more heavily in RN staffing as part of a quality-differentiation strategy. The RN-to-LPN ratio captures this compositional efficiency choice.

**Expected range and interpretation**: The RN-to-LPN ratio typically ranges from 0.2 to 2.5 across the population of nursing homes. A low ratio (0.2–0.4) indicates proportionally more LPN staffing, reflecting a cost-focused staffing strategy. A mid-range ratio (0.5–1.0) represents balanced RN and LPN staffing. A high ratio (1.5–2.5) indicates predominantly RN staffing, reflecting a quality-focused strategy. The distribution of this ratio is expected to be right-skewed due to a subset of facilities with very high RN reliance.

**Hypothesis 1 Prediction**: Under the Transaction Cost Economics and scale economies hypotheses, the RN-to-LPN ratio is predicted to **increase monotonically with facility size (median daily resident census)**. Larger facilities achieve economies of scale in recruiting, training, and retaining higher-credentialed nursing staff, enabling them to maintain proportionally more RN hours. This hypothesis predicts a positive regression coefficient when facility size is included as a predictor of the RN-to-LPN ratio.

### 4.3 Primary Outcome Variable 2: Contract Certified Nursing Assistant Proportion

The **second primary outcome variable** is the **Contract Certified Nursing Assistant (CNA) Proportion**, defined as the ratio of mean daily hours of contract CNAs to total mean daily hours of CNAs (employee plus contract):

$$\text{Contract CNA Proportion}_{i} = \frac{\text{Mean Contract CNA Hours}_{i}}{\text{Mean Total CNA Hours}_{i}}$$

This variable is bounded on the interval [0, 1], where 0 indicates exclusive reliance on employee (directly hired) CNAs, and 1 indicates exclusive reliance on contract (temporary, agency, per diem) CNAs. Values between 0 and 1 represent mixed use of employee and contract CNA staffing.

**Justification for this outcome**: The contract CNA proportion serves as a proxy for workforce flexibility and operational strategy. Certified nursing assistants provide the bulk of activities of daily living (ADL) assistance in nursing homes, comprising the largest component of the nursing-related workforce. Facilities face a discrete choice in staffing CNAs: invest in permanent employee hiring (with associated recruitment, training, and retention costs but stable staffing) or rely on contract agency staff (with higher per-hour costs but operational flexibility). Under Transaction Cost Economics theory, this choice depends on facility-specific factors including size, census volatility, and market conditions. The contract CNA proportion captures this labor allocation decision.

**Expected range and interpretation**: The contract CNA proportion typically ranges from 0.0 to 1.0. A low proportion (0.0–0.15) indicates facilities that employ primarily permanent employee CNAs. A mid-range proportion (0.20–0.50) represents facilities using mixed permanent and contract staffing. A high proportion (0.60–1.0) indicates heavy or exclusive reliance on contract CNAs. The distribution is expected to be multimodal or bimodal, with concentration at the extremes (all-employee or all-contract) reflecting binary strategic choices.

**Hypothesis 2 Prediction**: Under the Transaction Cost Economics framework, contract CNA proportion is predicted to follow an **inverted-U (quadratic or concave) pattern** with facility size. Small facilities (Decile 1–3; typically 20–60 residents) face high per-unit costs of recruiting and training permanent CNAs and thus rely heavily on contract labor. Mid-sized facilities (Decile 4–6; typically 60–150 residents) experience maximum workforce volatility and uncertainty, incentivizing contract labor reliance as a means of flexibility; this group is predicted to have the highest contract CNA proportion (the peak of the inverted-U). Large facilities (Decile 7–10; > 150 residents) achieve sufficient scale to justify permanent CNA hiring, amortizing recruitment and training costs across many residents, and thus have lower contract proportions. This hypothesis predicts a quadratic (concave) regression relationship when facility size is included as a predictor.

### 4.4 Derived Outcome Variable: Staffing Efficiency Index

A **secondary outcome variable** is the **Staffing Efficiency Index**, defined as the proportion of total direct caregiving staff hours provided by licensed nurses (RN + LPN) versus unlicensed assistants (CNAs):

$$\text{Staffing Efficiency Index}_{i} = \frac{\text{Mean RN Hours}_{i} + \text{Mean LPN Hours}_{i}}{\text{Mean RN Hours}_{i} + \text{Mean LPN Hours}_{i} + \text{Mean CNA Hours}_{i}}$$

This index is bounded on [0, 1], where higher values indicate greater proportional reliance on licensed nursing staff (higher "skill intensity") and lower values indicate greater proportional reliance on unlicensed assistants (lower "skill intensity").

**Justification**: The Staffing Efficiency Index captures the joint effect of facility size on the overall skill composition of the care workforce, combining information about both RN-LPN substitution and CNA reliance into a single composite measure. Higher values reflect staffing strategies emphasizing professional nursing quality; lower values reflect cost minimization through unlicensed assistant staffing. This index is exploratory and serves to validate findings from the primary outcome variables.

**Expected range**: The index typically ranges from 0.20 to 0.70, with 0.20–0.35 representing predominantly CNA-staffed (cost-minimized) facilities, 0.35–0.50 representing mixed licensed-assistant staffing, and 0.50–0.70 representing predominantly licensed nurse-staffed (quality-focused) facilities.

### 4.5 Covariates

#### Temporal Covariates

**Study Quarter** (CY_Qtr): A categorical variable with eight levels representing each quarter of the study period (2023Q1, Q2, Q3, Q4; 2024Q1, Q2, Q3, Q4). This covariate controls for seasonal variation in staffing patterns, as some quarters may experience predictable staffing challenges (e.g., Q4 with holiday staffing constraints) or staffing advantages (e.g., post-pandemic stabilization trends over time).

#### Geographic Covariates

**State**: A categorical variable representing the state in which the facility is located (50 states + District of Columbia; 51 levels). State-level covariates control for substantial variation in state regulatory requirements, Medicaid payment rates, nursing wage differentials, and labor market conditions that may systematically predict staffing composition independent of facility size effects.

**Census Division**: A categorical variable representing the nine-region U.S. Census Bureau division classification (Northeast, Middle Atlantic, East North Central, West North Central, South Atlantic, East South Central, West South Central, Mountain, Pacific). Census division provides a higher-level geographic clustering that reduces dimensionality in stratified analyses and enables assessment of regional heterogeneity in facility size–staffing relationships.

#### Optional Facility Characteristics (Contingent on Data Linkage)

The following variables are **not present in the raw PBJ staffing data** but may be incorporated if linked from supplementary CMS sources:

- **Ownership Type** (For-profit vs. Non-profit vs. Government): To enable stratified analyses examining whether the relationship between facility size and staffing composition differs by ownership structure (Hypothesis 3, secondary analysis).
- **Chain Affiliation** (Multi-facility chain vs. Independent): To assess whether membership in a multi-facility organization predicts staffing composition differences.

These variables will be incorporated **only if successfully linked** to the analytic sample; analyses without these linkages are primary and complete unto themselves.

### 4.6 Variable Mapping Table: PBJ Variables to Human-Readable Labels

**Table 2: Detailed Variable Mapping**

| PBJ Variable | Human-Readable Label | Type | Unit | Role in Analysis | Expected Range | Notes |
|--------------|---------------------|------|------|------------------|-----------------|-------|
| MDScensus | Daily Resident Census | Continuous | Residents/day | **Exposure** (Primary) | 20–1,500 | Derived from Minimum Data Set (MDS) assessments; aggregated to facility-level mean/median |
| Hrs_RN + Hrs_RN_ctr | Registered Nurse Hours (Total) | Continuous | Hours/day | **Outcome Component** (Primary 1) | 0–50 | Includes clinical RNs, administrative RNs, RN Director of Nursing; combined employee + contract hours |
| Hrs_LPN + Hrs_LPN_ctr | Licensed Practical Nurse Hours (Total) | Continuous | Hours/day | **Outcome Component** (Primary 1) | 0–30 | Includes clinical LPNs, administrative LPNs; combined employee + contract hours |
| Hrs_CNA | Certified Nursing Assistant Hours (Total) | Continuous | Hours/day | **Outcome Component** (Primary 2) | 0–100 | Total CNA hours (employee + contract); largest component of direct care workforce |
| Hrs_CNA_ctr | Certified Nursing Assistant Hours (Contract) | Continuous | Hours/day | **Outcome Component** (Primary 2) | 0–80 | Contract/temporary CNA hours; numerator for contract CNA proportion calculation |
| CY_Qtr | Study Quarter | Categorical | — | **Covariate** (Temporal) | 2023Q1–2024Q4 | Eight levels; controls for seasonal variation and temporal trends |
| STATE | State Postal Code | Categorical | — | **Covariate** (Geographic) | AL, AK, ..., WY | 51 levels including DC; controls for state regulatory and labor market variation |
| Census Division | U.S. Census Division | Categorical | — | **Covariate** (Geographic) | 1–9 | Nine regions; higher-level geographic clustering |
| PROVNUM | Facility Provider Number | String | — | **Identifier** | 000001–999999 | Medicare 6-digit provider identification; used for data linkage (not in models) |
| PROVNAME | Facility Name | String | — | **Identifier** | Various | Used for facility verification and matching (not in models) |

---

## 5. Statistical Methods

### 5.1 Descriptive Analysis

Descriptive statistics are presented in **Table 1: Facility Characteristics Stratified by Daily Resident Census Deciles**. This primary descriptive table presents facility counts, facility-level mean values, and standard deviations for all key variables, stratified by daily resident census decile. The table includes:

- **Number of facilities per decile**: Expected ~710–910 facilities per decile for a total sample of ~7,100–9,100.
- **Census summary statistics**: Mean and range of daily resident census within each decile.
- **Staffing hours**: Mean daily hours (and standard deviation) for RN, LPN, and CNA staffing across deciles.
- **Outcome variables**: Mean RN-to-LPN ratio, contract CNA proportion, and Staffing Efficiency Index (with SD) by decile.
- **Hours per resident-day**: Total RN, LPN, and CNA staffing intensity (hours of staff per resident-day) by decile.
- **Geographic distribution**: Number and percentage of facilities from each census region by decile.
- **Temporal coverage**: Confirmation that all included facilities have complete four-quarter data.

The descriptive table is presented in visually accessible format with deciles ordered from smallest (left) to largest (right) facility size, enabling visual inspection of trends in staffing composition across the facility size spectrum. Visual inspection of trends in descriptive statistics provides preliminary evidence about whether outcomes vary systematically with facility size, prior to formal statistical testing.

**Supplementary descriptive figures** may include:
- Histogram of daily resident census distribution (overall and within deciles)
- Box plots of RN-to-LPN ratio and contract CNA proportion, stratified by decile
- Histograms of outcome variables to assess distributional characteristics and skewness

### 5.2 Primary Regression Analysis 1: Hypothesis 1 (RN-to-LPN Ratio vs. Facility Size)

#### Model Specification and Functional Form

To test **Hypothesis 1** (that RN-to-LPN ratio increases monotonically with facility size), we fit a **restricted cubic spline (RCS) regression model** with the RN-to-LPN ratio as the dependent variable and facility median daily resident census as the primary predictor:

$$\text{RN-to-LPN Ratio}_{i} = \alpha + \sum_{k=1}^{K} \beta_k \phi_k(\text{Census}_{i}) + \sum_{j=1}^{J} \gamma_j \text{State}_{ij} + \sum_{q=1}^{Q} \delta_q \text{Quarter}_{iq} + \epsilon_i$$

where:
- $\alpha$ is the intercept
- $\phi_k(\text{Census}_{i})$ are the restricted cubic spline basis functions (K terms)
- $\beta_k$ are spline coefficients
- $\text{State}_{ij}$ are indicator variables for state (j = 1, ..., J; 51 states + DC)
- $\text{Quarter}_{iq}$ are indicator variables for study quarter (q = 1, ..., Q; 8 levels)
- $\gamma_j, \delta_q$ are coefficients for state and quarter effects
- $\epsilon_i$ is residual error, assumed independent and normally distributed with mean 0 and constant variance

#### Justification for Restricted Cubic Spline Regression

Restricted cubic spline regression is selected over simpler functional forms (linear, quadratic, polynomial) for several reasons. First, RCS relaxes the assumption of a linear relationship between facility size and staffing outcomes, allowing for flexible, data-driven functional forms that can capture non-linear associations without imposing a priori parametric assumptions. Second, RCS avoids extrapolation artifacts at the tails of the predictor distribution (where polynomial regression often produces spurious behavior). Third, RCS has a well-established methodological foundation in biostatistical literature (Harrell, 2015) and is widely used for flexible regression in observational studies.

The RCS model uses **three to four internal knots** positioned at quantiles of the daily census distribution. Knots are typically placed at the 25th, 50th, and 75th percentiles of the census distribution, resulting in a 4-degree-of-freedom model (4 basis terms: one for the linear baseline plus 3 spline basis functions). A four-degree-of-freedom model provides sufficient flexibility to capture non-linearity while maintaining parsimony and avoiding overfitting. Knot placement at quantiles ensures that knots are evenly distributed across the observed range of facility sizes, providing stable estimation across all regions of the predictor space.

#### Model Assumptions and Diagnostics

**Linearity and Functional Form**: The RCS regression relaxes linearity assumptions. However, we assess the adequacy of the RCS functional form by testing the null hypothesis that the relationship is linear (i.e., that spline terms contribute zero additional predictive power beyond the linear term). This is conducted via an F-test comparing the full RCS model to a reduced linear model: $H_0: \beta_2 = \beta_3 = \beta_4 = 0$ (where $\beta_2, \beta_3, \beta_4$ are the spline coefficients beyond the linear baseline). A significant F-test (p < 0.05) indicates that non-linearity is statistically important.

**Residual Normality**: We examine Q-Q plots (quantile-quantile plots) of standardized residuals against normal quantiles to assess whether residuals are approximately normally distributed. If substantial departures from normality are observed (e.g., heavy tails, skewness), we consider log-transformation of the outcome variable (RN-to-LPN ratio) to improve model fit and assumptions.

**Heteroscedasticity**: We conduct the Breusch-Pagan test to assess whether the variance of residuals is constant across levels of the predictor. The test statistic follows a chi-squared distribution; p < 0.05 indicates statistically significant heteroscedasticity. If heteroscedasticity is detected, we report **robust standard errors** (Huber-White sandwich estimators) clustered by state to account for state-level clustering in residual variance.

**Multicollinearity**: We calculate variance inflation factors (VIF) for all included covariates (state, quarter) to assess multicollinearity. A VIF < 5 is considered acceptable; VIF > 10 indicates problematic multicollinearity requiring variable removal or combination. State and quarter indicators typically have modest VIF values (< 3) due to near-orthogonal factor structure.

**Outlier Influence**: We examine standardized residuals and Cook's distance to identify facilities with extreme residuals or high influence on model coefficients. Facilities with |standardized residual| > 4 or Cook's distance > 4/n (where n is sample size) are flagged and excluded from the final model (in addition to the pre-analysis outlier screening described in Section 2.3). This two-stage outlier detection (pre-analysis and post-model) ensures robust inference.

#### Model Interpretation

Interpretation of RCS models focuses on the **fitted spline curve** rather than individual coefficient estimates. The fitted curve represents the predicted RN-to-LPN ratio as a function of facility census, adjusting for state and quarter effects. We present the spline curve graphically with 95% confidence bands (shaded region around the curve). 

**Test of Hypothesis 1**: Hypothesis 1 predicts that the spline curve is **monotonically increasing** (a positive trend in RN-to-LPN ratio with increasing facility size). To formally test this hypothesis, we examine the fitted spline curve and calculate the **derivative (slope)** of the curve at representative facility sizes (e.g., Decile 1, 5, and 10). If the derivative is positive across the observed range of facility sizes and the 95% confidence bands on the slope do not cross zero, we conclude that Hypothesis 1 is supported.

### 5.3 Primary Regression Analysis 2: Hypothesis 2 (Contract CNA Proportion vs. Facility Size)

#### Model Specification

To test **Hypothesis 2** (that contract CNA proportion follows an inverted-U pattern with facility size), we fit an analogous RCS regression model with contract CNA proportion as the dependent variable:

$$\text{Contract CNA Proportion}_{i} = \alpha + \sum_{k=1}^{K} \beta_k \phi_k(\text{Census}_{i}) + \sum_{j=1}^{J} \gamma_j \text{State}_{ij} + \sum_{q=1}^{Q} \delta_q \text{Quarter}_{iq} + \epsilon_i$$

The model structure is identical to the RN-to-LPN regression, but with contract CNA proportion as the outcome.

#### Handling Bounded Outcome Variables

Contract CNA proportion is bounded on [0, 1], potentially violating the normality assumption of ordinary least squares regression. We employ two analytical approaches:

**Primary Approach: OLS with Robust Standard Errors**: We fit an OLS model treating contract CNA proportion as a continuous unbounded variable, with robust standard errors to account for potential heteroscedasticity and departures from normality (Huber-White sandwich estimators). This approach is standard in epidemiology and biostatistics when continuous proportions are used as outcomes and is justified by the large sample size (n > 7,000) and Central Limit Theorem.

**Sensitivity Approach: Logit Transformation**: As a robustness check, we fit the model using a logit-transformed outcome: $\text{logit}(\text{proportion}) = \log\left(\frac{p}{1-p}\right)$. Facilities with observed contract CNA proportions of exactly 0 or 1 require special handling (addition of small constant or beta-binomial regression); results from logit-transformed models are compared to OLS results to assess robustness to functional form specification.

#### Tests for Non-Linearity and Inverted-U Pattern

**Test of Non-Linearity**: Conduct an F-test comparing the full RCS model to a reduced linear model: $H_0: \beta_2 = \beta_3 = \beta_4 = 0$. A significant F-test (p < 0.05) indicates that the relationship is non-linear.

**Test of Inverted-U (Concavity)**: After fitting the RCS model, we visually inspect the fitted spline curve. An inverted-U pattern is characterized by (a) initial increase in contract CNA proportion with increasing facility size, (b) a peak (maximum) at some intermediate facility size, and (c) decline in contract CNA proportion at larger facility sizes. To formalize this pattern, we:

1. **Identify the peak**: Calculate the facility census value at which the fitted spline curve is maximized (the x-coordinate of the peak).
2. **Test concavity**: Calculate the second derivative (curvature) of the spline curve. A negative second derivative indicates concavity (inverted-U shape). If the second derivative is significantly negative (confidence band on the second derivative does not cross zero), the inverted-U pattern is statistically supported.
3. **Characterize the peak**: Estimate the predicted contract CNA proportion at the peak and the corresponding facility census value. For example, if the peak occurs at a median daily census of 100 residents (in Decile 5–6), this supports the hypothesis that mid-sized facilities show maximum contract CNA reliance.

### 5.4 Secondary Analysis: Staffing Efficiency Index

We fit an analogous RCS regression model with the Staffing Efficiency Index as the dependent variable, using the same model specification and diagnostics as Analyses 1 and 2. This analysis serves as a sensitivity/validation check on the primary hypotheses by examining a composite measure of staffing skill composition.

### 5.5 Data Quality and Model Assumptions: Comprehensive Diagnostic Approach

Prior to fitting all regression models, we conduct comprehensive diagnostic assessments:

1. **Distribution Assessment**: Examine histograms, density plots, and Q-Q plots for all continuous variables (census, RN-to-LPN ratio, contract CNA proportion). Assess skewness and kurtosis; if skewness > |2|, consider transformation.

2. **Outlier Detection**: Perform univariate outlier screening using z-scores (|z| > 4) for all continuous variables. Generate summary statistics on the number and characteristics of flagged outliers.

3. **Missing Data Patterns**: Examine missing data frequency for all key variables. If any variable has > 5% missingness at the facility level, conduct sensitivity analyses comparing complete-case to imputed data.

4. **Collinearity Assessment**: Calculate VIF and correlation matrices for all included predictors. Assess whether state/quarter variables are collinear with each other (expected: they should be nearly orthogonal).

5. **Sample Size and Power**: Confirm that the final sample size (n ~ 7,100–9,100) provides adequate statistical power (90% or greater) to detect clinically meaningful effect sizes in regression analyses. For a two-sided test with α = 0.05 and n > 7,000, power is expected to exceed 90% for effect sizes as small as standardized differences of 0.05–0.10 standard deviations.

### 5.6 Stratified Analyses

#### Stratification by Ownership Type (Hypothesis 3)

If facility ownership data (for-profit vs. non-profit) are successfully linked to the analytic sample, we conduct stratified analyses repeating the primary RCS regressions separately within each ownership stratum. We formally test for ownership × census size interaction by fitting a model with an interaction term:

$$\text{Outcome}_{i} = \alpha + \beta_1 f(\text{Census}_{i}) + \beta_2 \text{Ownership}_{i} + \beta_3 f(\text{Census}_{i}) \times \text{Ownership}_{i} + \ldots$$

where $f(\text{Census}_{i})$ represents the RCS basis expansion and $\times$ denotes interaction. A significant interaction term (F-test; p < 0.05) indicates that the relationship between facility size and staffing outcomes differs between for-profit and non-profit facilities.

#### Stratification by Geographic Region (Census Division)

We repeat primary analyses separately within each of the nine U.S. Census divisions (Northeast, Middle Atlantic, East North Central, West North Central, South Atlantic, East South Central, West South Central, Mountain, Pacific). Stratified results are presented in a table with division-specific effect estimates (spline coefficients, or equivalently, predicted outcomes at representative facility sizes) and 95% confidence intervals.

To test for **geographic heterogeneity**, we fit a meta-analytic fixed-effects model:

$$\text{Effect}_{d} = \mu + \nu_d$$

where $\mu$ is the overall pooled effect across all divisions and $\nu_d$ is division-specific deviation. We conduct a **Q-statistic test** for heterogeneity: $Q = \sum_{d=1}^{D} w_d (\text{Effect}_{d} - \mu)^2$, which follows a chi-squared distribution with D–1 degrees of freedom. A significant Q-test (p < 0.05) indicates statistically significant geographic heterogeneity in facility size–staffing relationships.

### 5.7 Sensitivity Analyses

#### Sensitivity 1: Alternative Outlier Exclusion Thresholds

The primary analysis excludes facilities with |z-score| > 4.0 on any continuous variable. We conduct sensitivity analyses using alternative thresholds (|z| > 3.5, |z| > 3.0) and compare regression coefficients, confidence intervals, and p-values. If conclusions are robust across outlier thresholds, inference is strengthened.

#### Sensitivity 2: Minimum Facility Size Threshold Variation

The primary analysis includes facilities with median daily census ≥ 20. We refit all models after excluding facilities with median census < 30, < 40, or < 50 to assess robustness to the small-facility threshold. If conclusions are consistent across thresholds, robustness is confirmed.

#### Sensitivity 3: Temporal Aggregation Method

The primary analysis aggregates daily data across four quarters into facility-level means. As a sensitivity check, we fit regression models separately for each individual quarter (8 separate models) and examine whether facility size–outcome relationships are temporally consistent. Consistency across quarters strengthens inference about stable structural relationships.

#### Sensitivity 4: Alternative Outcome Specifications

For the RN-to-LPN ratio outcome, we fit models using **log-transformed ratio** ($\log(\text{RN-to-LPN})$) to normalize a potentially skewed distribution. Results using log-transformed outcomes are compared to primary untransformed models. If conclusions remain consistent, robustness is demonstrated.

#### Sensitivity 5: Functional Form Specification

We compare the primary RCS model to alternative functional forms:

1. **Linear Model**: RN-to-LPN Ratio ~ Census (simple linear regression)
2. **Quadratic Model**: RN-to-LPN Ratio ~ Census + Census² (polynomial regression)
3. **Spline with Different Knot Placements**: RCS models with different knot placements (e.g., 3 knots, 5 knots) or at fixed locations rather than quantiles

Comparisons are made using likelihood ratio tests (comparing nested models) and by examining visual consistency of fitted curves across models.

#### Sensitivity 6: State vs. No-State Adjustment

As an assessment of the contribution of state-level adjustment, we refit all models (a) with state indicators included (primary), and (b) with state indicators excluded (baseline adjustment only). If state inclusion substantially alters conclusions, we explore whether specific states drive results.

### 5.8 Supplementary Analysis: Data Envelopment Analysis (DEA)

If resources and analyst expertise permit, we conduct a non-parametric **Data Envelopment Analysis (DEA)** to estimate nursing home staffing efficiency frontiers. In DEA, facilities are categorized as either "efficient" (operating on the efficiency frontier) or "inefficient" (operating below the frontier) based on optimization of inputs to outputs.

**DEA Model Specification**:
- **Inputs**: Daily resident census (facility operating scale)
- **Outputs**: Total RN + LPN hours (quality output), total CNA hours (quantity output)

Each facility receives an efficiency score between 0 and 1, where 1 indicates frontier efficiency (optimal input-output combination) and < 1 indicates efficiency relative to frontier. Facilities are stratified into efficiency quintiles, and we examine the distribution of efficiency scores across facility size deciles. If larger facilities are overrepresented in higher efficiency quintiles, this supports the hypothesis that size enables efficiency.

---

## 6. Sample Characteristics and Data Quality Assessment

### 6.1 Pre-Analysis Data Validation

Prior to conducting primary analyses, we perform comprehensive data validation:

**Univariate Distributions**: Examine histograms, density plots, and summary statistics (mean, median, SD, min, max, quartiles) for all continuous variables. Assess skewness and kurtosis; values with |skewness| > 2 or kurtosis > 5 indicate potentially problematic distributions requiring transformation.

**Missing Data Inventory**: Tabulate the frequency and pattern of missing values. Expected: all key variables should have < 1% missingness after pre-analysis exclusion screening.

**Facility Count Verification**: Confirm that the final analytic sample contains the expected number of facilities (~7,100–9,100) and that exclusion counts match expected ranges from Table 1.

**Geographic and Temporal Coverage**: Verify that the final sample includes facilities from all 50 states and DC, and that all eight study quarters are represented in the data.

### 6.2 Post-Analysis Validation and Robustness Checks

After fitting primary regression models, we conduct the following validation checks:

**Direction of Estimates**: Confirm that regression coefficients and predicted curves are consistent with stated hypotheses. For Hypothesis 1, slopes should be positive (RN-to-LPN ratio increases with size). For Hypothesis 2, curves should exhibit inverted-U shape (increasing then decreasing with size).

**Magnitude of Effects**: Assess whether predicted effect sizes are clinically/practically meaningful. For example, if Hypothesis 1 predicts that RN-to-LPN ratio increases by 0.05 per 50-resident increase in facility size, this represents a 5–10% relative increase for typical facilities, a meaningful but moderate effect size.

**Sensitivity Stability**: Compare primary results to all sensitivity analyses (alternative outlier thresholds, functional forms, temporal windows). If results are stable across specifications, robustness is confirmed. If results vary substantially, investigate sources of variation.

**Comparison to Prior Literature**: Compare effect sizes and directional patterns to published studies on nursing home staffing composition and economies of scale. Consistency with prior work strengthens validity; substantial departures prompt investigation of methodological differences.

---

## 7. Analysis Software, Reproducibility, and Data Security

All data preparation and statistical analyses are conducted using **Python 3** (version 3.10 or later) with the following open-source libraries:

- **pandas**: Data manipulation and facility-level aggregation
- **numpy**: Numerical computations
- **scipy**: Statistical functions and distributions
- **statsmodels**: Restricted cubic spline regression models (via `patsy` formula interface and `statsmodels.formula.api`)
- **matplotlib** and **seaborn**: Data visualization (histograms, scatter plots, fitted curves with confidence bands)

**Alternative Software**: Some analyses may be conducted in **R** (version 4.0 or later) using the **rms** package (Harrell, 2015) for flexible regression, which provides superior tools for RCS modeling. If R is used, this will be noted in analysis scripts.

### 7.1 Data Security and Vault Execution

All analysis operates within the **pbj-analysis-vault Docker container**, a network-isolated computing environment designed to protect facility-level PBJ data. The container is configured with:

- **Network Isolation**: Executed with `--network none` to prevent any data transmission to external networks
- **Read-Only Data Mount**: PBJ data files mounted at `/data:ro` (read-only)
- **Study Output Mount**: Study directory mounted at `/study` (read-write) for outputs
- **Aggregation Mandate**: All Python scripts output only aggregated statistics (means, coefficients, confidence intervals, counts) to `/study/04-analysis/outputs/`, never raw facility-level data or individual records

All analysis scripts document:
- Input data sources (PBJ quarters, data paths)
- Python version and package versions
- Random seed (if applicable)
- Output file paths and naming conventions
- Exclusion counts and final sample size

### 7.2 Version Control and Reproducibility

All analysis scripts are version-controlled using Git. Scripts include:

- **Header comments**: Study title, data source, quarter, variable definitions, analysis date
- **Inline comments**: Explanations of statistical procedures, diagnostic checks, exclusion logic
- **Execution logs**: Print statements documenting sample sizes at each step, diagnostic test results, model fit statistics
- **Output documentation**: Filenames, locations, and variable definitions for generated tables and figures

Scripts are designed to be fully reproducible: re-running a script with the same input data and random seed produces identical numerical results.

---

## References

Harrell, F. E. (2015). *Regression modeling strategies: With applications to linear models, logistic and ordinal regression, and survival analysis* (2nd ed.). Springer.

Williamson, O. E. (1985). *The economic institutions of capitalism: Firms, markets, relational contracting*. Free Press.

Donabedian, A. (1988). The quality of care: How can it be assessed? *JAMA*, 260(12), 1743–1748.

---

**End of Methods Document**
