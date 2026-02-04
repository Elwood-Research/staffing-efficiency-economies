# Statistical Tests Reference: Detailed Formulas and Procedures

This document provides technical reference material for all statistical procedures described in the Methods section. It is designed for analysts implementing the analysis and peer reviewers verifying methodological rigor.

---

## 1. Restricted Cubic Spline (RCS) Regression

### 1.1 Overview

Restricted cubic spline regression is a flexible semi-parametric regression method that relaxes linearity assumptions while avoiding overfitting. The RCS basis consists of piecewise cubic polynomials joined at predefined knot locations, with restrictions ensuring continuity and smoothness at knots.

### 1.2 RCS Basis Functions

For a continuous predictor $X$ with $K$ knots at locations $\xi_1 < \xi_2 < \cdots < \xi_K$, the RCS basis functions are:

$$\phi_0(X) = 1 \quad \text{(Intercept)}$$

$$\phi_1(X) = X \quad \text{(Linear term)}$$

$$\phi_j(X) = (X - \xi_j)_+^3 - (X - \xi_K)_+^3 \cdot \frac{X - \xi_j}{X - \xi_K}, \quad j = 2, \ldots, K-1$$

where $(u)_+ = \max(0, u)$ is the positive part function.

The number of basis functions is $K$, resulting in a model with $K-1$ degrees of freedom (df) for the spline term plus 1 df for the intercept, for a total of $K$ parameters.

### 1.3 Knot Selection

**Quantile-Based Placement** (Recommended):
Knots are positioned at quantiles of the predictor distribution. For a 3-knot interior (recommended for this study):
- $\xi_1$ = 25th percentile of daily census
- $\xi_2$ = 50th percentile (median)
- $\xi_3$ = 75th percentile
- Boundary knots: $\xi_0 = \min(X)$ and $\xi_4 = \max(X)$

This results in 4 basis functions and 3 degrees of freedom for the spline term.

**Alternative: Fixed Knot Placement**:
For consistency across studies or to avoid data-driven knot placement, fixed knots may be specified based on clinical/practical thresholds (e.g., facilities < 50, 50–100, 100–150, > 150 residents). If used, fixed knots must be pre-specified in the Statistical Analysis Plan.

### 1.4 Model Fitting

The full model is:

$$Y_i = \alpha + \sum_{j=1}^{K} \beta_j \phi_j(X_i) + \sum_{k} \gamma_k Z_{ik} + \epsilon_i$$

where:
- $Y_i$ is the outcome (RN-to-LPN ratio or contract CNA proportion)
- $X_i$ is the exposure (daily resident census for facility $i$)
- $\phi_j$ are the RCS basis functions
- $Z_{ik}$ are covariates (state, quarter)
- $\epsilon_i \sim N(0, \sigma^2)$

Estimation uses ordinary least squares (OLS) with standard assumptions: linearity in parameters, independence of observations, homoscedasticity, and normality of residuals (latter assumption relaxed via robust standard errors if necessary).

### 1.5 Degrees of Freedom and Model Comparison

**Primary RCS Model** (with spline term):
- Degrees of freedom in spline term: 3 (for 3 interior knots)
- Additional df for covariates (state: 50 df; quarter: 7 df)
- **Total model df**: 1 (intercept) + 3 (spline) + 50 (state) + 7 (quarter) = 61

**Reduced Linear Model** (for comparison):
- Degrees of freedom: 1 (intercept) + 1 (linear census term) + 50 (state) + 7 (quarter) = 59
- **Difference in df**: 61 – 59 = 2

### 1.6 Hypothesis Tests for Non-Linearity

**Test of Linearity** (H₀: Relationship is linear, spline terms contribute nothing beyond linear term):

Conduct an **F-test** comparing the full RCS model to the reduced linear model:

$$F = \frac{\text{RSS}_{\text{reduced}} - \text{RSS}_{\text{full}}}{\text{df}_{\text{diff}} \cdot \text{MSE}_{\text{full}}}$$

where:
- $\text{RSS}_{\text{reduced}}$ = residual sum of squares for linear model
- $\text{RSS}_{\text{full}}$ = residual sum of squares for RCS model
- $\text{df}_{\text{diff}}$ = difference in residual degrees of freedom = 2
- $\text{MSE}_{\text{full}}$ = mean squared error of full model = $\text{RSS}_{\text{full}} / (n - 61)$

The test statistic $F$ follows an F-distribution with $\text{df}_{\text{diff}} = 2$ and $\text{df}_{\text{residual}} = n - 61$ degrees of freedom.

**Decision Rule**: 
- If p-value < 0.05, reject H₀; conclude that non-linearity is statistically significant.
- If p-value ≥ 0.05, fail to reject H₀; linear model is sufficient.

### 1.7 Spline Coefficient Interpretation

Individual spline coefficients ($\beta_1, \beta_2, \beta_3$) are not directly interpretable as slopes or effects. Instead, interpretation focuses on the **fitted curve** and its properties.

**Fitted Prediction**:
$$\hat{Y}_i = \hat{\alpha} + \sum_{j=1}^{3} \hat{\beta}_j \phi_j(X_i)$$

provides the predicted outcome for facility $i$ with census $X_i$, averaged over state and quarter effects.

### 1.8 Testing for Monotonicity (Hypothesis 1)

**Test of Positive Monotonicity** (H₀: RN-to-LPN ratio is non-increasing with census):

Calculate the derivative (slope) of the fitted spline curve at representative points (e.g., 25th, 50th, 75th percentiles of census):

$$\frac{d\hat{Y}}{dX} \bigg|_{X = x_j} = \sum_{k=1}^{3} \hat{\beta}_k \frac{d\phi_k}{dX}\bigg|_{X=x_j}$$

**Decision Rule**:
- If the derivative is positive (95% CI excludes zero) at all representative points, Hypothesis 1 is supported.
- If the derivative is negative at any point, monotonicity is violated.

**Visualization**: Present the fitted spline curve graphically with 95% confidence bands (shaded region). Visual inspection of a monotonically increasing curve with non-zero slope and confidence bands not crossing horizontal baseline confirms Hypothesis 1.

### 1.9 Testing for Inverted-U (Concavity; Hypothesis 2)

**Test of Concavity** (H₀: The relationship is convex or linear, not concave):

Calculate the second derivative (curvature) of the fitted spline:

$$\frac{d^2\hat{Y}}{dX^2} = \sum_{k=1}^{3} \hat{\beta}_k \frac{d^2\phi_k}{dX^2}$$

**Identification of Peak**:
The peak of the inverted-U occurs at the value of $X$ (facility census) where the first derivative equals zero:

$$\frac{d\hat{Y}}{dX}\bigg|_{X=X_{\text{peak}}} = 0$$

Solve numerically to identify $X_{\text{peak}}$.

**Concavity Test**:
If the second derivative is negative (95% CI excludes zero) across the observed range of $X$, the relationship is concave (inverted-U shaped), supporting Hypothesis 2.

**Decision Rule**:
- If curvature is significantly negative AND the peak occurs at a mid-range facility size (e.g., Decile 5–6), Hypothesis 2 is supported.
- If curvature is positive or near zero, the inverted-U hypothesis is rejected.

---

## 2. Heteroscedasticity Testing and Robust Standard Errors

### 2.1 Breusch-Pagan Test

The Breusch-Pagan test assesses whether residual variance is constant across the range of predicted values (homoscedasticity).

**Test Procedure**:

1. Fit the regression model and obtain residuals: $\hat{\epsilon}_i = Y_i - \hat{Y}_i$
2. Calculate squared residuals: $\hat{\epsilon}_i^2$
3. Regress squared residuals on the predictor (census) and covariates:
   $$\hat{\epsilon}_i^2 = \alpha_0 + \alpha_1 X_i + \sum_k \alpha_k Z_{ik} + v_i$$
4. Calculate test statistic: $BP = \text{SS}_{\text{regression}} / \text{MSE}_{\text{null}}^2$

where $\text{SS}_{\text{regression}}$ is the sum of squares from the auxiliary regression and $\text{MSE}_{\text{null}}$ is the mean squared error from the original model.

**Null Distribution**: The test statistic follows approximately a chi-squared distribution with degrees of freedom equal to the number of predictors in the auxiliary regression.

**Decision Rule**:
- If p-value < 0.05, reject H₀; heteroscedasticity is present. Use robust standard errors.
- If p-value ≥ 0.05, homoscedasticity assumption is supported.

### 2.2 Robust Standard Errors (Huber-White Sandwich Estimator)

If heteroscedasticity is detected, standard errors are corrected using the Huber-White sandwich estimator (HC1 variant):

$$\hat{\text{Var}}_{\text{HC1}}(\hat{\beta}) = (X'X)^{-1} \left( X'WX \right) (X'X)^{-1}$$

where:
- $X$ is the design matrix (predictors and covariates)
- $W$ is a diagonal matrix with $W_{ii} = \hat{\epsilon}_i^2$ (squared residuals)
- HC1 includes a finite-sample correction factor: $\frac{n}{n-p}$

**Clustering by State**: If substantial clustering of residuals within states is suspected, standard errors are clustered by state using the cluster-robust covariance matrix:

$$\hat{\text{Var}}_{\text{cluster}}(\hat{\beta}) = (X'X)^{-1} \sum_{s=1}^{S} X_s' \hat{\epsilon}_s \hat{\epsilon}_s' X_s (X'X)^{-1}$$

where $s$ indexes states and $\hat{\epsilon}_s$ are residuals for facilities in state $s$.

---

## 3. Multicollinearity Assessment

### 3.1 Variance Inflation Factor (VIF)

VIF measures the increase in variance of a regression coefficient due to correlation with other predictors.

**Calculation**:
$$\text{VIF}_k = \frac{1}{1 - R_k^2}$$

where $R_k^2$ is the R² from regressing predictor $k$ on all other predictors.

**Interpretation**:
- VIF = 1: No correlation with other predictors
- VIF < 5: Generally acceptable collinearity
- VIF > 10: Problematic multicollinearity; consider variable removal or combination

**Application**: Calculate VIF for all included covariates (state, quarter indicators). For categorical variables represented as multiple indicators, calculate VIF for the set of indicators as a group.

**Expected Results**: State and quarter indicators typically have modest VIF (< 3) due to near-orthogonal factor structure.

### 3.2 Correlation Matrix

Report the correlation matrix for continuous predictors (primary predictor: daily census; outcomes: RN-to-LPN ratio, contract CNA proportion). Correlations should be moderate (|r| < 0.7) to avoid multicollinearity problems.

---

## 4. Outlier Screening and Influence Diagnostics

### 4.1 Standardized Residuals and Z-Scores

For each observation, calculate the standardized residual:

$$z_i = \frac{\hat{\epsilon}_i}{\hat{\sigma} \sqrt{1 - h_{ii}}}$$

where:
- $\hat{\epsilon}_i$ is the residual
- $\hat{\sigma}$ is the residual standard error
- $h_{ii}$ is the leverage (hat matrix diagonal element)

**Outlier Flagging**: Observations with |$z_i$| > 3 or > 4 are flagged as potential outliers.

### 4.2 Cook's Distance

Cook's distance measures the influence of observation $i$ on model coefficients:

$$D_i = \frac{1}{p \cdot \text{MSE}} \sum_{j=1}^{n} (\hat{Y}_j - \hat{Y}_{j(-i)})^2$$

where $\hat{Y}_{j(-i)}$ is the predicted value for observation $j$ when observation $i$ is omitted from the data.

**Influential Observation Threshold**: Cook's distance > $\frac{4}{n}$ (or alternatively, > 1.0) indicates high influence on model coefficients.

**Decision**: Highly influential outliers (|$z_i$| > 4 and $D_i$ > $\frac{4}{n}$) are excluded from the final model.

---

## 5. Normality Testing

### 5.1 Shapiro-Wilk Test

The Shapiro-Wilk test assesses departure from normality.

**Test Statistic**:
$$W = \frac{\left( \sum_{i=1}^n a_i X_{(i)} \right)^2}{\sum_{i=1}^n (X_i - \bar{X})^2}$$

where $X_{(i)}$ are order statistics and $a_i$ are constants from a normal distribution.

**Null Distribution**: Test statistic follows approximately a normal distribution under the null hypothesis of normality.

**Decision Rule**:
- If p-value < 0.05, reject H₀; conclude departure from normality.
- If p-value ≥ 0.05, normality is not rejected.

**Note**: With large sample sizes (n > 7,000), minor deviations from normality can yield significant p-values despite minimal practical impact on inference due to robustness of OLS to non-normality (Central Limit Theorem).

### 5.2 Q-Q Plots

Quantile-quantile (Q-Q) plots visually assess normality by comparing empirical quantiles of residuals to theoretical normal quantiles. Residuals approximately normally distributed appear as points clustering along a 45-degree line. Systematic deviations (e.g., S-shaped pattern, heavy tails) indicate non-normality.

---

## 6. Confidence Intervals and Hypothesis Testing

### 6.1 Confidence Intervals for Regression Coefficients

For a coefficient estimate $\hat{\beta}_k$:

$$95\% \text{ CI} = \hat{\beta}_k \pm t_{\alpha/2, df} \cdot \text{SE}(\hat{\beta}_k)$$

where:
- $t_{\alpha/2, df}$ is the critical value from the t-distribution with degrees of freedom = $n - p$ (approximately 1.96 for large n)
- $\text{SE}(\hat{\beta}_k)$ is the standard error (from OLS or robust covariance matrix)

### 6.2 Confidence Bands for Fitted Spline Curves

For the fitted spline curve $\hat{Y}(X)$ at a given census value $X_0$:

$$95\% \text{ CB} = \hat{Y}(X_0) \pm 1.96 \cdot \text{SE}(\hat{Y}(X_0))$$

where:
$$\text{SE}(\hat{Y}(X_0))^2 = \phi(X_0)' \hat{\text{Var}}(\hat{\beta}) \phi(X_0)$$

and $\phi(X_0)$ is the vector of spline basis functions evaluated at $X_0$.

The confidence band represents the range of plausible fitted values accounting for sampling variability in coefficient estimates.

### 6.3 Hypothesis Tests on Coefficients

Two-sided t-test for individual coefficients:

$$t = \frac{\hat{\beta}_k}{\text{SE}(\hat{\beta}_k)} \sim t_{n-p}$$

**Decision Rule**: Reject H₀: $\beta_k = 0$ if |t| > $t_{\alpha/2, df}$ or equivalently, if the 95% CI for $\beta_k$ does not include zero.

---

## 7. Tests for Heterogeneous Effects (Stratified Analyses)

### 7.1 Interaction Testing

To test whether the relationship between facility size and staffing outcomes differs by ownership type:

**Full Model with Interaction**:
$$Y_i = \alpha + \beta_1 f(X_i) + \beta_2 O_i + \beta_3 f(X_i) \times O_i + \ldots$$

where:
- $f(X_i)$ represents the RCS basis expansion of census
- $O_i$ is the ownership indicator (0 = non-profit, 1 = for-profit)
- $\beta_3 f(X_i) \times O_i$ is the interaction term

**Test of Interaction Significance**:
Conduct an F-test comparing the full model (with interaction) to the reduced model (without interaction):

$$F = \frac{\text{RSS}_{\text{reduced}} - \text{RSS}_{\text{full}}}{\text{df}_{\text{diff}} \cdot \text{MSE}_{\text{full}}}$$

where $\text{df}_{\text{diff}}$ equals the number of interaction terms (approximately 2–3 for RCS interactions).

**Decision Rule**: If p-value < 0.05, conclude that the relationship differs by ownership; present stratified results separately for each ownership category.

### 7.2 Meta-Analysis for Geographic Heterogeneity

If analyses are stratified by census division, results are combined using fixed-effects meta-analysis:

**Pooled Effect**:
$$\hat{\mu} = \frac{\sum_d w_d \hat{\beta}_d}{\sum_d w_d}$$

where $w_d = 1/\text{SE}(\hat{\beta}_d)^2$ is the inverse-variance weight and $\hat{\beta}_d$ is the division-specific effect estimate.

**Heterogeneity Test** (Q-test):
$$Q = \sum_{d=1}^{D} w_d (\hat{\beta}_d - \hat{\mu})^2 \sim \chi^2_{D-1}$$

where D is the number of divisions.

**Decision Rule**: If Q p-value < 0.05, conclude that the relationship differs significantly across census divisions; present division-specific results separately.

---

## 8. Missing Data Procedures

### 8.1 Complete-Case Analysis

The primary approach: exclude any facility with missing values on key variables. This is appropriate when:
- Missingness is < 5% (expected in this study)
- Missingness is missing completely at random (MCAR)
- Sample remains sufficiently large (n > 7,000 after exclusion)

**Documentation**: Report the number of facilities excluded due to missingness and characteristics of excluded vs. included facilities.

### 8.2 Multiple Imputation (Sensitivity Analysis)

If missingness exceeds 5%, conduct multiple imputation:

1. Specify an imputation model (e.g., multivariate normal imputation or predictive mean matching)
2. Generate M = 10 complete datasets by imputing missing values
3. Fit regression models to each imputed dataset
4. Pool results using Rubin's rules:

$$\bar{\beta} = \frac{1}{M} \sum_{m=1}^{M} \hat{\beta}_m$$

$$\text{SE}(\bar{\beta})^2 = \frac{1}{M} \sum_{m=1}^{M} \text{SE}_m^2 + \frac{1}{M-1} \sum_{m=1}^{M} (\hat{\beta}_m - \bar{\beta})^2$$

**Comparison**: Compare results from complete-case and imputed-data analyses to assess sensitivity to missing data handling.

---

## 9. Power Calculation

### 9.1 Statistical Power for RCS Regression

For a given sample size n, effect size (quantified as the coefficient on the RCS term), and significance level α, we can calculate post-hoc statistical power.

**Approximate Formula** (for simple linear regression, adapted to RCS):

$$\text{Power} = P(F > F_{\alpha, df_1, df_2})$$

where $F_{\alpha, df_1, df_2}$ is the critical value of the F-distribution for non-centrality parameter:

$$\lambda = n \cdot f^2 = n \cdot \frac{R^2}{1 - R^2}$$

and $f$ is Cohen's effect size (relationship between effect size and R² depends on model specification).

**For this study** (n ~ 7,100, α = 0.05, expected effect size moderate):
- Power to detect standardized difference of 0.05–0.10 SD: > 90%
- Power to detect small effects (0.03 SD): approximately 70–80%

---

## 10. Supplementary: Data Envelopment Analysis (DEA) Reference

### 10.1 DEA Model Formulation

DEA solves the following linear programming problem for each facility:

$$\max_{\mu, \nu} \frac{\mu' Y_i}{\nu' X_i}$$

subject to:
$$\frac{\mu' Y_j}{\nu' X_j} \leq 1 \quad \text{for all } j$$
$$\mu, \nu \geq 0$$

where:
- $Y_i$ is the output vector for facility $i$ (RN + LPN hours, CNA hours)
- $X_i$ is the input vector (daily resident census)
- $\mu, \nu$ are vectors of weights

**Efficiency Score**: The optimal value of the objective function represents the efficiency score, ranging from 0 to 1.

### 10.2 DEA Results Presentation

Facilities are classified into efficiency quintiles (Q1: least efficient; Q5: most efficient). Cross-tabulation of efficiency quintile vs. facility size decile reveals whether larger facilities are more likely to be efficient.

---

**End of Statistical Tests Reference Document**
