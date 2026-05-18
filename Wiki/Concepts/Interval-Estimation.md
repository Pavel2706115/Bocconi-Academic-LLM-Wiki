---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Statistics]]"
status: seed
created: 2026-05-18
updated: 2026-05-18
sources:
  - "Raw/Sources/30001 STATISTICS/Lecture 15-16/Lecture 15-16 Interval Estimation with FULL NOTES.md"
source_count: 1
aliases:
  - "Confidence Interval"
  - "CI"
---

# Interval Estimation

## Definition

Interval estimation provides a range of plausible values for a population parameter, along with a confidence level indicating how often the method produces intervals that contain the true parameter.

## Confidence Interval Formula

**CI = point estimate ± margin of error**

- For mean (σ known): x̄ ± z_(α/2) · σ/√n
- For mean (σ unknown): x̄ ± t_(α/2, n-1) · s/√n
- For proportion: p̂ ± z_(α/2) · √(p̂(1-p̂)/n)

## Key Concepts

- **Confidence level** (1-α): typically 90%, 95%, or 99%
- **Margin of error**: half-width of the interval; decreases with larger n
- **Interpretation**: if we repeated the sampling procedure many times, (1-α)% of intervals would contain the true parameter

## Sample Size Determination

- n = (z_(α/2) · σ / E)² for means, where E is desired margin of error
- Larger confidence levels and smaller margins of error require larger samples

## Related Concepts

- [[Wiki/Concepts/Point-Estimation|Point Estimation]]
- [[Wiki/Concepts/Hypothesis-Testing|Hypothesis Testing]]
- [[Wiki/Concepts/Sampling-and-Central-Limit-Theorem|Sampling and CLT]]
