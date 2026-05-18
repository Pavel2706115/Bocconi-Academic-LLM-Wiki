---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Statistics]]"
status: seed
created: 2026-05-18
updated: 2026-05-18
sources:
  - "Raw/Sources/30001 STATISTICS/Lecture 17-21/Lecture 17-21 Slides_Hypotheses Testing with SUPERCOMPLETE NOTES.md"
source_count: 1
aliases:
  - "Significance Test"
  - "p-value"
---

# Hypothesis Testing

## Definition

Hypothesis testing is a formal statistical procedure for deciding whether sample data provide sufficient evidence to reject a claim (null hypothesis) about a population parameter.

## Framework

1. **State hypotheses**: H₀ (null) vs H₁ (alternative)
2. **Choose significance level** α (commonly 0.05)
3. **Compute test statistic** from sample data
4. **Find p-value** or compare to critical value
5. **Decision**: reject H₀ if p-value < α

## Key Concepts

- **Type I error** (α): rejecting H₀ when it is true (false positive)
- **Type II error** (β): failing to reject H₀ when it is false (false negative)
- **Power** (1-β): probability of correctly rejecting a false H₀
- **p-value**: probability of observing data as extreme or more extreme, assuming H₀ is true

## Common Tests

| Test | Use |
|------|-----|
| Z-test | Mean with known σ |
| t-test | Mean with unknown σ |
| χ² test | Variance; goodness of fit |
| F-test | Equality of two variances; regression overall significance |

## Related Concepts

- [[Wiki/Concepts/Interval-Estimation|Interval Estimation]]
- [[Wiki/Concepts/Point-Estimation|Point Estimation]]
- [[Wiki/Concepts/Linear-Regression|Linear Regression]] — uses t-tests and F-tests
