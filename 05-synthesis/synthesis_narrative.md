# Phase 5 Synthesis: Narrative Integration of Literature and Empirical Findings

**Study**: Staffing Mix Efficiency and Economies of Scale in Nursing Homes  
**Sample**: 14,209 U.S. nursing homes (CY2023Q1-CY2024Q4)  
**Date**: February 4, 2026

---

## 1. Study Overview & Theoretical Expectations

This research examines whether facility size influences nursing home staffing efficiency through two mechanisms: (1) the mix of registered nurses (RNs) versus licensed practical nurses (LPNs), operationalized as the RN-to-LPN ratio, and (2) reliance on contract-based certified nursing assistants (CNAs). The investigation was grounded in Transaction Cost Economics (TCE), which predicts that larger facilities achieve operational efficiencies through economies of scale. Under TCE, fixed costs of recruitment, training, and administration distribute across a larger resident population, enabling larger facilities to shift toward higher-skill staffing (i.e., proportionally more RNs) or reduce reliance on costly contract labor.

The Donabedian Structure-Process-Outcome model provided a complementary framework, positioning facility size as a structural characteristic that shapes care delivery processes. According to this model, larger facilities possess superior resources enabling more efficient processes—including higher-quality staffing composition—that ultimately improve resident outcomes. Agency Theory suggested that ownership type (particularly for-profit status) would interact with facility size to influence staffing choices, with financial incentives potentially overriding efficiency considerations. Together, these frameworks created compelling theoretical expectations: larger nursing homes should employ proportionally more RNs relative to LPNs, and mid-sized facilities should experience peak reliance on contract CNAs due to their unique position—too large to operate with purely flexible staffing arrangements, yet too small to leverage economies of scale of the largest systems.

The literature provided substantial evidence supporting these theoretical predictions. Christensen (2003) documented economies of scale across the nursing home industry, Farsi and colleagues (2008) confirmed scale advantages in Swiss settings, and Ghiasi and colleagues (2023) documented the financial costs of contract labor, suggesting facilities would minimize such use if they could. Research demonstrating that payment reforms shift staffing composition (Huang et al., 2025) further suggested that facilities respond rationally to incentive structures, adjusting skill mix in response to financial and regulatory pressures. The anticipated research gap was that no prior study had directly tested whether facility size produces the predicted efficiency improvements in staffing composition using comprehensive national data.

---

## 2. What the Data Actually Show: Contradictions and Surprises

### Finding 1: Larger Facilities Have LOWER RN-to-LPN Ratios (Contradicts H1)

The empirical analysis revealed a finding that directly contradicts the theoretical hypothesis. Rather than larger facilities maintaining higher RN-to-LPN ratios, the data showed a statistically significant negative relationship: each additional 10 residents in average daily census was associated with a 0.07-unit decrease in the RN-to-LPN ratio (coefficient = -0.00697, 95% CI: -0.0122 to -0.0017, p=0.005). This relationship was robust across all sensitivity analyses, remaining significant whether outliers were defined by |z| > 4, |z| > 3.5, or |z| > 3.0 thresholds. The association persisted even when minimum facility size thresholds were varied from 20 to 50 residents per day.

To contextualize this finding: the median nursing home in the sample (75 residents/day) maintained an RN-to-LPN ratio of 0.46, meaning for every registered nurse, facilities employed approximately 2.2 licensed practical nurses. Moving from the 20th percentile facility size (30 residents/day) to the 80th percentile facility size (130 residents/day) resulted in approximately a 0.5-unit decrease in this ratio—a substantial shift in staffing composition. The practical implication is profound: larger nursing homes employ proportionally MORE licensed practical nurses and fewer registered nurses than smaller facilities, precisely the opposite of the efficiency hypothesis.

This finding raises several critical questions. First, is it possible that larger facilities operate with lower RN-to-LPN ratios *by choice* rather than constraint? Perhaps they have developed care models that effectively distribute RN supervision across larger populations of LPNs. Second, is the relationship driven by selection effects—do certain types of facilities (e.g., for-profit chains, facilities in high-CNA-availability regions) both grow larger AND employ more LPNs? Third, might regulatory requirements actually constrain RN ratios while permitting variable LPN use, creating an upper bound on RN staffing regardless of size? The data alone cannot definitively answer these questions, but they complicate the narrative of efficiency advantages for larger facilities.

### Finding 2: No Inverted-U Pattern for Contract CNA Reliance (H2 Not Supported)

The second hypothesis—that contract CNA reliance peaks in mid-sized facilities due to their unique structural position—received no empirical support. Instead, the relationship was flat across the entire facility size distribution. Both the linear term (coefficient = -0.000050, p=0.393) and quadratic term (coefficient = 0.0000003, p=0.286) in the facility size models were statistically non-significant. The mean contract CNA proportion across all facilities was 5.9% (SD = 8.0%), with a median of 1.9%, indicating that the vast majority of nursing homes rely primarily on direct-hire CNAs.

Notably, the inverted-U pattern hypothesis was theoretically plausible: mid-sized facilities should face precisely the constraints that would drive contract labor reliance (inflexible full-time staffing requirements, insufficient census to amortize recruitment costs, yet too large to maintain purely flexible models). The absence of this pattern suggests either that (a) these theoretical constraints are less binding than expected, (b) other factors override size-related mechanisms, or (c) mid-sized facilities have adopted different strategies (workforce retention, modified scheduling, administrative consolidation) to avoid contract labor reliance. Geographic factors dominate: state fixed effects explained 12% of contract CNA variation compared to <1% for facility size effects.

### Finding 3: Staffing Scales Proportionally with Census, Composition Does Not

A crucial pattern emerged across multiple staffing categories. Census showed strong correlations with direct-hire CNA hours (r = 0.887), LPN hours (r = 0.811), and RN hours (r = 0.539). This indicates that larger facilities maintain proportionally more staff across all categories in line with their resident populations. However, the RN-to-LPN ratio showed negligible correlation with census (r = -0.030), suggesting that while larger facilities employ more total staff, they do not systematically recompose the nursing workforce. Stated differently: larger facilities scale up their total staffing proportionally with residents but maintain similar (or slightly lower) skill-mix ratios. This is consistent with a model of *uniform staffing processes* rather than *efficiency-driven differentiation* by facility size.

This pattern has important implications. It suggests that nursing home staffing decisions may reflect standardized care models applied uniformly across facilities rather than context-specific optimization. If larger facilities achieved true efficiency advantages, we would expect to see (a) lower total staffing hours per resident day, (b) higher skill mix (RN-to-LPN ratio), or (c) lower contract labor reliance. Instead, we observe uniform scaling with modest (but insignificant) shifts in composition. The evidence points toward staffing as a regulated compliance issue rather than an efficiency frontier—facilities meet regulatory minimums and apply consistent models across their operations.

---

## 3. Reconciling Theory with Evidence: Why Predictions Failed

### Transaction Cost Economics and the Limits of Scale

Transaction Cost Economics provides powerful insights into organizational structure under conditions of incomplete information, asset specificity, and bounded rationality. TCE suggests that larger organizations economize on per-unit transaction costs through specialization, standardization, and amortization of fixed investments. In nursing homes, this logic predicts that larger facilities would achieve superior recruiting capacity for registered nurses, amortize training costs across more residents, and standardize care processes to leverage higher-credentialed staff.

The empirical finding contradicts these predictions. Several mechanisms may explain this divergence:

**First, the regulatory ceiling hypothesis**: CMS minimum staffing rules establish *minimal* requirements but may also create implicit ceilings on RN staffing through state regulations and Medicare reimbursement rates. If regulatory bodies set baseline RN-to-LPN ratios (e.g., through state licensing requirements or Medicare payment structures), then larger facilities have no efficiency incentive to exceed these ceilings. TCE would then predict convergence toward regulatory minimums rather than competitive differentiation through higher staffing ratios. This interpretation is supported by the relatively tight distribution of RN-to-LPN ratios (median = 0.46, IQR = 0.28-0.79) despite wide facility size variation.

**Second, the labor market constraint hypothesis**: The persistent nursing shortage in long-term care settings may constrain RN availability regardless of facility size or financial incentives. If RN supply is inelastic—driven by regional labor market conditions, educational pipeline constraints, and competing healthcare demands—then larger facilities cannot simply purchase their way to higher RN ratios through superior compensation or working conditions. Instead, they substitute LPNs and CNAs, technologies, and care models to compensate for RN shortages. This interpretation aligns with research documenting acute RN workforce challenges during the COVID-19 pandemic (Brazier et al., 2023) and the geographic variation in staffing patterns (Kang et al., 2024).

**Third, the cost minimization hypothesis**: While TCE predicts efficiency-seeking behavior, it does not assume all efficiencies produce higher-skill staffing. If cost minimization dominates the organizational objective function, larger facilities with greater financial resources and administrative sophistication might *choose* lower RN-to-LPN ratios as a deliberate strategy to minimize labor costs while maintaining quality thresholds. This would be rational economic behavior—TCE does not require that organizations seek quality maximization, only that they economize on transaction costs. Ghiasi and colleagues' (2023) finding that contract staffing reduces operating margins is illuminating: if contract labor is so costly, why do facilities use it? The answer must be that other considerations (flexibility, incumbent workforce pressures, localized labor unavailability) override pure cost optimization.

**Fourth, the care process differentiation hypothesis**: Larger facilities may have developed fundamentally different care processes than smaller facilities, processes that efficiently utilize LPNs and CNAs rather than RNs. If such processes are standardizable, replicable, and quality-producing, then larger facilities' adoption of lower RN-to-LPN ratios reflects process innovation rather than cost-cutting. Under this scenario, the TCE logic still applies—larger facilities achieve efficiency through different means—but the nature of efficiency is not captured by RN-to-LPN ratios alone. Testing this hypothesis would require linked outcomes data examining whether larger facilities' residents experience equivalent or superior outcomes despite lower RN-to-LPN ratios.

### The Donabedian Model Requires Outcome Linkage

Donabedian's Structure-Process-Outcome model posits a causal chain: organizational structure → care processes → resident outcomes. This study examined the first link (does structure, operationalized as facility size, influence staffing composition processes?). The affirmative finding for total staffing but the negative finding for RN-to-LPN ratios suggests that facility size is an incomplete predictor of care processes. More importantly, the model's validity ultimately depends on demonstrating that structure-process changes produce outcome improvements.

The absence of outcome data in this analysis is a critical limitation. It is theoretically possible—even plausible—that larger facilities' lower RN-to-LPN ratios reflect *optimized processes* that achieve quality outcomes with different staffing configurations. Cho and colleagues (2020) found strong associations between RN staffing and quality deficiencies; Huang and colleagues (2025) documented that MSSP participation increased RN hours and reduced LPNs, suggesting a quality-driven policy response. Yet other research (Bowblis & Brunt, 2024) found that even mandated staffing increases produced modest quality improvements, suggesting diminishing returns and the importance of care processes beyond staffing composition.

The Donabedian framework remains valuable for interpreting these findings but requires humility: structural characteristics like facility size predict some variation in staffing processes (explaining ~3% of RN-to-LPN variance, 12% of contract CNA variance when geographic factors are included), but large unmeasured components of variation remain. These unmeasured factors—organizational culture, management quality, labor market conditions, state regulation—likely shape care processes more powerfully than facility size alone.

### Why Geographic/State Factors Dominate Size Effects

A striking finding across both analyses is the dominance of state fixed effects. In the contract CNA model, state indicators increased R² from 0.01 (size effects only) to 0.12 (size + state), suggesting that geographic factors explain approximately 11 times more variation than facility size. Specific state coefficients illustrate this pattern: Vermont facilities used 0.109 higher contract CNA proportions than the national average, while Arkansas facilities used 0.067 lower proportions. These state effects likely reflect regulatory requirements, labor market conditions, cost of living, and regional healthcare system characteristics.

This pattern suggests that staffing decisions are primarily shaped by contextual factors outside individual facilities' control: state minimum staffing standards, Medicaid reimbursement rates (which vary by state), regional wage pressures, and supply of different worker types. TCE predicts that organizations optimize within their given constraints; this finding shows that the constraints themselves (geographic, regulatory) are more powerful drivers of outcomes than organizational size. A facility's location matters more than its size—a conclusion at odds with assumptions that larger entities have superior strategic capacity.

### Integration with Prior Literature

The academic literature shows mixed evidence on economies of scale. Christensen (2003) found economies of scale in average cost functions but also diseconomies of scale in the lower cost distribution. Farsi and colleagues (2008) concluded that "optimal facility size varies depending on local market conditions." Chattopadhyay and Ray (1996) documented that some facility networks were less efficient than comparable smaller independent operators. The current findings—that facility size predicts staffing levels but not staffing mix, and that size effects are dominated by geographic factors—align with this literature of heterogeneous and context-dependent scale effects.

Several cited papers identified mechanisms that override size effects:

- **Payment reforms shift staffing composition**: Huang and colleagues (2025) showed that MSSP participation (a financial incentive structure) increased RN staffing while reducing LPN staffing. This demonstrates that facilities respond to financial incentives more than to organizational structure (size). By extension, if CMS minimum staffing standards (which are size-invariant) constrain RN ratios, then larger facilities cannot further increase RN-to-LPN ratios through economies of scale.

- **Labor market conditions dominate organizational factors**: Kang and colleagues (2024) found that nursing home staffing disparities during COVID-19 were most acute in distressed communities, suggesting that workforce availability (external to the facility) constrains staffing more than facility characteristics.

- **Contract labor serves multiple functions beyond cost minimization**: Khoja and colleagues (2026) found that contract staff use correlates with injurious falls, yet Brazier and colleagues (2023) documented that facilities continued using contract workers despite pandemic workforce shortages, suggesting contract labor serves functions (scheduling flexibility, workforce hedging, episodic needs) beyond pure cost minimization.

- **Staffing instability matters**: Benheim and colleagues (2025) found that staffing variability predicts worse outcomes independent of staffing levels. Larger facilities' apparently lower RN-to-LPN ratios might reflect not efficiency but rather reliance on LPNs due to RN shortage-driven instability and recruitment challenges.

---

## 4. What This Means for Policy and Practice

### Policy Implications: Reconsidering Size-Based Differentiation

Current CMS policy applies uniform minimum staffing standards (3.48 hours per resident day proposed in 2024 rule) regardless of facility size. The implicit assumption is that all facilities, when properly incentivized, can achieve baseline staffing. The empirical findings challenge assumptions that larger facilities have inherent advantages in achieving efficiency or quality through size-related mechanisms.

**Implication 1**: Size-invariant staffing policies may be appropriate given the data. If RN-to-LPN ratios do not systematically improve with size, and if contract labor reliance is driven more by geographic factors than size, then uniform staffing standards can be justified on equity grounds (protecting residents in smaller facilities) rather than abandoning differentiation as efficiency-destroying.

**Implication 2**: State-level variation in contract labor reliance (Vermont +0.109, Arkansas -0.067) suggests that state regulatory environments, labor supply structures, or workforce development initiatives shape staffing strategies more powerfully than facility size. Policies targeting regional workforce development, state-level training initiatives, or regulatory harmonization may be more effective than facility-size-based policies.

**Implication 3**: The financial costs of contract labor (Ghiasi et al., 2023: 10% increase in contract ratio → 0.45-0.52% decrease in operating margin) and its quality costs (Khoja et al., 2026: increased injurious falls) suggest that policy should address the root causes of contract labor reliance (RN shortage, inflexible regulatory requirements, inadequate reimbursement) rather than assuming larger facilities naturally minimize such use through economies of scale.

### Practice Implications: Rethinking Efficiency Strategies

For nursing home administrators and systems, the findings suggest that achieving staffing efficiency through size-related mechanisms may be limited. The implications are sobering:

**Implication 1**: Mergers and consolidations built on assumptions of "economies of scale in staffing" may not produce expected improvements in staffing mix or quality. If larger size does not predictably increase RN-to-LPN ratios or decrease contract labor reliance, then the staffing efficiency argument for consolidation is weakened. Administrators should scrutinize other proposed efficiency gains (administrative consolidation, bulk purchasing, information systems) rather than assuming staffing improvements from growth.

**Implication 2**: Staffing strategy requires attention to external (geographic, regulatory) factors more than internal (size, structure) optimization. Facilities competing for RN recruitment in tight labor markets face fundamentally different constraints than facilities in RN-abundant regions. Practice-based strategies should address these asymmetries: partnerships with nursing education programs, housing support, retention bonuses, and work environment improvements may be more effective than pure scale growth.

**Implication 3**: The lower RN-to-LPN ratios in larger facilities (despite higher total staffing) may reflect rational process design rather than efficiency failure. If larger facilities have developed evidence-based care models that effectively supervise LPNs while maintaining quality, then their staffing composition should not be viewed as inadequate. Conversely, if large facilities' lower RN-to-LPN ratios reflect constrained choices due to RN shortage or cost pressures, then support for RN recruitment and retention becomes critical policy lever.

**Implication 4**: Contract labor use appears driven by specific facility circumstances rather than systematic size-related factors. Facilities using high proportions of contract CNAs may face acute staffing challenges (high turnover, COVID-19 recovery, inadequate local labor supply) rather than structural inefficiency. Practice strategies should distinguish between facilities using contract labor strategically (to manage predictable gaps) versus those using it as a compensation mechanism for chronic understaffing.

### Workforce Planning Insights: Beyond Skill-Mix Rhetoric

The findings reveal complexity in workforce planning that extends beyond simple skill-mix discussions:

**Insight 1**: The persistent RN shortage constrains achievable staffing ratios across facility sizes. Larger facilities cannot "buy their way" to higher RN-to-LPN ratios in tight labor markets. Workforce planning must address supply-side constraints—education pipeline expansion, immigration policy, salary competitiveness relative to hospital settings—rather than assuming demand management through size will resolve shortages.

**Insight 2**: LPN and CNA training/development may be more cost-effective workforce strategies than competing for limited RNs. If larger facilities successfully operate with lower RN-to-LPN ratios (and outcomes are comparable), then policies encouraging LPN quality, advancement, and retention may yield better workforce security than universal RN staffing mandates.

**Insight 3**: The moderate correlation between facility size and RN staffing (r = 0.539) compared to very strong correlations for LPN and CNA staffing (r = 0.811 and 0.887) suggests that RN deployment is discretionary in a way that LPN/CNA staffing is not. This pattern may reflect regulatory minimums for RN presence (compliance-driven) combined with flexibility in total RN hours (efficiency-driven), while LPN and CNA staffing directly scales with resident care needs. Workforce planning should recognize these different drivers.

**Insight 4**: Geographic variation in contract labor use suggests that workforce flexibility strategies differ substantially across regions. Some states/regions may have developed effective alternatives to contract labor (strong local recruitment, public workforce development initiatives, regional staffing networks) while others rely more heavily on temporary workers. Learning from high-performing regions may reveal best practices for contract labor reduction.

---

## 5. Study Strengths and Limitations

### Methodological Strengths

**Large, nationally representative sample**: The analysis included 14,209 nursing homes across 52 states/territories, representing 94.9% of all U.S. nursing homes in the sampling frame. This sample size provides exceptional statistical power and generalizability. Most prior nursing home studies examined single states, regional samples, or smaller national surveys. The large sample reduces sampling error and enables precise estimation of modest effect sizes.

**Comprehensive data: Eight quarters of Payroll-Based Journal data** (CY2023Q1 through CY2024Q4) provide temporal stability verification. Rather than relying on a single snapshot, the analysis examined consistent patterns across two calendar years, capturing seasonal variation and year-to-year trends. The temporal breadth strengthens confidence that relationships are stable rather than artifacts of particular periods or economic conditions.

**Precise measurement from administrative data**: Payroll-Based Journal data capture facility payroll records directly, avoiding recall bias or survey response errors inherent in survey-based research. The distinction between employee and contract workers is recorded administratively (classification in payroll records), providing accurate measurement of contract labor proportions that survey methods might misreport.

**Robust across sensitivity analyses**: The core finding (negative relationship between facility size and RN-to-LPN ratio) remained statistically significant and consistent across six alternative model specifications:
- Alternative outlier thresholds (|z| > 3.5, |z| > 3.0)
- Alternative minimum facility size thresholds (≥30, ≥50 residents/day)
- Quadratic model specification
All sensitivity tests confirmed the stability of findings, increasing confidence in the conclusions.

**Conservative outlier handling**: The analysis applied a strict outlier exclusion rule (|z| > 4 for all continuous variables), removing only 2.9% of observations and remaining transparent about exclusion criteria. This conservative approach minimizes risk of artificially inflated effect sizes that can result from outlier over-exclusion.

### Critical Limitations

**Cross-sectional design prevents causal inference**: While the analysis documents that larger facilities have lower RN-to-LPN ratios and lower contract CNA use on average, the cross-sectional design cannot establish that facility size *causes* staffing composition differences. Selection effects remain plausible: facilities employing lower RN-to-LPN ratios may intentionally grow larger, or facilities in particular geographic/economic contexts both grow larger AND adopt different staffing models. Causal inference would require within-facility longitudinal analysis (examining how individual facilities' staffing changed as they grew/shrank) or instrumental variables, neither of which this study employed.

**Aggregated to facility-level; cannot examine individual episodes**: Payroll-Based Journal data are aggregated to facility-day averages, precluding examination of care episodes, individual resident needs, or unit-level staffing patterns. A nursing home with low average RN-to-LPN ratio might concentrate RN staffing in intensive care units while using LPNs for independent living areas. This study cannot distinguish such tactical allocation from system-wide understaffing.

**Paid hours only; excludes salaried administrative time**: PBJ data capture paid hours including overtime, but may not fully account for salaried management and supervisory time that is not separately itemized. If larger facilities have disproportionately more management overhead, and if management time substitutes for direct care RN time, then this measurement issue could systematically bias size-staffing relationships.

**No outcome data; cannot assess quality implications**: This study demonstrates that larger facilities have lower RN-to-LPN ratios but cannot determine whether residents experience worse or equivalent outcomes. It is theoretically possible that larger facilities' staffing compositions are optimized for efficiency and quality, rendering the lower RN-to-LPN ratios irrelevant or even beneficial. Conversely, lower RN-to-LPN ratios might reflect quality compromises that would be evident in linked outcome data. The Donabedian framework remains incomplete without outcome linkage.

**State/regulatory confounding may bias facility size coefficient**: The dramatic dominance of state fixed effects (explaining 11× more variance in contract CNA use than size) suggests that unmeasured state regulatory and labor market factors confound facility size relationships. For example, states with stronger RN training programs may both have more facilities achieving larger average size AND higher RN-to-LPN ratios, biasing the size coefficient downward. The analysis includes state fixed effects (addressing this for contract CNA outcome) but the H1 model relies on linear size effects without full geographic confounding adjustment.

**Missing ownership and system affiliation data**: CMS data include facility ownership (for-profit, nonprofit, government) and Medicare chain relationships, but these were not linkable to the base PBJ analysis. Agency Theory predicts differential staffing patterns by ownership; this analysis cannot test such interactions. Larger for-profit facilities might follow different staffing strategies than large nonprofits, a distinction this analysis obscures.

**Cross-sectional snapshot of post-pandemic period**: The analysis period (CY2023-CY2024) captures the post-acute COVID-19 period when staffing patterns may remain disrupted relative to pre-pandemic norms. Whether the findings generalize to typical operating periods remains uncertain.

---

## 6. Implications Across Theoretical Frameworks

### Revising Transaction Cost Economics in Healthcare

TCE provides powerful insights into organizational structure, but this study suggests its application to nursing home staffing requires qualification. The core TCE premise—that larger organizations economize on transaction costs and achieve superior efficiency—receives limited support in the staffing domain.

**Why TCE predictions failed**: Transaction cost theory assumes rational optimization and clear efficiency frontiers. In nursing home staffing, constraints override optimization: regulatory minima establish baselines, RN shortages constrain alternatives, and geographic variation dominates firm-level decisions. Larger facilities do not face lower transaction costs in recruiting RNs if RNs are unavailable in their region. They cannot achieve economies of scale in RN staffing if state regulations impose effective ceilings on RN-to-LPN ratios or if quality standards limit substitution elasticity between RN and LPN labor.

**Modified TCE application**: A refined application of TCE might focus on transaction costs that larger organizations genuinely economize on:
- *Administrative transactions*: Larger systems can amortize IT infrastructure, compliance expertise, and management across more facilities.
- *Supply transactions*: Bulk purchasing of medical supplies, pharmaceuticals, equipment.
- *Information transactions*: Technology investments in EHRs and clinical decision support.
- *Non-nursing staffing*: Centralized recruitment for administrative, dietary, housekeeping services.

Transaction costs that DO NOT appear economized by size:
- *Clinical staffing transactions*: RN recruitment, credentialing, and deployment appear driven by labor market conditions, not firm size.
- *Regulatory compliance transactions*: Nursing homes face facility-specific compliance requirements regardless of system size; consolidation may not reduce per-facility transaction costs.

**Implication**: TCE should be applied more selectively in healthcare, distinguishing between domains where scale genuinely produces efficiency (administrative, supply chain) versus domains where external constraints (regulation, labor markets) dominate (clinical staffing). Healthcare is not a typical industry for TCE applications because of sector-specific constraints (universal insurance, regulatory requirements, professional licensing, moral hazard issues).

### Donabedian Model Incompleteness

Donabedian's Structure-Process-Outcome framework remains conceptually sound but this analysis reveals its incompleteness as applied to nursing homes:

**Structure**: Facility size (a structural characteristic) predicts total staffing levels (process input) moderately well (r = 0.539-0.887 depending on staff type) but explains only 3% of RN-to-LPN ratio variance.

**Process**: Staffing composition (process characteristic) is weakly predicted by facility size but strongly predicted by unmeasured factors (geographic, regulatory, organizational). The framework's causal arrow from structure to process is partially broken by confounders.

**Outcome**: This study cannot examine the outcome link; without outcome data, the process-outcome relationship remains untested. Is lower RN-to-LPN ratio in larger facilities associated with worse resident outcomes (supporting concern) or equivalent/superior outcomes (supporting efficiency hypothesis)?

**Implication**: The framework should be expanded to acknowledge that processes in regulated organizations are constrained by external regulation (S→P linkage is partially mediated by regulation) and that outcome relationships may be non-linear or dependent on organizational context. A revised model might include regulatory environment, labor market conditions, and organizational culture as moderators of structure-process-outcome relationships.

---

## 7. Research Gaps Revealed by This Study

This research, while addressing prior gaps, reveals new questions:

1. **Do larger facilities' lower RN-to-LPN ratios reflect optimized processes or constrained choices?** Outcome-linked analysis would clarify whether residents in facilities with lower RN-to-LPN ratios experience equivalent or inferior outcomes. If equivalent, this would suggest process optimization; if inferior, it would suggest quality compromise.

2. **What mechanisms explain state variation in contract labor use?** The 0.177-unit range in contract CNA proportions across states (Vermont to Arkansas) is enormous. Understanding whether this reflects regulatory differences, labor supply variation, cost-of-living effects, or management practices could yield actionable policy insights.

3. **Do within-facility staffing allocation patterns differ by facility size?** Larger facilities might concentrate RNs in high-acuity units while using LPNs elsewhere, obscuring average staffing composition effects. Granular unit-level data would clarify whether low average RN-to-LPN ratios mask efficient specialization.

4. **How does staffing instability (emphasized by Benheim et al., 2025) correlate with facility size and contract labor use?** Are larger facilities' lower RN-to-LPN ratios associated with greater staffing turnover or instability, which Benheim and colleagues found predicts worse outcomes?

5. **What role do nursing education pipelines and regional professional networks play in staffing composition?** Geographic variation in staffing might reflect differential access to nursing education, professional associations, or training programs that shape the workforce available to facilities.

6. **How do care processes and management practices mediate the facility size-staffing composition relationship?** Within similarly-sized facilities, variation in RN-to-LPN ratios is enormous (IQR = 0.28-0.79). What management practices, care models, or technological investments enable some facilities to operate with low RN-to-LPN ratios while others require higher RN ratios? Such variation may yield best practices.

---

## Summary: Resolving the Contradiction

This study set out to test whether larger nursing homes achieve staffing efficiency through economies of scale. The theoretical prediction was clear: larger facilities should employ higher RN-to-LPN ratios and lower contract CNA proportions. Instead, the data revealed the opposite pattern for RN-to-LPN ratios and no pattern for contract CNAs.

Rather than dismissing these contradictions as anomalies, treating them as scientific opportunities has yielded important insights:

1. **Facility size is a weaker determinant of staffing decisions than regulatory and labor market factors.** While size predicts total staffing levels, it does not predict staffing composition or contract labor use once geographic factors are considered.

2. **Larger facilities' lower RN-to-LPN ratios may reflect either constrained optimization (rational response to RN shortage) or optimized processes (deliberately designed care models).** Without outcome data, we cannot distinguish these explanations, highlighting the need for linked analyses.

3. **Transaction cost economics provides limited predictive value for nursing home staffing.** While TCE explains administrative and supply chain economies of scale, it poorly predicts clinical staffing patterns that respond primarily to regulation and labor market conditions.

4. **Geographic factors dominate firm-level decisions.** State-level variation in contract labor use (11× greater than size effects) emphasizes that nursing home staffing operates within constrained policy environments that override organizational optimization.

5. **Future policy and research should focus on external constraints (RN supply, regulation, reimbursement) rather than assuming internal efficiency mechanisms (economies of scale) will resolve staffing challenges.** The persistent workforce crisis in nursing homes likely reflects macro-level problems (inadequate supply of healthcare workers, unfavorable work conditions, competing healthcare demands) rather than micro-level inefficiency in larger facilities.

These conclusions reorient staffing discussions from a narrative of "larger facilities achieve efficiency" to a more complex reality of "staffing patterns reflect constrained choices within regulatory and labor market frameworks." This reorientation has profound implications for policy (external constraints require external policy solutions), practice (internal consolidation strategies have limited staffing efficiency payoff), and theory (TCE applies differently in regulated versus market-driven industries).

