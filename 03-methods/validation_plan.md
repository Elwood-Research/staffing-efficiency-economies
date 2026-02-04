# Data Quality and Analysis Validation Plan

This document specifies the pre-analysis data validation checklist, post-analysis robustness verification procedures, and quality assurance sign-off criteria for the Staffing Mix Efficiency study.

---

## 1. Pre-Analysis Data Validation Checklist

### 1.1 Data Completeness and Integrity

**Checkpoint 1: File Presence and Integrity**
- [ ] All eight quarterly data files present in `/data/` directory:
  - CY2023Q1, Q2, Q3, Q4
  - CY2024Q1, Q2, Q3, Q4
- [ ] All eight documentation files present in `ProcessedData/Docs/`:
  - Data Dictionary CSV files: `YYYY-Q#_Data_Dictionary.csv`
  - Documentation Markdown files: `YYYY-Q#_Documentation.md`
- [ ] File sizes plausible (each quarterly data file > 100 MB, indicating ~1.2+ million daily records)
- [ ] No corrupted files (run file integrity check: `md5sum` or equivalent)

**Checkpoint 2: Data Structure Verification**
- [ ] Each quarterly file contains expected columns:
  - Facility identifiers: PROVNUM, PROVNAME, STATE, CITY, COUNTY_NAME, COUNTY_FIPS
  - Temporal: CY_Qtr, WorkDate
  - Census: MDScensus
  - Staffing: Hrs_RN, Hrs_RN_emp, Hrs_RN_ctr, Hrs_LPN, Hrs_LPN_emp, Hrs_LPN_ctr, Hrs_CNA, Hrs_CNA_emp, Hrs_CNA_ctr, (and others)
- [ ] No missing column headers
- [ ] Expected number of rows (≥ 1,000,000 per quarter)
- [ ] Data types correct (numeric for hours and census; string for identifiers)

**Checkpoint 3: Record-Level Data Integrity**
- [ ] For each quarterly file, calculate:
  - Number of unique facilities (expected: 9,000–11,000)
  - Number of operating days per facility (expected: 85–92 days, accounting for weekends)
  - Completeness of key variables (% non-missing for Hrs_RN, Hrs_LPN, Hrs_CNA, MDScensus)
    - Expected: > 99% non-missing for most facilities
- [ ] Identify facilities with > 10% missing data in any variable and flag for exclusion
- [ ] Verify no duplicate records (same PROVNUM + WorkDate + Quarter)

### 1.2 Variable Distribution Assessment

**Checkpoint 4: Univariate Distributions**

For each continuous variable, examine:

- **Daily Resident Census (MDScensus)**:
  - [ ] Mean, median, SD calculated
  - [ ] Range: minimum > 1, maximum < 1,500
  - [ ] Histogram: approximately normal, slight right skew acceptable
  - [ ] Skewness: |skewness| < 2 (acceptable)
  - [ ] Kurtosis: kurtosis < 5 (acceptable)
  - [ ] Outliers (|z| > 4): < 1% of observations

- **Registered Nurse Hours**:
  - [ ] Mean, median, SD calculated (expected mean: 1–5 hours/day per facility)
  - [ ] Range: minimum ≥ 0, maximum ≤ 50
  - [ ] Distribution: right-skewed (many facilities with low RN hours)
  - [ ] Skewness: acceptable if |skewness| < 3

- **Licensed Practical Nurse Hours**:
  - [ ] Mean, median, SD calculated (expected mean: 0.5–3 hours/day per facility)
  - [ ] Range: minimum ≥ 0, maximum ≤ 30
  - [ ] Distribution: right-skewed
  - [ ] Facilities with exactly 0 LPN hours: documented count (will require special handling in ratio calculation)

- **Certified Nursing Assistant Hours**:
  - [ ] Mean, median, SD calculated (expected mean: 2–10 hours/day per facility)
  - [ ] Range: minimum ≥ 0, maximum ≤ 100
  - [ ] Distribution: right-skewed

- **Contract CNA Hours**:
  - [ ] Mean, median, SD calculated
  - [ ] Range: minimum ≥ 0, maximum ≤ 80
  - [ ] Proportion of days with 0 contract hours (many facilities use no contract CNAs): documented

**Checkpoint 5: Categorical Variable Distributions**
- [ ] State: All 50 states + DC represented (51 levels); count facilities per state
  - [ ] No state has < 5% representation (expected: largest state ≤ 10%, smallest state ≥ 1%)
  - [ ] Facilities evenly distributed (e.g., no state missing)
- [ ] Quarter: All 8 quarters represented; equal representation expected
- [ ] Facility identifiers (PROVNUM, STATE, PROVNAME): No missing values (< 100 expected)

### 1.3 Facility-Level Aggregation Verification

**Checkpoint 6: Aggregation Process**
- [ ] Daily data successfully aggregated to facility level using formulas specified in Methods
- [ ] For each facility, calculate:
  - Mean daily census (across ~360 days)
  - Median daily census
  - Mean RN hours
  - Mean LPN hours
  - Mean CNA hours (total and contract)
  - RN-to-LPN ratio (verify: Mean RN Hours ÷ Mean LPN Hours; exclude facilities with 0 LPN hours)
  - Contract CNA proportion (verify: Mean Contract CNA ÷ Mean Total CNA)
  - Staffing efficiency index
- [ ] Number of resulting facility-level records: expected ~10,000–12,000 initially

**Checkpoint 7: Aggregated Variable Distributions**
- [ ] RN-to-LPN Ratio:
  - [ ] Range: 0.2–2.5 (majority within this range)
  - [ ] Mean, median, SD calculated
  - [ ] Skewness assessed (expected: moderate right skew)
  - [ ] Outliers (|z| > 4): count and document
- [ ] Contract CNA Proportion:
  - [ ] Range: 0–1 (bounded)
  - [ ] Mean, median, SD calculated
  - [ ] Bimodal or multimodal distribution expected (concentration at extremes)
  - [ ] Outliers (|z| > 4): count and document
- [ ] Staffing Efficiency Index:
  - [ ] Range: 0–1 (bounded)
  - [ ] Mean, median, SD calculated
  - [ ] Outliers (|z| > 4): count and document

### 1.4 Exclusion Screening and Sample Finalization

**Checkpoint 8: Inclusion/Exclusion Criteria Application**

Apply exclusion criteria sequentially and document counts:

- [ ] **Step 1**: Medicare certification status
  - [ ] Count of facilities failing this criterion: _____
  - [ ] Remaining facilities: _____

- [ ] **Step 2**: Operational continuity (all 4 quarters present)
  - [ ] Count of facilities with missing quarter(s): _____
  - [ ] Remaining facilities: _____

- [ ] **Step 3**: Minimum facility size (median census ≥ 20)
  - [ ] Count of facilities with median census < 20: _____
  - [ ] Remaining facilities: _____

- [ ] **Step 4**: Data completeness (< 10% missing in any quarter)
  - [ ] Count of facilities with > 10% missing: _____
  - [ ] Remaining facilities: _____

- [ ] **Step 5**: Valid identifiers
  - [ ] Count of facilities with missing PROVNUM, STATE, or PROVNAME: _____
  - [ ] Remaining facilities: _____

- [ ] **Step 6**: Statistical outliers (|z| > 4 on any continuous variable)
  - [ ] Variables screened: list all ____________
  - [ ] Count of facilities flagged as outliers: _____
  - [ ] Proportion of outliers: _____ % (expected: 1–4%)
  - [ ] Final analytic sample size: _____
  - [ ] **Verification**: Expected range 7,100–9,100 ✓ / ✗

**Checkpoint 9: Outlier Documentation**
- [ ] For each excluded outlier facility, document:
  - [ ] PROVNUM and facility name
  - [ ] Variable(s) on which it is extreme (z-score value)
  - [ ] Reason for outlier status (e.g., very large facility, extremely high RN reliance)
  - [ ] Whether exclusion aligns with prior knowledge of facility type

**Checkpoint 10: Final Sample Characteristics**
- [ ] Stratified descriptive table (Table 1) generated:
  - [ ] Facilities per decile: all deciles contain ~710–910 facilities ✓ / ✗
  - [ ] Census range per decile: monotonically increasing from D1 to D10 ✓ / ✗
  - [ ] Staffing variables summarized (RN, LPN, CNA hours; ratios)
  - [ ] Geographic distribution documented (states, census divisions)
  - [ ] Temporal coverage confirmed (all 8 quarters represented)

### 1.5 Missing Data Assessment

**Checkpoint 11: Missing Data Patterns**
- [ ] Count of facility-level records with missing aggregated variables: _____
- [ ] Proportion missing: _____ % (expected: < 1%)
- [ ] Variables with missingness: list ____________
  - [ ] RN-to-LPN ratio missing because LPN hours = 0: count = _____
  - [ ] Contract CNA proportion missing because Total CNA hours = 0: count = _____
- [ ] Decision on handling:
  - [ ] Exclude facilities with LPN = 0 from ratio analysis? ✓ / ✗
  - [ ] Exclude facilities with CNA = 0 from proportion analysis? ✓ / ✗
  - [ ] Document sample size for each analysis (may differ)

**Checkpoint 12: Missingness Assessment**
- [ ] If overall facility-level missingness > 5%:
  - [ ] Conduct missing data pattern analysis (is missingness MCAR, MAR, or MNAR?)
  - [ ] Plan multiple imputation sensitivity analysis (described in Methods)
- [ ] If overall missingness < 5%:
  - [ ] Proceed with complete-case primary analysis
  - [ ] Document that imputation sensitivity is optional

### 1.6 Data Quality Summary Report

**Checkpoint 13: Pre-Analysis QA Sign-Off**

Generate a comprehensive pre-analysis data quality report including:

- [ ] **Executive Summary**:
  - Total facilities in input data: _____
  - Final analytic sample size: _____
  - Proportion retained: _____ % (expected: 70–75%)

- [ ] **Exclusion Summary Table**:
  - Tabular display of exclusion counts and reasons (as in Checkpoint 8)

- [ ] **Final Sample Characteristics**:
  - Descriptive statistics for all key variables in the analytic sample
  - Geographic distribution (N and % by state and census division)
  - Temporal coverage (all 8 quarters confirmed)

- [ ] **Data Quality Indicators**:
  - Proportion of missing data: _____ %
  - Proportion of statistical outliers (|z| > 4): _____ %
  - Proportion of outliers excluded: _____ %

- [ ] **QA Sign-Off Checklist**: All 13 checkpoints completed? ✓ / ✗

**Signatory and Date**: _________________ (Analyst), _________________ (Date)

---

## 2. Post-Analysis Validation and Robustness Assessment

### 2.1 Model Fit and Assumption Checking

**Checkpoint 14: Regression Model Diagnostics**

For each primary regression model (H1 and H2):

**Linearity and Functional Form**:
- [ ] F-test of non-linearity (RCS vs. linear model) conducted
  - [ ] Test statistic: F = _____
  - [ ] p-value: p = _____
  - [ ] Conclusion: Non-linearity significant? Yes / No
  - [ ] If "No": Consider whether linear model is more parsimonious; document decision

**Residual Normality**:
- [ ] Q-Q plots examined (normal probability plots of standardized residuals)
  - [ ] Visual assessment: residuals approximately normal? Yes / No
- [ ] Shapiro-Wilk test conducted (if n < 5,000; otherwise approximate via visualization)
  - [ ] Test statistic: W = _____
  - [ ] p-value: p = _____
  - [ ] Interpretation: Evidence of non-normality? Yes / No
- [ ] If substantial non-normality detected: consider outcome transformation (log, logit)
  - [ ] Transformed outcome used in final model? Yes / No
  - [ ] Rationale documented: ____________

**Heteroscedasticity**:
- [ ] Breusch-Pagan test conducted
  - [ ] Test statistic: BP = _____
  - [ ] p-value: p = _____
  - [ ] Heteroscedasticity detected? Yes / No
- [ ] Residual plot (predicted values vs. residuals) examined
  - [ ] Visual pattern: heteroscedasticity present? Yes / No
- [ ] If heteroscedasticity detected: robust standard errors employed? Yes / No
  - [ ] Standard error type: ☐ Huber-White HC1 ☐ Cluster-robust (by state) ☐ Other: ____

**Multicollinearity**:
- [ ] Variance Inflation Factors (VIF) calculated for all included predictors
  - [ ] Maximum VIF: _____
  - [ ] All VIF < 5? Yes / No
  - [ ] Any problematic collinearity detected? Yes / No
- [ ] Correlation matrix examined (for continuous predictors)
  - [ ] Maximum |correlation|: _____
  - [ ] Problematic correlations (|r| > 0.8)? List: ____________

**Outlier Influence**:
- [ ] Standardized residuals examined (|residual| > 3 or > 4)
  - [ ] Count of extreme residuals (|z| > 4): _____
  - [ ] Proportion of observations: _____ %
- [ ] Cook's distance calculated and examined
  - [ ] Count of highly influential observations (D > 4/n): _____
  - [ ] These observations excluded from final model? Yes / No
  - [ ] Justification: ____________

**Checkpoint 15: Model Fit Quality**
- [ ] R² (coefficient of determination) calculated
  - [ ] R² for full RCS model: _____
  - [ ] R² for reduced linear model (if applicable): _____
  - [ ] Interpretation: Does model explain a meaningful proportion of outcome variance? Yes / No
- [ ] Residual standard error (RMSE) calculated
  - [ ] RMSE: _____ (units: same as outcome)
  - [ ] Interpretation: Average prediction error = _____ (substantial or minimal?)
- [ ] Model likelihood or information criteria (AIC, BIC) if applicable
  - [ ] Model with RCS spline preferred over linear? Yes / No

### 2.2 Direction and Magnitude of Effects

**Checkpoint 16: Hypothesis 1 Validation (RN-to-LPN Ratio Increases with Size)**

- [ ] Fitted spline curve examined graphically
  - [ ] Curve direction: monotonically increasing? Yes / No
  - [ ] If "No": document departure from expectation and investigate

- [ ] Slope (first derivative) of spline curve calculated
  - [ ] Sign of slope across facility size range: positive throughout? Yes / No
  - [ ] At 25th percentile of census: slope = _____ (positive? Yes / No)
  - [ ] At 50th percentile of census: slope = _____ (positive? Yes / No)
  - [ ] At 75th percentile of census: slope = _____ (positive? Yes / No)

- [ ] Confidence bands examined
  - [ ] At any point, confidence band crosses horizontal baseline (indicating uncertainty about sign)? Yes / No
  - [ ] Overall: 95% CI supports monotonic positive trend? Yes / No

- [ ] Predicted RN-to-LPN ratio at representative facility sizes
  - [ ] At Decile 1 (smallest facilities): predicted ratio = _____
  - [ ] At Decile 5 (median facilities): predicted ratio = _____
  - [ ] At Decile 10 (largest facilities): predicted ratio = _____
  - [ ] Trend: increasing from D1 to D10? Yes / No
  - [ ] Magnitude of increase: _____ ratio points (e.g., 0.1 to 0.3 = 0.2 point increase)

- [ ] **Hypothesis 1 Conclusion**:
  - [ ] Supported (monotonically increasing trend, statistically significant)? Yes / No
  - [ ] Partially supported (trend in expected direction, but not monotonic throughout)? Yes / No
  - [ ] Not supported (flat or decreasing trend)? Yes / No

**Checkpoint 17: Hypothesis 2 Validation (Contract CNA Proportion Follows Inverted-U)**

- [ ] Fitted spline curve examined graphically
  - [ ] Curve shape: inverted-U (concave)? Yes / No
  - [ ] If "No": describe actual shape (linear, U-shaped, other): ____________

- [ ] Non-linearity F-test (RCS vs. linear)
  - [ ] Test statistic: F = _____
  - [ ] p-value: p = _____
  - [ ] Non-linearity significant? Yes / No
  - [ ] If "No": consider whether quadratic or linear model is appropriate

- [ ] Peak of inverted-U identified
  - [ ] Census value at peak: _____ residents/day
  - [ ] Corresponding census decile: Decile _____
  - [ ] Predicted contract CNA proportion at peak: _____
  - [ ] Peak plausibly occurs at mid-sized facilities (Decile 4–6)? Yes / No

- [ ] Concavity of curve
  - [ ] Second derivative (curvature) negative throughout observed range? Yes / No
  - [ ] Confidence bands on second derivative exclude zero? Yes / No
  - [ ] Curvature statistically significant? Yes / No

- [ ] Predicted contract CNA proportion at representative facility sizes
  - [ ] At Decile 1 (smallest): predicted proportion = _____
  - [ ] At Decile 5 (median): predicted proportion = _____
  - [ ] At Decile 10 (largest): predicted proportion = _____
  - [ ] Pattern: inverted-U with peak in middle? Yes / No

- [ ] **Hypothesis 2 Conclusion**:
  - [ ] Supported (inverted-U shape, peak at mid-sized facilities, significant curvature)? Yes / No
  - [ ] Partially supported (inverted-U shape, but peak location differs from expectation)? Yes / No
  - [ ] Not supported (linear or U-shaped relationship)? Yes / No

### 2.3 Sensitivity Analyses

**Checkpoint 18: Outlier Threshold Sensitivity**

Refit all primary models using alternative outlier exclusion thresholds:

- [ ] **Primary (|z| > 4)**: Sample size = _____, Key effect sizes documented (Checkpoint 16–17)

- [ ] **Sensitivity 1 (|z| > 3.5)**:
  - [ ] Sample size: _____ (n excluded: _____)
  - [ ] RN-to-LPN regression: slope/trend direction consistent? Yes / No
  - [ ] Contract CNA regression: inverted-U pattern consistent? Yes / No
  - [ ] Effect size change: < 10% / 10–20% / > 20%?
  - [ ] Conclusions robust to threshold change? Yes / No

- [ ] **Sensitivity 2 (|z| > 3.0)**:
  - [ ] Sample size: _____ (n excluded: _____)
  - [ ] RN-to-LPN regression: slope/trend direction consistent? Yes / No
  - [ ] Contract CNA regression: inverted-U pattern consistent? Yes / No
  - [ ] Effect size change: < 10% / 10–20% / > 20%?
  - [ ] Conclusions robust to threshold change? Yes / No

**Checkpoint 19: Minimum Facility Size Threshold Sensitivity**

Refit all models excluding small facilities:

- [ ] **Primary (median census ≥ 20)**:
  - [ ] Sample size: _____
  - [ ] Key effect sizes documented

- [ ] **Sensitivity 1 (median census ≥ 30)**:
  - [ ] Sample size: _____ (n excluded: _____)
  - [ ] Effect size change: < 10% / 10–20% / > 20%?
  - [ ] Conclusions consistent? Yes / No

- [ ] **Sensitivity 2 (median census ≥ 40)**:
  - [ ] Sample size: _____ (n excluded: _____)
  - [ ] Effect size change: < 10% / 10–20% / > 20%?
  - [ ] Conclusions consistent? Yes / No

- [ ] **Sensitivity 3 (median census ≥ 50)**:
  - [ ] Sample size: _____ (n excluded: _____)
  - [ ] Effect size change: < 10% / 10–20% / > 20%?
  - [ ] Conclusions consistent? Yes / No

**Checkpoint 20: Temporal Aggregation Sensitivity**

Fit regression models separately for each individual quarter:

- [ ] **Primary (4-quarter aggregation)**:
  - [ ] Key effect sizes documented

- [ ] **Sensitivity (8 separate quarterly models)**:
  - [ ] CY2023Q1: slope/trend direction consistent with primary? Yes / No
  - [ ] CY2023Q2: slope/trend direction consistent with primary? Yes / No
  - [ ] CY2023Q3: slope/trend direction consistent with primary? Yes / No
  - [ ] CY2023Q4: slope/trend direction consistent with primary? Yes / No
  - [ ] CY2024Q1: slope/trend direction consistent with primary? Yes / No
  - [ ] CY2024Q2: slope/trend direction consistent with primary? Yes / No
  - [ ] CY2024Q3: slope/trend direction consistent with primary? Yes / No
  - [ ] CY2024Q4: slope/trend direction consistent with primary? Yes / No
  - [ ] Overall: temporal consistency of effects? Yes / No
  - [ ] Any seasonal patterns detected (e.g., Q4 effects differ)? Yes / No

**Checkpoint 21: Functional Form Sensitivity**

Compare RCS regression to alternative functional forms:

- [ ] **Primary (RCS with 3 interior knots, 4 df for spline)**:
  - [ ] Model fit (R², RMSE): _____
  - [ ] Effect sizes documented

- [ ] **Sensitivity 1 (Linear model: Census only, no spline)**:
  - [ ] R²: _____ (vs. primary: _____)
  - [ ] RMSE: _____ (vs. primary: _____)
  - [ ] Slope sign and magnitude: _____
  - [ ] Compared to RCS via F-test (linearity test result): p = _____
  - [ ] Linear model adequate? Yes / No

- [ ] **Sensitivity 2 (Quadratic model: Census + Census²)**:
  - [ ] R²: _____ (vs. primary: _____)
  - [ ] RMSE: _____ (vs. primary: _____)
  - [ ] Polynomial terms sign/magnitude: _____
  - [ ] Quadratic provides meaningful improvement over linear? Yes / No

- [ ] **Sensitivity 3 (RCS with different knot placement)**:
  - [ ] Number of interior knots: 2 / 4 / 5?
  - [ ] Model fit: R² = _____, RMSE = _____
  - [ ] Effect sizes vs. primary: consistent? Yes / No

- [ ] **Overall conclusion on functional form**:
  - [ ] RCS model is preferred / linear model is adequate / alternative form better?
  - [ ] Justification: ____________

**Checkpoint 22: Outcome Transformation Sensitivity**

For outcomes with bounded or skewed distributions:

- [ ] **Contract CNA Proportion (Primary: untransformed OLS)**:
  - [ ] Effect sizes documented

- [ ] **Sensitivity (Logit-transformed outcome)**:
  - [ ] Facilities with proportion = 0 or 1: handled via ______ (small constant / beta-binomial / exclusion)
  - [ ] Model fit and effect sizes calculated
  - [ ] Inverted-U pattern consistent with primary? Yes / No
  - [ ] Conclusions robust to transformation? Yes / No

- [ ] **RN-to-LPN Ratio (Primary: untransformed OLS)**:
  - [ ] Effect sizes documented

- [ ] **Sensitivity (Log-transformed outcome)**:
  - [ ] Model fit and effect sizes calculated
  - [ ] Monotonic increasing trend consistent with primary? Yes / No
  - [ ] Conclusions robust to transformation? Yes / No

### 2.4 Geographic and Ownership Heterogeneity

**Checkpoint 23: Stratified Analysis by Census Division**

If conducted, report results for each of 9 census divisions:

- [ ] Division-specific slope estimates (RN-to-LPN model) or peak locations (contract CNA model) documented
- [ ] Visual forest plot or table presenting all division effects
- [ ] Heterogeneity test (Q-statistic):
  - [ ] Q-statistic: _____
  - [ ] p-value: p = _____
  - [ ] Significant heterogeneity across divisions? Yes / No
- [ ] If heterogeneity present: investigate sources (e.g., state regulations, labor market)
  - [ ] Division with largest effect size: ____________
  - [ ] Division with smallest effect size: ____________
  - [ ] Plausible explanation: ____________

**Checkpoint 24: Stratified Analysis by Ownership (If Data Available)**

If ownership data successfully linked:

- [ ] **For-profit facilities** (n = _____):
  - [ ] H1 (RN-to-LPN increases with size): supported? Yes / No
  - [ ] H2 (Contract CNA inverted-U): supported? Yes / No
  - [ ] Effect sizes: _____

- [ ] **Non-profit facilities** (n = _____):
  - [ ] H1 (RN-to-LPN increases with size): supported? Yes / No
  - [ ] H2 (Contract CNA inverted-U): supported? Yes / No
  - [ ] Effect sizes: _____

- [ ] **Ownership × size interaction test**:
  - [ ] Interaction F-test: F = _____, p = _____
  - [ ] Significant interaction? Yes / No
  - [ ] Conclusions: Effects differ by ownership? Yes / No

### 2.5 Comparison to Prior Literature

**Checkpoint 25: Face Validity Assessment**

- [ ] Published effect sizes from similar studies identified and summarized: ____________
- [ ] Effect sizes from this analysis consistent with prior work? Yes / No / Partially
- [ ] If inconsistent, plausible explanations documented:
  - [ ] Different populations (e.g., nursing homes vs. other settings)
  - [ ] Different time periods (e.g., pandemic era vs. post-pandemic)
  - [ ] Different outcome definitions (e.g., RN-to-LPN ratio vs. RN staffing hours only)
  - [ ] Other: ____________

- [ ] **Face validity conclusion**: Results appear plausible and aligned with theory? Yes / No

### 2.6 Magnitude and Clinical Significance

**Checkpoint 26: Effect Size Interpretation**

- [ ] **RN-to-LPN Ratio (H1)**:
  - [ ] Magnitude of increase from smallest to largest decile: _____ ratio points
  - [ ] Relative percent change: _____ %
  - [ ] Interpretation: Is this change meaningful from a staffing composition perspective? Yes / No
  - [ ] Rationale: ____________

- [ ] **Contract CNA Proportion (H2)**:
  - [ ] Magnitude of peak vs. endpoints: _____ proportion points
  - [ ] Relative percent change: _____ %
  - [ ] Peak census value: _____ residents
  - [ ] Interpretation: Is the inverted-U pattern clinically meaningful? Yes / No
  - [ ] Rationale: ____________

---

## 3. Quality Assurance Sign-Off and Final Approval

### 3.1 QA Checklist Summary

All post-analysis validation checkpoints completed? ✓ / ✗

- [ ] Checkpoint 14: Model diagnostics ✓ / ✗
- [ ] Checkpoint 15: Model fit quality ✓ / ✗
- [ ] Checkpoint 16: Hypothesis 1 validation ✓ / ✗
- [ ] Checkpoint 17: Hypothesis 2 validation ✓ / ✗
- [ ] Checkpoint 18: Outlier threshold sensitivity ✓ / ✗
- [ ] Checkpoint 19: Facility size threshold sensitivity ✓ / ✗
- [ ] Checkpoint 20: Temporal aggregation sensitivity ✓ / ✗
- [ ] Checkpoint 21: Functional form sensitivity ✓ / ✗
- [ ] Checkpoint 22: Outcome transformation sensitivity ✓ / ✗
- [ ] Checkpoint 23: Geographic heterogeneity ✓ / ✗
- [ ] Checkpoint 24: Ownership heterogeneity (if applicable) ✓ / ✗
- [ ] Checkpoint 25: Comparison to prior literature ✓ / ✗
- [ ] Checkpoint 26: Effect size interpretation ✓ / ✗

### 3.2 Analyst Certification

**Analyst Certification Statement**:

I certify that:

- [ ] All pre-analysis data validation checkpoints (1–13) have been completed and documented
- [ ] All post-analysis validation checkpoints (14–26) have been completed and documented
- [ ] Data quality standards meet or exceed study requirements
- [ ] Regression model assumptions are satisfied or appropriate adjustments have been made
- [ ] Sensitivity analyses demonstrate robustness of conclusions to alternative specifications
- [ ] Results align with stated hypotheses and prior literature, or departures are explained
- [ ] All analysis scripts are version-controlled and reproducible
- [ ] Data security protocols (vault execution, no raw data export) have been maintained

**Analyst Name**: _________________ **Date**: _________________ **Signature**: _________________

### 3.3 Senior Researcher Review and Approval

**Senior Researcher Review Statement**:

I have reviewed the analysis and validation documentation and certify that:

- [ ] Data quality is sufficient for publication-quality research
- [ ] Statistical methods are appropriate and correctly implemented
- [ ] Assumptions are satisfied and diagnostic checks are thorough
- [ ] Sensitivity analyses support robustness of conclusions
- [ ] Results are interpreted accurately and limitations acknowledged
- [ ] Manuscript is ready for submission to peer-reviewed journal

**Senior Reviewer Name**: _________________ **Date**: _________________ **Signature**: _________________

### 3.4 Quality Gate Approval

**Study Phase**: Phase 3 – Methods Documentation and Preliminary Analysis
**Status**: ☐ APPROVED (Proceed to Phase 4 – Full Analysis) / ☐ CONDITIONAL (Address items below) / ☐ NOT APPROVED (Return to Methods revision)

**Approval Notes** (if conditional or not approved):
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________

**Quality Gate Authority**: _________________ **Date**: _________________ **Signature**: _________________

---

**End of Validation Plan Document**
