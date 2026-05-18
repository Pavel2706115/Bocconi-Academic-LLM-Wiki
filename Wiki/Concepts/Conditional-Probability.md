---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Management]]"
  - "[[Wiki/Topics/Statistics]]"
status: seed
created: 2026-05-18
updated: 2026-05-18
sources:
  - "Raw/Sources/30060 MANAGEMENT/Decision Analysis.md"
source_count: 1
aliases:
  - "Bayes Rule"
  - "Bayesian Updating"
---

# Conditional Probability

## Definition

Conditional probability is the probability of an event occurring given that another event has already taken place: P(A|B) = P(A∩B) / P(B).

## Key Formulas

- **Conditional**: P(X|Y) = P(X,Y) / P(Y)
- **Joint**: P(X,Y) = P(X|Y) × P(Y)
- **Independence**: if P(X|Y) = P(X), then X and Y are independent
- **Conditional expectation**: E(X|Y) = Σ P(xᵢ|Y) × xᵢ

## Bayesian Updating

1. Start with **prior probability** P(Y)
2. Collect a **signal** S
3. Update to **posterior probability** P(Y|S)
4. Repeat as more signals arrive

## Contingency Tables

Used to display joint and conditional frequencies; marginal frequencies appear as row/column totals.

## Related Concepts

- [[Wiki/Concepts/Probability-Distributions|Probability Distributions]]
- [[Wiki/Concepts/Decision-Analysis|Decision Analysis]]
- [[Wiki/Concepts/Hypothesis-Testing|Hypothesis Testing]]
