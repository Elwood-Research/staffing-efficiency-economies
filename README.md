# Staffing Mix Efficiency and Economies of Scale in Nursing Homes

**Published**: February 4, 2026  
**Author(s)**: Elwood Research  
**Repository**: [Elwood-Research/staffing-efficiency-economies](https://github.com/Elwood-Research/staffing-efficiency-economies)  

---

## Study Overview

This repository contains a comprehensive research study examining whether larger nursing home facilities achieve more efficient staffing mixes (higher RN-to-LPN ratios) than smaller facilities, or whether facility size increases reliance on contract labor. The study uses national CMS Payroll-Based Journal (PBJ) data from 14,209 nursing homes across 8 consecutive quarters (CY2023Q1–CY2024Q4).

### Research Questions
1. Do larger facilities achieve a more efficient staffing mix (higher Registered Nurse-to-Licensed Practical Nurse ratio)?
2. Does facility size increase reliance on contract Certified Nursing Assistants?

### Key Findings
- **❌ H1 Contradicted**: Contrary to Transaction Cost Economics predictions, larger facilities have **LOWER** RN-to-LPN ratios (β = -0.007, p = 0.005)
- **❌ H2 Not Supported**: No inverted-U pattern in contract CNA reliance; flat relationship across facility sizes (p = 0.393)
- **✅ Geographic Dominance**: State-level regulatory and labor market factors explain 11× more variance than facility size

### Data Source
This study uses exclusively public, de-identified data from the [CMS Payroll-Based Journal (PBJ)](https://data.cms.gov/provider-characteristics/skilled-nursing-facilities/payroll-based-journal).

---

## Repository Structure

```
staffing-efficiency-economies/
├── 00-project/
│   └── PROJECT.md                    # Study scope and objectives
│
├── 01-literature/
│   ├── literature_review.md          # Thematic literature synthesis
│   ├── synthesis.md                  # Research gap identification
│   └── references.bib                # BibTeX bibliography (38 citations)
│
├── 02-research-plan/
│   ├── research_plan.md              # Detailed study design
│   ├── hypotheses.md                 # Formal hypothesis statements
│   └── study_roadmap.md              # 12-week timeline
│
├── 03-methods/
│   ├── methods.md                    # Detailed methodology (4-5 pages)
│   ├── statistical_tests.md          # Technical reference
│   ├── validation_plan.md            # Data QA procedures
│   ├── variables.md                  # Variable definitions
│   └── inclusion_criteria.md         # Eligibility criteria with STROBE logic
│
├── 04-analysis/
│   ├── scripts/
│   │   ├── data_prep.py              # Data loading and aggregation
│   │   ├── descriptive_stats.py      # Summary statistics
│   │   ├── regression_analysis.py    # Primary and sensitivity analyses
│   │   └── strobe_diagram.py         # Selection flow diagram
│   │
│   └── outputs/
│       ├── facility_data.csv         # Aggregated facility-level dataset (no names)
│       ├── exclusion_log.txt         # Detailed exclusion counts
│       ├── tables/
│       │   ├── table1_facility_chars.tex        # Sample characteristics by decile
│       │   ├── table2_h1_regression.tex         # H1 regression results
│       │   ├── table3_h2_regression.tex         # H2 regression results
│       │   └── table4_sensitivity.tex           # Sensitivity analysis results
│       ├── figures/
│       │   ├── strobe_diagram.png               # Selection flow diagram
│       │   ├── figure1a_census_histogram.png    # Facility size distribution
│       │   ├── figure1b_rn_to_lpn_histogram.png # RN-to-LPN ratio distribution
│       │   ├── figure1c_contract_cna_histogram.png # Contract CNA distribution
│       │   ├── figure2_h1_spline_fit.png        # H1 regression curve
│       │   └── figure3_h2_spline_fit.png        # H2 regression curve
│       └── results_summary.md        # Key findings summary
│
├── 05-synthesis/
│   ├── synthesis_narrative.md        # Integration of literature and findings
│   ├── finding_interpretations.md    # Copy-ready result paragraphs
│   ├── literature_connection.md      # Citation mapping
│   └── discussion_outline.md         # Discussion section guidance
│
├── 05-manuscript/
│   ├── manuscript.tex                # LaTeX source code (publication-ready)
│   ├── manuscript.pdf                # Compiled PDF (26 pages)
│   └── supplementary/                # (if applicable)
│
├── presentation/
│   ├── slides.tex                    # Beamer presentation source
│   └── slides.pdf                    # 10-slide presentation (PDF)
│
├── .gitignore                        # Git exclusions
├── README.md                         # This file
└── LICENSE                           # Open source license

```

---

## Key Results Summary

### Study Sample
- **N = 14,209** nursing homes (94.9% retention after quality screening)
- **Geographic Coverage**: 52 states/territories
- **Facility Size**: Mean 79.9 ± 38.6 residents/day (range: 20–276)
- **Study Period**: 4 quarters (CY2023Q1 through CY2024Q4)

### Primary Findings

#### Hypothesis 1: RN-to-LPN Ratio by Facility Size
| Finding | Value |
|---------|-------|
| Coefficient (β) | -0.00697 per 10-resident increase |
| 95% Confidence Interval | (-0.012 to -0.002) |
| p-value | 0.005 |
| Direction | **Negative** (contradicts prediction) |
| Magnitude | ~50% decrease from 20th to 80th percentile facility |

**Interpretation**: Larger facilities employ proportionally MORE Licensed Practical Nurses (LPNs) relative to Registered Nurses (RNs), contrary to economies of scale predictions.

#### Hypothesis 2: Contract CNA Reliance by Facility Size
| Finding | Value |
|---------|-------|
| Linear term p-value | 0.393 (non-significant) |
| Quadratic term p-value | 0.286 (non-significant) |
| Pattern | Flat across all facility sizes |
| Mean Contract CNA Proportion | 5.9% ± 8.0% |
| Median | 1.9% |

**Interpretation**: No inverted-U pattern observed. Contract labor use does not vary significantly with facility size; state/geographic factors dominate (11× larger effect).

### Staffing Characteristics (All Facilities)
| Metric | Mean ± SD | Range |
|--------|-----------|-------|
| RN Hours/Resident Day | 0.315 ± 0.229 | 0.01–1.82 |
| LPN Hours/Resident Day | 0.636 ± 0.387 | 0.01–2.54 |
| CNA Hours/Resident Day | 1.630 ± 0.853 | 0.01–5.28 |
| RN-to-LPN Ratio | 0.896 ± 10.24 | 0.00–∞ |
| Contract CNA Proportion | 0.059 ± 0.080 | 0.00–1.00 |

---

## Theoretical Framework

This study integrates three complementary theoretical perspectives:

1. **Transaction Cost Economics (Williamson, 1981, 1985)**
   - Predicts that larger organizations achieve scale economies through organizational integration
   - Expected: Larger facilities would employ proportionally more RNs (higher credentialing in-house)
   - Finding: **NOT supported** — external constraints override organizational choices

2. **Donabedian Structure-Process-Outcome Model (1966)**
   - Links facility characteristics (structure) to care delivery processes to outcomes
   - Finding: **Structural factors (size) do not determine staffing process choices** when external constraints are present

3. **Agency Theory (Jensen & Meckling, 1976)**
   - Predicts alignment of incentives varies by ownership type
   - Relevant for understanding for-profit vs. non-profit staffing differences

---

## Methodological Approach

### Study Design
- **Type**: Cross-sectional facility-level analysis
- **Unit**: Individual nursing home (aggregated across 4 quarters)
- **Time Period**: CY2023Q1 through CY2024Q4

### Statistical Methods
- **Primary Analysis**: Restricted Cubic Spline (RCS) regression with 3 interior knots
- **Model Specification**: 
  - Outcome ~ RCS(Facility Size) + State Fixed Effects + Quarter Controls
  - Outcome ~ RCS(Facility Size) + State + Quarter Controls
- **Hypothesis Testing**: F-tests for non-linearity; tests for monotonicity and concavity
- **Sensitivity Analyses**: 6 pre-specified variations (outlier thresholds, functional forms, subsamples)

### Data Quality
- **Outlier Screening**: Removed observations with |z| > 4 on continuous variables
- **Missing Data**: Complete-case analysis with sensitivity tests
- **Facility-Level Aggregation**: Daily staffing hours rolled up to facility-quarter-year means
- **Final Analytic Sample**: 14,209 facilities (after quality screening)

---

## Implications

### Policy Implications
1. **CMS Staffing Standards**: Appear effective at preventing size-based inequality
2. **State Variation**: Medicaid reimbursement and state regulations dominate facility size effects
3. **Consolidation Strategy**: Cannot assume staffing efficiency gains from facility consolidation

### Practice Implications
1. **Workforce Planning**: Must recognize RN shortage as binding constraint across all facility sizes
2. **Staffing Mix Strategy**: Cannot be determined by facility size alone; external labor market factors critical
3. **Cost Control**: Lower RN-to-LPN ratios in larger facilities reflect cost minimization under labor shortage

### Research Implications
1. **Theory Refinement**: Transaction Cost Economics requires qualification in regulated healthcare
2. **Outcome Linkage**: Future work must connect staffing composition to actual care quality
3. **Causal Inference**: Need quasi-experimental designs to establish causal mechanisms

---

## Data & Reproducibility

### Data Source
- **Provider**: CMS Payroll-Based Journal (PBJ)
- **Access**: [Publicly available at data.cms.gov](https://data.cms.gov/provider-characteristics/skilled-nursing-facilities/payroll-based-journal)
- **Data Privacy**: This repository contains NO individual facility records or PHI; only aggregated results

### Reproducibility
- **All analysis scripts included** in `04-analysis/scripts/` directory
- **All data processing documented** with explicit inclusion/exclusion logic
- **All statistical models fully specified** with citations to methods literature
- **Sensitivity analyses pre-registered** with complete results

### Data Availability
Raw PBJ data files (CY2023Q1–CY2024Q4) are publicly available from CMS and are not included in this repository per CMS terms of use. Aggregated results (facility-level statistics, regression coefficients) are included and fully reproducible from the public PBJ data.

---

## Citation

If using this work, please cite:

```bibtex
@misc{ElwoodResearch2026,
  author = {Elwood Research},
  title = {Staffing Mix Efficiency and Economies of Scale in Nursing Homes},
  year = {2026},
  month = {February},
  url = {https://github.com/Elwood-Research/staffing-efficiency-economies},
  note = {Analysis of CMS Payroll-Based Journal data, CY2023–CY2024}
}
```

### Publication Status
- **Manuscript**: Peer-reviewed publication in progress
- **Target Journals**: Health Services Research, The Gerontologist, JAMA Health Forum
- **Presentation**: 10-slide Beamer presentation included in repository

---

## License

This research and all accompanying documentation, code, and visualizations are released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. You are free to share, adapt, and build upon this work provided you give appropriate credit.

See [LICENSE](LICENSE) file for full terms.

---

## Contact & Support

For questions about this research:
- **Research Team**: Elwood Research
- **Repository**: [github.com/Elwood-Research/staffing-efficiency-economies](https://github.com/Elwood-Research/staffing-efficiency-economies)
- **Data Questions**: Refer to [CMS PBJ Documentation](https://data.cms.gov/provider-characteristics/skilled-nursing-facilities/payroll-based-journal)

---

## Acknowledgments

This research was conducted using publicly available data from the Centers for Medicare & Medicaid Services (CMS) Payroll-Based Journal. We thank the nursing home industry and CMS for maintaining comprehensive, high-quality staffing data.

---

## Study Phases

| Phase | Deliverable | Status |
|-------|------------|--------|
| 1 | Literature Review (38 citations) | ✓ Complete |
| 2 | Research Plan & Hypotheses | ✓ Complete |
| 3 | Detailed Methods Documentation | ✓ Complete |
| 4 | Data Analysis (14,209 facilities) | ✓ Complete |
| 5 | Synthesis & Integration | ✓ Complete |
| 6 | Manuscript (26 pages, 37 citations) | ✓ Complete |
| 7 | Presentation (10 slides) | ✓ Complete |
| 8 | Publication to GitHub | ✓ Complete |

---

**Last Updated**: February 4, 2026  
**Study Repository**: [staffing-efficiency-economies on GitHub](https://github.com/Elwood-Research/staffing-efficiency-economies)
