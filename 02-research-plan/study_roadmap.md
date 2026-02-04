# Study Roadmap: Staffing Mix Efficiency and Economies of Scale in Nursing Homes

## EXECUTIVE SUMMARY

This document provides a comprehensive, phase-based timeline for executing the research study from literature review through GitHub publication. The roadmap spans **12 weeks** with clear milestones, deliverables, data management protocols, contingency plans, and quality assurance checkpoints. Eight sequential phases ensure reproducible, publication-quality research output.

---

## PHASE 1: LITERATURE REVIEW AND SYNTHESIS (Weeks 1–2)

### 1.1 Objectives
- Identify and collect ≥20 peer-reviewed citations addressing nursing home staffing, facility size, economies of scale, and transaction cost economics
- Synthesize literature findings to establish theoretical framework and identify research gaps
- Produce narrative literature review and synthesis document

### 1.2 Key Activities
1. **Literature Search** (Days 1–3):
   - Search academic databases: PubMed, Google Scholar, ProQuest, Business Source Complete
   - Search terms: "nursing home staffing", "facility size economies of scale", "transaction cost economics healthcare", "contract labor nursing", "RN LPN ratio"
   - Target: 20–30 papers
   - Required: All papers must have valid DOI (digital object identifier)

2. **Literature Screening** (Days 4–5):
   - Review abstracts; assess relevance to research question
   - Select 20–25 most relevant papers
   - Verify DOI for each selected paper

3. **Literature Synthesis** (Days 6–10):
   - Read full texts of selected papers
   - Extract: Author, year, DOI, study design, key findings, relevance to transaction cost economics framework
   - Organize by theme: (a) nursing home staffing levels, (b) facility size effects, (c) economies of scale, (d) contract labor use, (e) transaction cost theory, (f) healthcare labor markets
   - Write synthesis document identifying key findings and research gaps

4. **Bibliography Creation** (Days 11–14):
   - Create BibTeX file (`references.bib`) with complete citations and DOI fields
   - Format: natbib-compatible entries
   - Verify all DOIs are functional (cross-reference with published papers)

### 1.3 Deliverables
- [ ] `01-literature/literature_review.md` (2–3 pages): Narrative review of selected papers
- [ ] `01-literature/synthesis.md` (2–3 pages): Synthesis document identifying theoretical framework, prior findings, and research gaps
- [ ] `01-literature/references.bib`: Complete BibTeX bibliography with 20+ citations, all with DOI fields

### 1.4 Quality Gate (Minimum Thresholds)
- **✓ PASS if**: ≥20 citations collected, all with valid DOIs; synthesis identifies theoretical framework; research gap clearly articulated
- **✗ FAIL if**: <20 citations, missing DOIs, synthesis is mere list (no synthesis), or theory not identified

### 1.5 Resource Requirements
- Access to academic databases (Google Scholar, PubMed, ProQuest)
- ~40–50 hours analyst effort

### 1.6 Contingency Plans
**If literature search yields <15 papers initially:**
- Expand search to gray literature (CMS reports, nursing home association white papers)
- Broaden search terms to include related healthcare staffing topics
- Target recent papers (last 5 years) to ensure contemporary relevance

**If DOI verification fails for selected papers:**
- Search alternative DOI lookup services (CrossRef, Semantic Scholar)
- Manually verify through journal websites
- If DOI cannot be verified, replace paper with alternative

---

## PHASE 2: RESEARCH PLANNING AND HYPOTHESIS SPECIFICATION (Week 3)

### 2.1 Objectives
- Finalize research plan with explicit study design, population definition, and analysis approach
- Specify falsifiable primary and secondary hypotheses
- Confirm all variables exist and are measurable in PBJ data

### 2.2 Key Activities
1. **Research Plan Development** (Days 1–3):
   - Document study design, population definition, time period, inclusion/exclusion criteria
   - Define theoretical framework and how it guides hypotheses
   - Specify data collection procedures and quarters selected
   - Develop analysis plan overview

2. **Variable Confirmation** (Days 4–6):
   - Query PBJ data dictionaries for all required variables (CY2023Q1, CY2024Q4)
   - Verify presence of: MDScensus, Hrs_RN, Hrs_LPN, Hrs_CNA, Hrs_CNA_ctr, etc.
   - Check consistency across all four quarters
   - Create variable mapping table (PBJ names → human-readable labels)

3. **Hypothesis Specification** (Days 7–8):
   - State primary hypotheses (H1, H2) with explicit predictions
   - Specify expected effect sizes (conservative estimates) based on literature
   - Develop falsifiability statements for each hypothesis
   - Outline secondary hypotheses (H3, H4) conditional on data availability

4. **Inclusion/Exclusion Criteria Finalization** (Day 9):
   - Document explicit, measurable inclusion criteria
   - Document explicit, measurable exclusion criteria
   - Create flow chart showing exclusion logic and expected sample sizes

5. **Study Roadmap and Timeline** (Days 10–11):
   - Create detailed phase-by-phase timeline with milestones
   - Identify data management considerations and contingencies
   - Specify resource requirements

### 2.3 Deliverables
- [ ] `02-research-plan/research_plan.md` (4–5 pages): Complete research plan
- [ ] `02-research-plan/hypotheses.md` (3–4 pages): Detailed hypothesis specifications
- [ ] `03-methods/variables.md` (4–5 pages): Variable definitions, mapping table, aggregation formulas
- [ ] `03-methods/inclusion_criteria.md` (3–4 pages): Explicit inclusion/exclusion criteria with flow chart and sample size expectations
- [ ] `02-research-plan/study_roadmap.md` (this document): Phase-by-phase roadmap

### 2.4 Quality Gate (Minimum Thresholds)
- **✓ PASS if**: 
  - Hypotheses are falsifiable and testable
  - All required variables confirmed in PBJ data dictionaries
  - Inclusion/exclusion criteria are explicit and measurable
  - Expected sample sizes documented (7,100–9,100 facilities)
  - Theoretical framework clearly articulated
- **✗ FAIL if**: 
  - Hypotheses are vague or non-falsifiable
  - Required variables missing from PBJ data
  - Criteria are non-specific ("some" missingness, etc.)
  - No sample size estimation

### 2.5 Resource Requirements
- ~30–40 hours analyst effort
- Access to PBJ data dictionaries

---

## PHASE 3: METHODS AND STATISTICAL ANALYSIS PLAN (Week 4)

### 3.1 Objectives
- Develop detailed statistical methodology
- Specify regression models, assumptions, diagnostics
- Plan sensitivity analyses and model robustness checks
- Outline STROBE diagram construction

### 3.2 Key Activities
1. **Statistical Methodology Documentation** (Days 1–3):
   - Specify restricted cubic spline regression models for hypothesis testing
   - Document model specifications: outcomes, exposures, covariates, link functions
   - Justify statistical choices with citations

2. **Model Assumption Documentation** (Days 4–5):
   - Linearity/functional form: Spline basis expansions, rationale for knot placement
   - Residual normality: Q-Q plots, Shapiro-Wilk tests; log/logit transformation protocols
   - Heteroscedasticity: Breusch-Pagan test; robust standard errors if needed
   - Multicollinearity: Variance inflation factor thresholds (VIF <5)

3. **Diagnostic Plan** (Day 6):
   - Outlier detection protocol (|z| > 4 rule)
   - Residual plot inspection procedures
   - Influence diagnostics (Cook's distance, DFBETAS)

4. **Sensitivity Analysis Plan** (Days 7–8):
   - Outlier exclusion sensitivity (|z| > 4 vs. |z| > 3)
   - Minimum census threshold sensitivity (≥20, ≥30, ≥10 beds)
   - Quarterly aggregation variations
   - Alternative outcome specifications (log-transformed ratios, logit-transformed proportions)

5. **STROBE Diagram Planning** (Day 9):
   - Define flow chart structure (exclusion logic)
   - Identify data points to report (starting N, exclusions at each step, final N)
   - Plan for integration into final manuscript

### 3.3 Deliverables
- [ ] `03-methods/methods.md` (4–6 pages): Detailed methodology including statistical models, diagnostics, sensitivity plans
- [ ] `03-methods/strobe_planning.txt` (1 page): STROBE diagram content outline

### 3.4 Quality Gate (Minimum Thresholds)
- **✓ PASS if**:
  - Statistical models are clearly specified with mathematical notation
  - Assumptions and diagnostics plan documented
  - Sensitivity analyses planned with explicit protocols
  - STROBE elements identified
- **✗ FAIL if**: 
  - Models are vague ("will fit regression")
  - No diagnostic plan
  - No sensitivity analyses planned

### 3.5 Resource Requirements
- ~25–30 hours analyst effort
- Statistical software (Python/statsmodels, R, or equivalent)

---

## PHASE 4: DATA PREPARATION AND ANALYSIS (Weeks 5–7)

### 4.1 Objectives
- Extract and clean raw PBJ daily data
- Aggregate to facility-level summaries
- Conduct descriptive statistics
- Execute primary regression analyses
- Generate STROBE flow diagram and results tables/figures

### 4.2 Key Activities

#### Week 5: Data Preparation
1. **Data Extraction** (Days 1–2):
   - Extract raw PBJ files (CY2023Q1–CY2024Q4) from secure data repository
   - Load into pbj-analysis-vault Docker container
   - Verify file integrity (row counts, column structure)

2. **Data Cleaning** (Days 3–5):
   - Check for missing values, duplicates, data type issues
   - Apply inclusion/exclusion criteria sequentially
   - Document exclusions in data cleaning log
   - Generate intermediate sample size estimates

3. **Facility-Level Aggregation** (Days 6–7):
   - Compute daily aggregates per facility-quarter
   - Calculate facility-level summary statistics:
     - Mean daily census, RN hours, LPN hours, CNA hours, contract CNA hours
     - Facility-period aggregates (total person-days, ratios)
     - Derived variables (RN-to-LPN ratio, contract CNA proportion, efficiency index)
   - Verify aggregation logic (control checks: totals should equal sums)

#### Week 6: Descriptive Statistics and Outlier Screening
1. **Outlier Detection** (Days 1–2):
   - Calculate z-scores for all continuous facility-level variables
   - Identify facilities with |z| > 4.0
   - Investigate outliers; document decisions (exclude or retain)

2. **Descriptive Statistics** (Days 3–5):
   - Generate summary statistics (n, mean, SD, median, IQR, range) for all key variables
   - Stratify by census decile
   - Create **Table 1: Facility Characteristics by Census Decile**
     - Includes: n per decile, mean census, staffing hours, RN-to-LPN ratio, contract CNA proportion
   - Create frequency distributions and histograms for key variables

3. **Final Sample Determination** (Day 6):
   - Report final analytic sample size (expected 7,100–9,100 facilities)
   - Compare characteristics to starting population to assess representativeness

#### Week 7: Primary Regression Analyses
1. **Model Fitting** (Days 1–3):
   - Fit restricted cubic spline regression models for H1 (RN-to-LPN ratio) and H2 (contract CNA proportion)
   - Include state and quarter fixed effects as covariates
   - Report model coefficients, standard errors, p-values, confidence intervals

2. **Model Diagnostics** (Days 4–5):
   - Generate diagnostic plots (residuals, Q-Q plots, fitted vs. residuals)
   - Test for model assumptions (normality, heteroscedasticity, multicollinearity)
   - Assess goodness-of-fit (R², adjusted R², F-statistics)

3. **Results Visualization** (Day 6):
   - Create spline plots showing predicted RN-to-LPN ratio and contract CNA proportion across facility size range
   - Create **Figure 1: RN-to-LPN Ratio vs. Facility Size**
   - Create **Figure 2: Contract CNA Proportion vs. Facility Size**

4. **STROBE Flow Diagram** (Day 7):
   - Generate flow diagram showing exclusion logic and final sample
   - Create **Figure 3: STROBE Flow Diagram**

### 4.3 Deliverables
- [ ] `04-analysis/scripts/data_prep.py`: Data extraction, cleaning, aggregation script
- [ ] `04-analysis/scripts/descriptive_stats.py`: Summary statistics and Table 1 generation
- [ ] `04-analysis/scripts/analysis.py`: Primary regression models
- [ ] `04-analysis/outputs/tables/table1.tex`: Facility characteristics by census decile
- [ ] `04-analysis/outputs/figures/figure1.png`: RN-to-LPN ratio spline plot
- [ ] `04-analysis/outputs/figures/figure2.png`: Contract CNA proportion spline plot
- [ ] `04-analysis/outputs/figures/figure3_strobe.png`: STROBE flow diagram
- [ ] `04-analysis/results_summary.md` (2–3 pages): Summary of descriptive and analytical findings

### 4.4 Quality Gate (Minimum Thresholds)
- **✓ PASS if**:
  - Final sample size is 7,000+ facilities
  - All analysis scripts run without errors inside Docker vault
  - Descriptive statistics table completed
  - Primary regression models converge
  - STROBE diagram complete and accurate
  - Results are logically consistent with theoretical predictions (or clearly contradict them)
- **✗ FAIL if**:
  - Final sample <5,000 facilities
  - Scripts have runtime errors
  - Table/figures missing
  - Models fail to converge
  - Extreme anomalies in results unexplained

### 4.5 Resource Requirements
- **Computing**: Docker pbj-analysis-vault container with Python 3, pandas, numpy, scipy, statsmodels, matplotlib
- **Storage**: ~5–10 GB for raw PBJ files (read-only)
- **Effort**: ~80–100 hours analyst effort (40–50 hours data prep; 30–40 hours analysis; 10–15 hours visualization)

### 4.6 Contingency Plans
**If final sample falls below 5,000:**
- Relax inclusion criteria (e.g., lower minimum census to ≥10 beds) and recompute
- Investigate why exclusion rate exceeds expectations
- Document revised approach and sensitivity to threshold changes

**If primary models fail to converge:**
- Check for multicollinearity or extreme outliers (may need to exclude more facilities)
- Consider alternative functional forms (quadratic instead of spline; linear instead of non-linear)
- Apply regularization (ridge regression) if sample-to-parameter ratio is poor

**If STROBE diagram reveals unexpected exclusion patterns:**
- Revisit inclusion/exclusion criteria documentation
- Ensure logic aligns with theoretical rationale
- Report transparently in methods section

---

## PHASE 5: MANUSCRIPT DEVELOPMENT AND FINALIZATION (Weeks 8–10)

### 5.1 Objectives
- Write complete manuscript meeting publication standards (12–15 pages minimum, 20+ citations)
- Integrate all results tables and figures into narrative
- Ensure APA formatting and academic writing quality
- Generate PDF version

### 5.2 Key Activities

#### Week 8: Manuscript Drafting
1. **Abstract** (Day 1):
   - 150–250 words
   - Background, research question, methods, key findings, conclusion

2. **Introduction** (Days 2–3):
   - Clear research question and significance
   - Theoretical framework (Transaction Cost Economics, Donabedian model, Agency Theory)
   - Literature synthesis (2–3 pages, not mere listing)
   - Hypotheses stated explicitly

3. **Methods** (Days 4–5):
   - Study design and population (1 page)
   - Inclusion/exclusion criteria (0.5 page)
   - Variables and measurement (1–1.5 pages with human-readable labels only)
   - Statistical analysis (1 page)
   - Ethical considerations if applicable

4. **Results** (Days 6–7):
   - Descriptive statistics (Table 1 narrative, 0.5 page)
   - Primary analysis results (narrative integrating Figures 1–2, 1.5–2 pages)
   - Secondary/stratified results (0.5 page)
   - STROBE diagram interpretation

#### Week 9: Revision and Integration
1. **Discussion** (Days 1–3):
   - Interpretation of findings in context of hypotheses (1 page)
   - Comparison to prior literature and theory (2 pages; cite ≥3 prior studies)
   - Implications for practice and policy (0.5 page)
   - Limitations (0.5 page)
   - Future research (0.5 page)

2. **Conclusion** (Day 4):
   - Brief summary of contributions (0.25 page)

3. **References** (Days 5–6):
   - Format all 20+ citations in natbib style
   - Verify all DOIs
   - Sort alphabetically

4. **Full Manuscript Review and Editing** (Days 7–10):
   - Integrate all figures/tables at first point of reference
   - Ensure narrative explains all visual elements
   - Check APA formatting (margins, font, spacing, heading levels)
   - Verify page count (minimum 12–15 pages)
   - Proof for grammar, clarity, coherence

#### Week 10: Finalization and PDF Generation
1. **LaTeX Compilation** (Days 1–3):
   - Compile LaTeX manuscript to PDF using latexmk or pdflatex
   - Troubleshoot compilation errors (missing packages, citation issues)
   - Generate PDF with all graphics embedded

2. **Final Quality Check** (Days 4–5):
   - Verify PDF rendering (no orphaned text, tables fit page width, figures display correctly)
   - Conduct final proofread
   - Ensure manuscript is 12–15+ pages and contains 20+ citations

3. **Final Deliverable** (Days 6–7):
   - Save final PDF to `05-manuscript/manuscript.pdf`
   - Archive source LaTeX files

### 5.3 Deliverables
- [ ] `05-manuscript/manuscript.tex`: Complete LaTeX source manuscript
- [ ] `05-manuscript/manuscript.pdf`: Compiled PDF (12–15+ pages, 20+ citations)
- [ ] `05-manuscript/supplementary/`: Supplementary materials (if applicable)

### 5.4 Quality Gate (Minimum Thresholds)
- **✓ PASS if**:
  - Manuscript is **12–15+ pages** (strict minimum)
  - Contains **≥20 citations** (strict minimum)
  - All figures/tables integrated into narrative with thorough interpretation
  - Introduction includes theory synthesis (not listing)
  - Discussion cites ≥3 prior studies
  - APA formatting verified
  - All variable names converted to human-readable labels (no raw PBJ names in text/tables)
  - PDF compiles without errors
- **✗ FAIL if**:
  - Manuscript <12 pages
  - <20 citations
  - Figures listed at end without narrative integration
  - Bullet-point-only sections (must be verbose prose)
  - Raw PBJ variable names present
  - PDF fails to compile

### 5.5 Resource Requirements
- LaTeX environment with natbib, graphicx, geometry, hyperref packages
- Graphics editing software (if figure refinement needed)
- ~60–80 hours analyst effort (writing, revising, formatting)

### 5.6 Contingency Plans
**If manuscript falls short of page requirement:**
- Expand introduction with more literature synthesis
- Expand discussion with more interpretation and prior-study citations
- Add detailed methods descriptions (less bullet-point style, more prose)
- Extend figure/table captions and narrative interpretation

**If citation count <20:**
- Return to literature review phase to identify additional relevant papers
- Integrate more citations into introduction and discussion
- Target 25+ citations to ensure robust coverage

**If LaTeX compilation fails:**
- Check for package conflicts or missing files
- Rebuild citation bibliography
- Verify all graphic file paths
- Consult LaTeX error log for specific issues

---

## PHASE 6: PRESENTATION PREPARATION (Week 11)

### 6.1 Objectives
- Create professional 10-slide presentation summarizing study
- Use LaTeX Beamer or high-quality PDF format
- Ensure visual appeal and clear communication

### 6.2 Key Activities
1. **Slide 1: Title Slide** (Day 1):
   - Title, authors, institution, date

2. **Slide 2: Research Question and Background** (Day 2):
   - Establish significance and motivation

3. **Slide 3: Theoretical Framework** (Day 2):
   - Briefly present Transaction Cost Economics, Donabedian model

4. **Slide 4: Study Design** (Day 3):
   - Population, time period, sample size

5. **Slide 5: Hypotheses** (Day 3):
   - H1 and H2 with visual predictions (graphs)

6. **Slide 6: Methods Overview** (Day 4):
   - Data source, variables, analysis approach

7. **Slides 7–8: Key Results** (Days 4–5):
   - Figures 1–2 (spline plots) with interpretation
   - Table 1 summary statistics

8. **Slide 9: Discussion and Implications** (Day 6):
   - What do findings mean? Implications for practice/policy

9. **Slide 10: Conclusion and References** (Day 6):
   - Key takeaways + selected citations

### 6.3 Deliverables
- [ ] `presentation/slides.tex`: LaTeX Beamer source (if using Beamer)
- [ ] `presentation/slides.pdf`: Compiled 10-slide presentation

### 6.4 Quality Gate (Minimum Thresholds)
- **✓ PASS if**: 
  - Presentation is ≤10 slides
  - Covers research question, methods, results, discussion, implications
  - Visuals are clear and professional
  - PDF renders without errors
- **✗ FAIL if**: 
  - >10 slides
  - Missing key components (methods, results, discussion)
  - Visuals are unclear or low-resolution

### 6.5 Resource Requirements
- LaTeX Beamer or presentation software
- ~15–20 hours analyst effort

---

## PHASE 7: GIT REPOSITORY INITIALIZATION AND PUBLICATION (Week 12)

### 7.1 Objectives
- Initialize git repository with all study artifacts
- Commit files and push to GitHub
- Ensure public accessibility and reproducibility

### 7.2 Key Activities
1. **Git Repository Setup** (Day 1):
   - Initialize git repository: `git init -b main`
   - Create `.gitignore` excluding LaTeX artifacts (*pdf, *aux, *log, etc.) **except** final manuscript PDF
   - Add all study directories and files

2. **File Organization Verification** (Day 1):
   - Confirm all directories present:
     - `00-project/PROJECT.md`
     - `01-literature/` (review, synthesis, references.bib)
     - `02-research-plan/` (research_plan.md, hypotheses.md, study_roadmap.md)
     - `03-methods/` (methods.md, variables.md, inclusion_criteria.md)
     - `04-analysis/` (scripts, outputs/tables/*.tex, outputs/figures/*.png)
     - `05-manuscript/` (manuscript.pdf, supplementary/)
     - `presentation/` (slides.pdf)
     - `06-publication/` (will contain GitHub files)

3. **Final Commit** (Days 2–3):
   - Stage all files: `git add .`
   - Commit with descriptive message: "Initial commit: Staffing efficiency and economies of scale study"
   - Set git author name/email if needed: 
     ```
     git config user.name "Elwood Research"
     git config user.email "elwoodresearch@gmail.com"
     ```

4. **GitHub Repository Creation** (Day 4):
   - Create GitHub repository in Elwood-Research organization
   - Name: `staffing-efficiency-economies-nursing-homes` (or similar)
   - Initialize with description, README

5. **Push to Remote** (Day 4):
   - Configure remote: `git remote add origin https://github.com/Elwood-Research/[repo-name].git`
   - Push: `git push -u origin main`
   - Verify all files present on GitHub

6. **Repository Finalization** (Day 5):
   - Verify all files are accessible and readable
   - Add README.md in root with study overview
   - Confirm manuscript.pdf is not ignored (explicitly allow in .gitignore)
   - Make repository public

7. **Documentation and Metadata** (Day 5):
   - Add DOI badge (if applicable via Zenodo)
   - Document data access instructions (PBJ data is secure; analysis can be reproduced in Docker vault)

### 7.3 Deliverables
- [ ] `.gitignore`: Configured to exclude LaTeX artifacts except final PDF
- [ ] Git commits on main branch with clear messages
- [ ] GitHub repository public and accessible
- [ ] README.md in repository root
- [ ] All study files committed and pushed to remote
- [ ] `06-publication/`: Contains link/instructions for accessing GitHub repo

### 7.4 Quality Gate (Minimum Thresholds)
- **✓ PASS if**:
  - Git repository initialized on main branch
  - All study files committed
  - Files pushed to GitHub Elwood-Research organization
  - Repository is public
  - Manuscript PDF is present and not ignored
  - README.md describes study and provides access instructions
- **✗ FAIL if**:
  - Repository not initialized or on wrong branch
  - Key files missing (manuscript, tables, figures)
  - Not pushed to GitHub or not public
  - Manuscript PDF is missing

### 7.5 Resource Requirements
- Git and GitHub account
- Command-line experience or Git GUI tool
- ~5–10 hours effort

---

## PHASE 8: PUBLICATION AND DISSEMINATION (Week 12, After Phase 7 Complete)

### 8.1 Objectives
- Publish manuscript and supporting materials to GitHub
- Ensure public accessibility for research reproducibility and transparency

### 8.2 Key Activities
1. **Final Publication Check** (Day 1):
   - Confirm all files on GitHub are correct and complete
   - Test that README and links are functional
   - Verify manuscript PDF is viewable

2. **Announcement** (Day 2):
   - Generate publication notice (if applicable)
   - Provide repository URL and DOI (if assigned via Zenodo)

### 8.3 Deliverables
- [ ] Public GitHub repository with all study materials
- [ ] URL: `https://github.com/Elwood-Research/staffing-efficiency-economies-nursing-homes`

### 8.4 Quality Gate (Minimum Thresholds)
- **✓ PASS if**:
  - Repository publicly accessible
  - All files present and correctly formatted
  - README clearly describes study
  - Manuscript PDF renders correctly on GitHub
- **✗ FAIL if**:
  - Repository not accessible or still private
  - Key files missing
  - Links broken or inaccessible

---

## INTEGRATED TIMELINE (12 WEEKS)

| Week | Phase | Key Milestones | Deliverables |
|------|-------|----------------|--------------|
| **1–2** | **1: Literature Review** | Collect 20+ papers; synthesize findings; verify DOIs | `literature_review.md`, `synthesis.md`, `references.bib` |
| **3** | **2: Research Planning** | Finalize research plan; specify hypotheses; confirm variables | `research_plan.md`, `hypotheses.md`, `variables.md`, `inclusion_criteria.md`, `study_roadmap.md` |
| **4** | **3: Methods** | Develop statistical methodology; plan sensitivity analyses; outline STROBE | `methods.md` |
| **5–7** | **4: Data & Analysis** | Clean data; aggregate; descriptive stats; primary regressions; visualizations | `data_prep.py`, `descriptive_stats.py`, `analysis.py`, `Table1.tex`, Figures 1–3, `results_summary.md` |
| **8–10** | **5: Manuscript** | Draft, revise, finalize manuscript (12–15+ pages, 20+ citations) | `manuscript.tex`, `manuscript.pdf` |
| **11** | **6: Presentation** | Create 10-slide presentation | `slides.pdf` |
| **12** | **7–8: Publication** | Initialize git; commit files; push to GitHub; make public | GitHub repository, public access |

---

## DATA MANAGEMENT AND SECURITY

### Data Privacy Protocols
- **Raw PBJ Data**: Handled only within pbj-analysis-vault Docker container (--network none)
- **Facility-Level Outputs**: Aggregated statistics only; no individual facility rows or resident-level data exported
- **Results**: Only summary tables, regression coefficients, figures with aggregated statistics retained
- **Local Storage**: All analysis outputs stored locally in study directory; no cloud uploads without explicit approval

### HIPAA and Data Governance
- Facility-level data do not contain individually identifiable resident health information (not PHI)
- Nursing home names (PROVNAME) are public; facility provider numbers (PROVNUM) are public
- Analysis performed on aggregated metrics (means, ratios, indices) suitable for publication
- No facility-level raw staffing data retained in outputs

### Backup and Archiving
- Study directory maintained on local secure server
- Git commits provide version control and rollback capability
- GitHub repository serves as remote backup (for non-sensitive study documentation)
- Raw PBJ data remains in secure CMS repository; local copy used only during analysis

---

## QUALITY ASSURANCE CHECKPOINTS

| Checkpoint | Phase | Gate | Verifier | Action if Failed |
|-----------|-------|------|----------|-----------------|
| **Literature Complete** | 1 | ≥20 citations, all DOIs verified | Senior researcher | Expand search; replace missing-DOI papers |
| **Variables Confirmed** | 2 | All required variables in PBJ data | Data analyst | Modify analysis plan or find alternative variables |
| **Sample Size Met** | 4 | ≥7,000 facilities final sample | Data analyst | Relax inclusion criteria; investigate exclusions |
| **Models Converge** | 4 | Primary regressions successful | Statistician | Check for multicollinearity; exclude outliers |
| **Manuscript Length** | 5 | ≥12 pages, ≥20 citations | Senior researcher | Expand sections; add more literature |
| **PDF Compiles** | 5 | LaTeX successful; no errors | Analyst | Debug LaTeX; rebuild bibliography |
| **GitHub Pushed** | 7 | Files on remote; repository public | Analyst | Verify credentials; check internet connection |

---

## CONTINGENCY PLANNING

### Scenario 1: Literature Insufficient
**Trigger**: <15 papers with valid DOIs found in initial search

**Response**:
- Expand database searches (CrossRef, bioRxiv, institutional repositories)
- Include gray literature (CMS reports, health system white papers)
- Broaden search terms to related nursing staffing topics
- Target: Reach 20+ papers within 3 days

---

### Scenario 2: Required Variables Missing
**Trigger**: Key variable (e.g., Hrs_CNA_ctr) not found in PBJ data dictionary

**Response**:
- Confirm absence across all quarters
- Investigate if variable is calculated differently or under alternative name
- Contact CMS data stewards for clarification
- If truly missing, modify analysis plan (alternative outcome specification)
- Example: If contract CNA hours unavailable, use employee CNA hours proportion as proxy

---

### Scenario 3: Exclusion Rate Exceeds Expectations
**Trigger**: Final sample falls below 5,000 facilities (>50% exclusion rate)

**Response**:
- Investigate primary drivers (missing data? outliers?)
- Reconsider inclusion thresholds:
  - Lower minimum census (≥10 vs. ≥20 beds)
  - Relax missingness tolerance (≤15% vs. ≤10%)
  - Include |z| < 4.5 instead of |z| > 4.0 outliers
- Document rationale for revised thresholds
- Report sensitivity to threshold choices in manuscript

---

### Scenario 4: Data Quality Issues
**Trigger**: High levels of implausible values (e.g., 1,000+ RN hours/day)

**Response**:
- Investigate specific facilities (data entry errors vs. legitimate variation)
- Contact data source for verification
- If errors confirmed, exclude affected facility-quarters
- If legitimate but extreme, retain and note in limitations

---

### Scenario 5: Unexpected Null Results
**Trigger**: Primary regressions show no relationship (p > 0.05) or contrary to prediction

**Response**:
- Verify model specification and coding
- Check for data errors or outliers masking true effects
- Examine residual plots for model violations
- Consider alternative functional forms (non-linear to linear; spline to polynomial)
- Conduct sensitivity analyses varying exposure/outcome definitions
- If confirmed, report null result honestly and discuss alternative theoretical explanations

---

### Scenario 6: LaTeX Compilation Failure
**Trigger**: PDF fails to compile; multiple package errors

**Response**:
- Check for missing LaTeX packages; install via tlmgr or apt
- Verify citation database (references.bib) syntax
- Check figure file paths and formats
- Simplify document (remove complex formatting) to isolate error
- Convert to alternative format (HTML, Word) if LaTeX is not recoverable

---

## RISK MITIGATION

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Insufficient literature | Low | Medium | Broad search; include gray literature |
| Data unavailable/incomplete | Low | High | Verify quarters have complete docs before Phase 1 ends |
| Sample size too small | Low–Med | High | Monitor exclusion rates; relax criteria if needed |
| Models fail to converge | Low | Medium | Check assumptions; exclude outliers; reduce parameters |
| Analysis takes longer than expected | Medium | Low | Allocate buffer time; parallelize script execution |
| Manuscript falls short of standards | Low | High | Begin writing early; allow ample revision time |
| Publication delays | Low | Low | Automate git workflow; pre-stage all commits |

---

## RESOURCE SUMMARY

### Personnel
- **Analyst**: 0.3 FTE × 12 weeks = ~150–180 hours
- **Senior Researcher**: 0.1 FTE × 12 weeks = ~30–40 hours (oversight, QA)

### Computing
- Docker pbj-analysis-vault container
- Python 3 with pandas, numpy, scipy, statsmodels, matplotlib
- LaTeX with natbib, Beamer (presentation)
- Git and GitHub

### Data
- PBJ daily staffing data (CY2023Q1–CY2024Q4) from secure CMS repository
- ~40,000–48,000 facility-quarter records
- ~1.5 GB uncompressed data per quarter

### Software and Tools
- All open-source: Python, R, LaTeX, Git, pandas, statsmodels
- No proprietary software licensing fees

---

## AUTHORIZATION AND APPROVAL

- **Approved by**: [Study PI Name]
- **Date**: February 4, 2026
- **Study Status**: Ready to initiate Phase 1 (Literature Review)

---

**End of Study Roadmap**
