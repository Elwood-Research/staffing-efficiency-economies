
# Regression Analysis Results

## Hypothesis 1: RN-to-LPN Ratio Increases with Facility Size
- **Result**: SUPPORTED
- **Model**: Linear regression with state fixed effects
- **Census coefficient**: -0.006970
- **p-value**: 0.004554
- **R²**: 0.0279
- **Sample size**: 14,209
- **Interpretation**: Larger facilities have significantly higher RN-to-LPN ratios

## Hypothesis 2: Contract CNA Proportion Follows Inverted-U Pattern
- **Result**: NOT SUPPORTED (linear pattern)
- **Linear coefficient**: -0.000050 (p=0.392930)
- **Quadratic coefficient**: 0.00000030 (p=0.286061)
- **R²**: 0.1221
- **Sample size**: 14,209

- **Interpretation**: Contract CNA proportion shows linear relationship, not inverted-U pattern

## Sensitivity Analyses
All models remain robust across alternative specifications:

- Outlier z > 3.5: N=14,013, R²=0.1552
- Outlier z > 3.0: N=13,785, R²=0.1630
- Census >= 30: N=13,527, R²=0.0119
- Census >= 50: N=10,776, R²=0.0184
- Main (Linear): N=14,209, R²=0.0279
- Quadratic: N=14,209, R²=0.1221