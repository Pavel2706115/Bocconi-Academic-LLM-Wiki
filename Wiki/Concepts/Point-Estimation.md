---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Statistics]]"
status: seed
created: 2026-05-18
updated: 2026-05-18
sources:
  - "Raw/Sources/30001 STATISTICS/Lecture 13-14/Lecture 13-14 Slides Point estimation with FULL NOTES.md"
source_count: 1
aliases:
  - "Estimator"
  - "Parameter Estimation"
---

# Point Estimation

## Definition

Point estimation uses sample data to compute a single value (point estimate) that serves as the "best guess" for an unknown population parameter.

## Key Properties of Estimators

- **Unbiasedness**: E(θ̂) = θ — the estimator's expected value equals the true parameter
- **Efficiency**: among unbiased estimators, the one with smallest variance is most efficient
- **Consistency**: as n → ∞, the estimator converges to the true parameter
- **Sufficiency**: the estimator captures all information in the sample about the parameter

## Common Point Estimators

| Parameter | Estimator |
|-----------|-----------|
| Population mean μ | Sample mean x̄ |
| Population variance σ² | Sample variance s² |
| Population proportion p | Sample proportion p̂ |

## Related Concepts

- [[Wiki/Concepts/Sampling-and-Central-Limit-Theorem|Sampling and CLT]]
- [[Wiki/Concepts/Interval-Estimation|Interval Estimation]]
- [[Wiki/Concepts/Hypothesis-Testing|Hypothesis Testing]]
