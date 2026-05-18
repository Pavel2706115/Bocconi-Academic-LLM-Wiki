---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Statistics]]"
  - "[[Wiki/Topics/Management]]"
status: seed
created: 2026-05-18
updated: 2026-05-18
sources:
  - "Raw/Sources/30001 STATISTICS/Lecture 5-6/Lecture 5-6 Slides with NOTES.md"
  - "Raw/Sources/30001 STATISTICS/Lecture 7/Lesson 7 Slides with NOTES.md"
  - "Raw/Sources/30001 STATISTICS/Lecture 8-9/Lecture 8-9 Slides with FULL NOTES.md"
  - "Raw/Sources/30060 MANAGEMENT/Decision Analysis.md"
source_count: 4
aliases:
  - "Random Variables"
  - "Normal Distribution"
---

# Probability Distributions

## Definition

A probability distribution describes all possible values a random variable can take and the probability associated with each value. Distributions are the foundation of statistical inference and decision-making under uncertainty.

## Types of Random Variables

- **Discrete**: countable values (e.g., number of defective items)
- **Continuous**: any value in a range (e.g., height, temperature)
- **Binary/Dichotomous**: only two outcomes (e.g., success/failure)

## Key Distributions

### Discrete
- **Bernoulli**: single trial with probability p of success
- **Binomial**: number of successes in n independent Bernoulli trials
- **Poisson**: count of events in a fixed interval

### Continuous
- **Uniform**: equal probability for all values in a range
- **Normal (Gaussian)**: bell-shaped, symmetric around the mean; described by μ and σ
- **Standard Normal (Z)**: normal with μ=0, σ=1; used for z-scores

## Properties

- All probabilities sum to 1 (discrete) or integrate to 1 (continuous)
- Mean (expected value): E(X) = Σ pᵢxᵢ
- Variance: Var(X) = Σ pᵢ(xᵢ − μ)²

## Related Concepts

- [[Wiki/Concepts/Descriptive-Statistics|Descriptive Statistics]]
- [[Wiki/Concepts/Sampling-and-Central-Limit-Theorem|Sampling and CLT]]
- [[Wiki/Concepts/Conditional-Probability|Conditional Probability]]
- [[Wiki/Concepts/Hypothesis-Testing|Hypothesis Testing]]
