# Study: Staffing Mix Efficiency and Economies of Scale in Nursing Homes

## Research Question
Do larger nursing home facilities achieve a more efficient staffing mix (higher Registered Nurse [RN]-to-Licensed Practical Nurse [LPN] ratio) than smaller facilities, or does facility size increase reliance on contract Certified Nursing Assistants (CNAs)?

## Background and Significance
Nursing home staffing represents a critical determinant of both operational efficiency and quality of care. The economics of scale in nursing homes suggest that larger facilities may achieve staffing synergies through centralized management, pooled resources, and economies of recruitment. However, recent literature indicates mixed results: while larger facilities may sustain higher average staffing levels, the composition of staffing mix—particularly the proportion of high-skill versus low-skill workers—remains unclear. This study examines whether facility size (measured by resident census) is associated with staffing efficiency, defined as the prevalence of RN-to-LPN ratios and contract labor use patterns.

### Key Research Gap
Prior work on nursing home staffing has focused on absolute staffing levels (total hours per resident day) but has not systematically examined whether facility size is associated with meaningful differences in staffing composition and skill mix optimization. Understanding these patterns has implications for workforce planning, labor market dynamics, and regulatory policy.

## Primary Research Hypotheses

### H1: RN-to-LPN Ratio Increases with Facility Size
Larger facilities (higher MDScensus) maintain proportionally higher RN-to-LPN staffing ratios, suggesting greater clinical oversight and sophisticated care delivery models.

### H2: Contract CNA Reliance Follows an Inverted-U Pattern
Mid-sized facilities (census 50-150) show the highest contract CNA reliance (proportion of contract hours to total CNA hours), while both small and large facilities maintain lower contract labor ratios through different mechanisms: small facilities use direct-hire staff due to intimate operational scale; large facilities achieve staffing stability through internal recruitment and advancement programs.

## Study Design
**Type**: Cross-sectional analysis of nursing home facilities stratified by daily resident census deciles.

**Data Source**: CMS Payroll-Based Journal (PBJ) daily nurse staffing data (calendar quarters to be determined).

**Population**: Medicare-certified nursing homes with complete staffing records and no missing values on key variables.

**Study Period**: CY 2023-Q1 to CY 2024-Q4 (four consecutive quarters representing stable post-pandemic staffing patterns).

## Key Variables

### Outcome Variables
- **RN-to-LPN Ratio**: Calculated as mean Hrs_RN divided by mean Hrs_LPN per facility per quarter, stratified by census decile
- **Contract CNA Proportion**: Calculated as contract hours divided by total CNA hours (sum of direct-hire and contract)
- **Staffing Efficiency Index**: Multi-dimensional measure combining RN intensity, LPN utilization, and contract labor proportion

### Exposure Variable
- **Facility Size (Continuous & Stratified)**:
  - Continuous: MDScensus (daily resident census from MDS)
  - Stratified: Deciles of MDScensus (for comparison tables and visualizations)

### Covariates
- **Facility Characteristics**: For-profit vs. non-profit status, chain affiliation, geographic region (by census division)
- **State Fixed Effects**: To account for state-level regulatory and market differences
- **Temporal Indicators**: Quarter indicators to capture seasonal staffing variation

## Analysis Plan

### Primary Analysis
1. **Descriptive Statistics**: Characterize the sample by facility size deciles
2. **Non-Linear Regression**: Fit restricted cubic splines (RCS) with 3-4 knots to model the relationship between MDScensus and:
   - RN-to-LPN ratio
   - Contract CNA proportion
   - Staffing efficiency index
3. **Stratified Analysis**: Repeat analyses stratified by facility ownership type (for-profit vs. non-profit)
4. **Sensitivity Analysis**: Exclude extreme outliers (|z| > 4 on all continuous variables) and re-fit models

### Secondary Analysis
1. **Efficiency Frontier**: Estimate Data Envelopment Analysis (DEA) frontier for staffing efficiency
2. **Regional Variation**: Test for significant heterogeneity in staffing patterns by US Census division

## Key Variables for Analysis (PBJ Mapping)

| PBJ Variable | Human-Readable Label | Role |
|--------------|---------------------|------|
| MDScensus | Daily Resident Census | Exposure (facility size) |
| Hrs_RN | Registered Nurse Hours | Outcome (numerator for RN-to-LPN ratio) |
| Hrs_LPN | Licensed Practical Nurse Hours | Outcome (denominator for RN-to-LPN ratio) |
| Hrs_CNA | Certified Nursing Assistant Hours (Direct-Hire) | Outcome (staffing mix) |
| Hrs_CNA_ctr | Contract CNA Hours | Outcome (contract labor reliance) |
| PROVNUM | Facility Provider Number | Facility identifier |
| PROVNAME | Facility Name | Facility identifier |
| STATE | State | Geographic covariate |
| CY_Qtr | Calendar Quarter | Temporal indicator |
| For_Profit | For-Profit Status | Ownership covariate |
| Chain | Chain Affiliation | Ownership covariate |

## Expected Outcomes

### Primary Finding
We expect to observe:
1. A significant, positive non-linear relationship between facility size and RN-to-LPN ratio
2. An inverted-U shaped relationship between facility size and contract CNA proportion, peaking in the mid-size range (deciles 4-6)
3. Statistically significant interactions between facility size and ownership type

### Manuscript Contributions
1. **Empirical Evidence**: First comprehensive national analysis of staffing mix efficiency by facility size using PBJ data
2. **Operational Insight**: Identification of optimal facility size for staffing efficiency and cost control
3. **Policy Implications**: Evidence-based recommendations for facility management and workforce planning

## Publication Target
A peer-reviewed manuscript of 12-15 pages suitable for:
- *Health Affairs*
- *Health Services Research*
- *Inquiry: Journal of Health Care Organization, Provision, and Financing*
- *Journal of Health Economics*

## Timeline
- Phase 1 (Literature): 5 working days
- Phase 2 (Research Planning): 2 working days
- Phase 3 (Methods): 2 working days
- Phase 4 (Analysis): 3 working days
- Phase 5 (Synthesis): 2 working days
- Phase 6 (Manuscript): 5 working days
- Phase 7 (Presentation): 2 working days
- Phase 8 (Publication): 1 working day
- **Total**: ~22 working days

## Quality Assurance
- Literature review: Minimum 20 citations (target), 15 citations (absolute floor)
- Manuscript: 12-15 pages, APA formatted, publication-quality
- Analysis: All scripts reproducible; outlier screening documented
- Visuals: STROBE flow diagram, efficiency frontier plots, census-stratified comparisons
- Data security: All analysis in PBJ analysis vault (Docker, isolated from network)

---

**Study Initiated**: February 4, 2026  
**Principal Coordinator**: Elwood Research  
**Data Source**: CMS Payroll-Based Journal (PBJ) Public Use Files  
**Repository**: Will be published to GitHub (Elwood-Research organization) upon completion
