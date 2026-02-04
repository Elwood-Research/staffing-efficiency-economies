# PDF Recompilation Instructions

## Status

⚠️ **IMPORTANT**: The `.tex` source files have been corrected and committed to git, but the `.pdf` files need to be recompiled to reflect these changes.

### What Was Corrected in .tex Files
1. ✅ U-shaped pattern for H2 (contract CNA) - documented with specific percentages
2. ✅ Removed "highly significant" / "not significant" language from p-values
3. ✅ All page fitting requirements maintained

### What Still Needs to Be Done
❌ The `.pdf` files must be **recompiled** from the corrected `.tex` files

---

## Why This Matters

The current PDF files in the repository were compiled from earlier versions of the .tex files. While the source `.tex` files now contain all corrections, the rendered `.pdf` files do not yet reflect these changes.

**Current Status:**
- ✅ `05-manuscript/manuscript.tex` - **CORRECTED** (contains U-shape, objective p-value language)
- ❌ `05-manuscript/manuscript.pdf` - **OUTDATED** (needs recompilation)
- ✅ `presentation/slides.tex` - **CORRECTED** (contains U-shape, objective language)
- ❌ `presentation/slides.pdf` - **OUTDATED** (needs recompilation)

---

## How to Recompile the PDFs

### Option 1: On a Linux/Mac System with LaTeX Installed

#### Compile the Manuscript

```bash
cd 05-manuscript/
pdflatex -interaction=nonstopmode manuscript.tex
bibtex manuscript
pdflatex -interaction=nonstopmode manuscript.tex
pdflatex -interaction=nonstopmode manuscript.tex
cd ..
```

#### Compile the Presentation

```bash
cd presentation/
pdflatex -interaction=nonstopmode slides.tex
pdflatex -interaction=nonstopmode slides.tex
cd ..
```

#### Commit the Updated PDFs

```bash
git add 05-manuscript/manuscript.pdf presentation/slides.pdf
git commit -m "Recompile PDFs from corrected .tex files (U-shape H2 finding, objective p-value language)"
git push origin main
```

---

### Option 2: Using Docker (if LaTeX is not installed locally)

#### Compile Using Docker Container

```bash
# Compile Manuscript
docker run --rm \
  -v $(pwd)/05-manuscript:/work \
  -w /work \
  texlive/texlive:latest \
  bash -c "pdflatex -interaction=nonstopmode manuscript.tex && bibtex manuscript && pdflatex -interaction=nonstopmode manuscript.tex && pdflatex -interaction=nonstopmode manuscript.tex"

# Compile Presentation
docker run --rm \
  -v $(pwd)/presentation:/work \
  -w /work \
  texlive/texlive:latest \
  bash -c "pdflatex -interaction=nonstopmode slides.tex && pdflatex -interaction=nonstopmode slides.tex"

# Commit the Updates
git add 05-manuscript/manuscript.pdf presentation/slides.pdf
git commit -m "Recompile PDFs from corrected .tex files (U-shape H2 finding, objective p-value language)"
git push origin main
```

---

### Option 3: Using Overleaf (Web-Based LaTeX)

1. Create an account at [Overleaf.com](https://www.overleaf.com)
2. Create a new blank project
3. Upload the corrected files from the repository:
   - `05-manuscript/manuscript.tex`
   - `01-literature/references.bib`
   - All figures from `04-analysis/outputs/figures/`
4. Compile the project
5. Download the generated `manuscript.pdf`
6. Replace the PDF file in the repository

---

## Verification Checklist

After recompiling, verify that the PDFs contain the corrections:

### For Manuscript PDF
- [ ] Open `05-manuscript/manuscript.pdf`
- [ ] Go to Abstract (page 1)
  - Should say "Contract CNA proportions exhibited a U-shaped pattern"
- [ ] Go to Results section (around page 5-6)
  - Should show "6.9% ... 5.4% ... 6.2%" (specific percentages)
  - Should NOT say "flat relationship"
  - Should NOT say "highly significant" or "not significant"
- [ ] Search PDF for "U-shaped" - should find multiple instances
- [ ] Search PDF for "highly" - should find 0 instances

### For Presentation PDF
- [ ] Open `presentation/slides.pdf`
- [ ] Go to Slide 7 (H2 Results)
  - Title should say "U-SHAPED PATTERN OBSERVED"
  - Should list "Small facilities: 6.9%", "Mid-sized: 5.4%", "Large: 6.2%"
- [ ] Go to Slide 6 (H1 Results)
  - Should say "p-value: 0.005" (not "p-value: 0.005 (highly significant)")
- [ ] Search PDF for "highly" - should find 0 instances

---

## What Each Change Looks Like

### Change 1: U-Shaped Pattern

**BEFORE (old .tex, old .pdf):**
> "Contract CNA proportions showed no association with facility size... flat relationship... contradicting the predicted inverted-U pattern"

**AFTER (corrected .tex and newly compiled .pdf):**
> "Contract CNA proportions exhibited a U-shaped pattern with facility size: smaller facilities (census <50) and larger facilities (census >150) employed contract CNAs at rates of approximately 6.9% and 6.2% respectively, while mid-sized facilities (census 60–90) maintained contract reliance at 5.4%, representing the lowest proportion."

### Change 2: P-Value Language

**BEFORE (old .tex, old .pdf):**
> "p-value: 0.005 (highly significant)"
> "Linear term: p = 0.393, not significant"

**AFTER (corrected .tex and newly compiled .pdf):**
> "p-value: 0.005"
> "Linear term: p = 0.393"

---

## Why PDFs Weren't Auto-Updated

The environment used for this project does not have LaTeX installed directly, and Docker compilation attempts timed out due to the large size of TeX Live package installations. Therefore, the PDFs must be recompiled in an environment where LaTeX is available (your local machine, Overleaf, or a properly-configured Docker image).

---

## Status Summary

| Item | Status | Notes |
|------|--------|-------|
| `.tex` files corrected | ✅ **DONE** | Committed and pushed to GitHub |
| PDF files recompiled | ❌ **PENDING** | Requires LaTeX environment |
| Git commits | ✅ **DONE** | All changes tracked in source files |
| Ready for peer review | ⚠️ **CONDITIONAL** | Ready once PDFs are recompiled |

---

## Questions?

If you have any questions about the corrections or need help recompiling, please refer to:
- `CORRECTIONS_SUMMARY.md` - Detailed explanation of each change
- `README.md` - Overall study documentation
- Git commit history - Track all changes with `git log`

---

**Next Steps:**
1. Recompile PDFs using one of the three methods above
2. Verify PDFs contain corrections (use checklist above)
3. Commit and push updated PDFs to GitHub
4. Study is ready for peer review
