# Research Hypotheses: Staffing Mix Efficiency and Economies of Scale

## PRIMARY HYPOTHESES

### Hypothesis 1 (H1): RN-to-LPN Ratio Increases with Facility Size

#### Statement
Larger nursing home facilities achieve higher Registered Nurse-to-Licensed Practical Nurse ratios than smaller facilities, reflecting economies of scale in recruiting and retaining higher-credentialed nursing staff.

#### Detailed Explanation
Transaction Cost Economics predicts that larger organizations can internalize functions (employee hiring and training) that smaller organizations externalize (contract labor or lower-credentialed staffing) due to fixed recruitment and training costs. Applied to nursing staffing:
- **Small facilities** face high per-unit costs of recruiting and training full-time Registered Nurses. The recruitment cost (~$3,000-5,000 per hire) is spread across fewer residents, raising the per-resident-day cost. Additionally, small facilities may lack the infrastructure (HR department, training program, clinical leadership) to support RN hiring. Consequently, small facilities hire proportionally fewer RNs and rely more on Licensed Practical Nurses.
- **Large facilities** achieve sufficient scale (200+ residents) to amortize recruitment and training costs across a large revenue base. They can employ dedicated HR and clinical leadership, establish competitive compensation packages, and develop career advancement pathways that attract RNs. Larger facilities also benefit from greater bargaining power with educational institutions for pipeline development (RN clinical placements, continuing education partnerships). Consequently, large facilities hire proportionally more RNs.

#### Expected Direction
**Positive monotonic relationship**: RN-to-LPN ratio (y-axis) increases as facility median daily resident census (x-axis) increases.

#### Theoretical Basis
1. **Transaction Cost Economics (Williamson, 1981, 1985)**: Firms choose organizational structure (make vs. buy) based on minimization of transaction costs. Internal hiring requires investment in HR infrastructure; external contracting requires search and negotiation costs. Scale shifts the trade-off: large firms internalize; small firms externalize.
2. **Economies of Scale in Healthcare (Skinner, 1938; Gaynor & Town, 2012)**: Healthcare organizations exhibit variable (labor) and fixed (management, HR, training) costs. Larger facilities spread fixed costs across more output units, reducing average cost per unit (resident).
3. **Labor Market Segmentation Theory (Doeringer & Piore, 1971)**: Primary labor market (skilled, permanent employment) is accessed primarily by large, stable employers. Small employers occupy secondary labor market (low-wage, unstable, contract employment).

#### Expected Effect Size (Conservative Estimate)
Based on preliminary examination of PBJ staffing distributions and published literature on nursing home economies of scale:

**Spline Regression Slope**: Moving from the 10th percentile to the 90th percentile of the facility census distribution (approximately 40 residents to 180 residents, a 3.5-fold increase):
- **Predicted change in RN-to-LPN ratio**: +0.15 to +0.25 (depending on baseline ratio at the 10th percentile)
- If baseline RN-to-LPN ratio at small facilities is ~0.5, large facilities are predicted to achieve ratios of 0.65-0.75, representing a 30-50% increase

**Interpretation**: A facility at the 90th census percentile would employ approximately 30-50% more RN hours relative to LPN hours compared to a facility at the 10th percentile.

#### Sample Size Implications
With final analytic sample of N = 7,000-9,000 facilities and four-quarter aggregation providing stable facility-level estimates, statistical power to detect a 0.15-0.25 change in ratio is very high (>0.95). The large sample size and use of restricted cubic splines (continuous covariate) provide substantial power even for small effect sizes.

#### Null vs. Alternative Framing
- **Null Hypothesis (H₀)**: RN-to-LPN ratio is **independent** of facility census size; the regression spline is flat (all coefficients = 0).
- **Alternative Hypothesis (H₁)**: RN-to-LPN ratio **depends on** facility census size in a monotonic manner; the regression spline slopes upward as census increases.

#### Falsifiability
This hypothesis is **falsifiable** if:
- Regression analysis reveals no significant relationship between census size and RN-to-LPN ratio (p > 0.05 for all spline coefficients).
- OR the relationship is reversed (negative slope), indicating smaller facilities hire proportionally more RNs—contradicting the transaction cost prediction.
- OR the relationship is non-monotonic (e.g., inverted-U) and is centered at small rather than large facilities.

#### Success Criterion for Hypothesis Support
- **Minimum threshold**: Restricted cubic spline regression shows a significant positive trend (p < 0.05 for overall spline test), with RN-to-LPN ratio increasing from smallest to largest decile (linear trend test p < 0.05).
- **Robust support**: Positive trend maintained in all sensitivity analyses (outlier exclusion, ownership stratification, geographic stratification).

---

### Hypothesis 2 (H2): Contract CNA Proportion Follows Inverted-U Pattern Across Facility Size

#### Statement
The proportion of Certified Nursing Assistant hours provided by contract (temporary, non-employee) staff follows a **non-monotonic (inverted-U) relationship** with facility size, peaking in mid-sized facilities (median daily census 50-150 residents) and declining at both smaller and larger sizes.

#### Detailed Explanation
This hypothesis emerges from Transaction Cost Economics and labor market dynamics specific to the CNA category:

1. **Small Facilities (Census <50)**:
   - Face the highest fixed costs of establishing HR recruitment infrastructure.
   - Hiring even a few full-time CNAs is expensive relative to total staffing budget.
   - **Strategic choice**: Use exclusively contract/per diem CNAs to maintain workforce flexibility; do not invest in permanent hiring (high contract reliance).

2. **Mid-Sized Facilities (Census 50-150)**:
   - Have sufficient scale to justify investing in permanent CNA hiring infrastructure.
   - Experience high resident census volatility (unpredictable occupancy rate fluctuations), requiring flexible staffing to manage 20-30% daily variation.
   - **Strategic choice**: Use **both** permanent and contract CNAs to balance efficiency (permanent lower-wage staff) with flexibility (temporary staff to absorb volatility). This dual-staffing model leads to **maximum contract reliance** as a proportion of total CNA hours.

3. **Large Facilities (Census >150)**:
   - Achieve sufficient scale to amortize permanent CNA hiring costs across a stable, predictable resident census.
   - Operating leverage: small daily census variations (±5-10% of total) can be absorbed by flexible scheduling of permanent staff rather than contract hiring.
   - **Strategic choice**: Hire predominantly permanent CNAs; use contract CNAs only for peak periods or short-term absences. This results in **lower contract reliance** despite larger absolute numbers of contract CNAs.

#### Expected Functional Form
Restricted cubic spline curve exhibits:
- **Ascending limb** (Deciles 1-4, census 20-80): Slight increase in contract CNA proportion as facility grows (fixed HR infrastructure becomes cost-effective)
- **Peak** (Deciles 5-6, census 80-150): Maximum contract CNA proportion (~35-45% of total CNA hours)
- **Descending limb** (Deciles 7-10, census 150-400+): Declining contract CNA proportion as facilities achieve full-scale economies

**Predicted Graph Shape**: Inverted-U (concave downward); not a V-shape or monotonic relationship.

#### Theoretical Basis
1. **Transaction Cost Economics (Williamson, 1981, 1985)**: Moving from external (contract) to internal (employee) hiring occurs as transaction-specific investments increase with firm size.
2. **Operations Research: Workforce Flexibility Models (Wright et al., 2006; Bard & Purnomo, 2007)**: Firms facing variable demand use a mix of permanent and temporary labor; the optimal proportion of temporary labor is a function of demand volatility and fixed hiring costs.
3. **Labor Market Dynamics in Healthcare (Aiken et al., 2002; Castle et al., 2009)**: Healthcare organizations strategically use contingent labor to manage seasonal demand fluctuations and handle absences without overloading permanent staff.

#### Expected Effect Size (Conservative Estimate)

**Spline Regression Coefficients (Quadratic Shape)**:
- **Small facilities (Decile 1, census ~30)**: Contract CNA proportion ≈ 25% (baseline)
- **Mid-sized facilities (Decile 5, census ~90)**: Contract CNA proportion ≈ 42% (peak; +17 percentage points above small facilities)
- **Large facilities (Decile 10, census ~280)**: Contract CNA proportion ≈ 30% (−12 percentage points below peak)

**Overall Range**: Contract CNA proportion varies from ~25% to ~42% across facility sizes, a range of 17 percentage points (68% relative increase from baseline).

#### Sample Size Implications
With N = 7,000-9,000 facilities, power to detect a quadratic relationship with 17-percentage-point peak deviation is extremely high (>0.99). The large sample provides sufficient statistical power even if the true quadratic effect is smaller.

#### Null vs. Alternative Framing
- **Null Hypothesis (H₀)**: Contract CNA proportion is **independent** of facility census size; the regression spline is flat (all coefficients = 0).
- **Alternative Hypothesis (H₂)**: Contract CNA proportion **depends** on facility census size in a **non-monotonic** (inverted-U) manner; the spline rises then falls (quadratic effect).

#### Falsifiability
This hypothesis is **falsifiable** if:
- Regression analysis reveals **no significant relationship** between census size and contract CNA proportion (p > 0.05 for all spline coefficients).
- OR the relationship is **monotonic** (strictly increasing or strictly decreasing) rather than inverted-U.
- OR the **peak is at extremely small or extremely large facilities** (outside the predicted 50-150 range), contradicting the transaction cost mechanism.
- OR the **amplitude of the inverted-U is very small** (<5 percentage points), indicating negligible practical effect.

#### Success Criterion for Hypothesis Support
- **Minimum threshold**: Restricted cubic spline regression shows a significant quadratic (non-linear) pattern (p < 0.05 for quadratic spline test). Peak of the curve is located in deciles 4-6 (census 70-130).
- **Strong support**: Peak amplitude is ≥10 percentage points (contract CNA proportion at peak exceeds baseline by ≥10 percentage points). Non-linear pattern is significant (comparison of linear vs. quadratic models via F-test, p < 0.05).
- **Robust support**: Inverted-U pattern maintained across ownership types, census divisions, and sensitivity analyses.

---

## SECONDARY HYPOTHESES

### Hypothesis 3 (H3): Ownership Type Moderates the Facility Size – Staffing Composition Relationship

#### Statement
The effect of facility size on RN-to-LPN ratio and contract CNA proportion differs between for-profit and non-profit nursing homes, with for-profit facilities showing stronger size-driven reductions in RN-to-LPN ratios and stronger increases in contract CNA reliance.

#### Theoretical Basis
**Agency Theory (Jensen & Meckling, 1976; Eisenhardt, 1989)**: 
- **For-profit facilities** prioritize shareholder value maximization, incentivizing aggressive cost minimization. Staffing decisions emphasize labor cost reduction; larger size enables better contract negotiation terms and labor substitution (RN→LPN, employee→contract).
- **Non-profit facilities** operate under mission-driven governance with stakeholder (resident, employee, community) interests potentially weighted alongside financial sustainability. Larger size provides more financial flexibility to sustain higher nursing staffing and employee ratios if consistent with mission.

#### Expected Effect
- **For-profit facilities**: Stronger positive association between size and RN-to-LPN ratio (slope β₁ > for non-profits); stronger inverted-U for contract CNA (peak amplitude > for non-profits).
- **Non-profit facilities**: Flatter slopes; smaller peak amplitude in contract CNA proportion.

#### Effect Size
- **Interaction coefficient (size × for-profit)**: +0.10 to +0.20 for RN-to-LPN ratio (expected), indicating for-profits gain more RN employment per unit increase in size.
- Alternatively, for-profits may show **negative** coefficients (lower RN-to-LPN ratio at given size), indicating they prioritize cost minimization even as size increases.

#### Falsifiability
This hypothesis is **falsifiable** if:
- Ownership type does not significantly moderate the size effect (p > 0.05 for interaction term).
- OR the interaction is in the opposite direction (non-profits show stronger size effects than for-profits).

#### Status
This is a **secondary hypothesis** dependent on successful linkage of PBJ data to external ownership variables from CMS. If ownership data cannot be linked, this hypothesis will not be tested.

---

### Hypothesis 4 (H4): Geographic Variation in Size Effects

#### Statement
The relationship between facility size and staffing composition varies significantly by U.S. Census Division, reflecting regional labor market conditions, state regulatory standards, and payment structures.

#### Theoretical Basis
**Institutional Theory (DiMaggio & Powell, 1983; Scott, 2014)**: Organizations conform to regional norms and state-level regulations. Regional variation in:
- Nursing labor supply and wage differentials
- State Medicaid reimbursement rates and payment policies
- State staffing regulations and enforcement
- Regional non-profit vs. for-profit facility concentration

leads to heterogeneous size-staffing relationships.

#### Expected Effect
- **Northeastern states** (higher nursing wages, stricter regulations): May show steeper RN-to-LPN gradient (larger facilities attract more RNs due to scale advantages in competing for scarce supply).
- **Southern and rural states** (lower wages, less stringent regulation): May show flatter RN-to-LPN gradient (smaller facilities more readily access lower-wage LPN labor).

#### Falsifiability
Hypothesis is **falsifiable** if:
- No significant heterogeneity detected across divisions (meta-analytic Q-test p > 0.05).
- OR predicted geographic patterns are not observed (e.g., Northeastern gradient is not steeper than Southern gradient).

#### Status
This is a **secondary hypothesis**; analysis will be conducted only if primary analyses support H1 and H2.

---

## HYPOTHESIS TESTING MATRIX

| Hypothesis | Primary Outcome | Predictor | Expected Shape | Sample Size Required | Power | Status |
|-----------|-----------------|-----------|---------------|--------------------|-------|--------|
| **H1** | RN-to-LPN Ratio | Census (continuous) | Positive monotonic | N ≥ 1,000 | >0.95 | **Primary** |
| **H2** | Contract CNA Proportion | Census (continuous) | Inverted-U (quadratic) | N ≥ 1,000 | >0.99 | **Primary** |
| **H3** | Both outcomes | Census × Ownership | Different slopes by ownership | N ≥ 500 per group | >0.85 | **Secondary** |
| **H4** | Both outcomes | Census × Division | Heterogeneous slopes | N ≥ 100 per division | >0.80 | **Secondary** |

---

## JOINT SUPPORT FOR TRANSACTION COST ECONOMICS FRAMEWORK

### Predicted Pattern if All Primary Hypotheses Supported

If both H1 and H2 are supported, the data would provide strong support for Transaction Cost Economics applied to nursing home staffing:

1. **RN Staffing (H1 supported)**: Larger facilities internalize RN employment (high RN-to-LPN ratio), consistent with TCE prediction that large firms invest in specialized, high-skill labor.

2. **CNA Staffing (H2 supported)**: Mid-sized facilities maintain maximum contract CNA reliance, consistent with TCE prediction that firms at intermediate scale experience highest demand uncertainty and highest marginal benefit from flexible staffing.

3. **Combined Interpretation**: Nursing homes exhibit a **two-tiered staffing strategy** that varies with size:
   - **Tier 1 (Credentialed Nursing)**: Internalized by large facilities; externalized (fewer RNs, more LPNs) by small facilities.
   - **Tier 2 (Support Services)**: Externalizes (contract CNAs) by small and large facilities; dual-source (employee + contract) by mid-sized facilities.

This pattern is **theoretically coherent** and would support a refined understanding of how transaction costs structure healthcare labor markets.

### Predicted Pattern if H1 Supported but H2 Not Supported

- **Interpretation**: Larger facilities prioritize RN staffing as a primary quality signal but do not strategically adjust CNA sourcing by size.
- **Implication**: Quality-of-care concerns drive RN hiring; workforce flexibility concerns do not drive contract CNA usage.
- **TCE Assessment**: Partial support; size effects exist for higher-credentialed staff but not for support staff.

### Predicted Pattern if H2 Supported but H1 Not Supported

- **Interpretation**: Larger facilities manage workforce flexibility through CNA sourcing but do not adjust RN-to-LPN ratios by size.
- **Implication**: Workforce flexibility and demand uncertainty drive staffing sourcing decisions; credentialing does not vary by size.
- **TCE Assessment**: Partial support; size effects exist for operational flexibility but not for skill composition.

### Predicted Pattern if Neither H1 nor H2 Supported

- **Interpretation**: Facility size does not predict staffing composition in expected directions.
- **Implication**: Factors other than transaction costs (e.g., state regulations, network effects, historical hiring patterns) drive staffing decisions.
- **TCE Assessment**: No support; alternative theoretical frameworks required.

---

## CONCLUSION AND RESEARCH SIGNIFICANCE

These four hypotheses (two primary, two secondary) are structured to test a coherent theoretical prediction from Transaction Cost Economics applied to nursing home staffing markets. The hypotheses are:

1. **Falsifiable**: Each specifies a direction and functional form for predicted relationships.
2. **Testable**: All required variables exist in PBJ data and can be reliably measured at the facility level.
3. **Theoretically grounded**: Predictions emerge from established economic theory applied to a novel healthcare context.
4. **Practically relevant**: Findings will inform management and policy decisions about optimal staffing strategies for facilities of different sizes.

**Expected Impact**: This study will contribute to understanding how organizational economics structure labor markets in long-term care and will provide evidence to support facility leaders, policymakers, and researchers in making staffing decisions aligned with both quality and efficiency objectives.

---

**End of Hypotheses Document**
