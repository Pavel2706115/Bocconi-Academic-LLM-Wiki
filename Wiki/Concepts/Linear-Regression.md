---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Statistics]]"
status: seed
created: 2026-05-18
updated: 2026-05-18
sources:
  - "Raw/Sources/30001 STATISTICS/Lecture 22-24/Lecture 22-24_Simple Linear Regression with FULL NOTES.md"
  - "Raw/Sources/30001 STATISTICS/Lecture 25-27/Lecture 25_27 Slides - Multiple Regression with NOTES up to L26.md"
  - "Raw/Sources/30001 STATISTICS/Lecture 22-24/Computation of b0 and b1 through Least Squares .md"
source_count: 3
aliases:
  - "Regression"
  - "OLS"
  - "Simple Linear Regression"
  - "Multiple Regression"
---

# Linear Regression

## Definition

Linear regression models the relationship between a dependent variable Y and one or more independent variables X. It estimates the best-fitting linear equation using the **Ordinary Least Squares (OLS)** method, minimizing the sum of squared residuals.

## Simple Linear Regression

- Model: Y = β₀ + β₁X + ε
- OLS estimators: b₁ = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²; b₀ = ȳ - b₁x̄
- **R²**: coefficient of determination — proportion of variance in Y explained by X
- **Standard error of estimate**: measures spread of observed values around the regression line

## Multiple Linear Regression

- Model: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε
- **Adjusted R²**: penalizes for adding variables that don't improve the model
- **Multicollinearity**: when independent variables are highly correlated
- **Categorical variables**: included as dummy (indicator) variables

## Inference

- t-test for individual coefficient significance
- F-test for overall model significance
- Confidence intervals for coefficients

## Assumptions (Gauss-Markov)

1. Linearity
2. Independence of errors
3. Homoscedasticity (constant variance of errors)
4. Normality of errors (for inference)
5. No perfect multicollinearity

## Related Concepts

- [[Wiki/Concepts/Hypothesis-Testing|Hypothesis Testing]]
- [[Wiki/Concepts/Descriptive-Statistics|Descriptive Statistics]]
- [[Wiki/Concepts/Financial-Statement-Analysis|Financial Statement Analysis]] — regression used for ratio analysis
