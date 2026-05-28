---
tags:
  - concept
topics:
  - "[[Wiki/Topics/Marketing]]"
status: seed
created: 2026-05-29
updated: 2026-05-29
sources:
  - "Raw/Sources/30705 MARKETING/Presentation 3.md"
source_count: 1
aliases:
  - "Demand Estimation and Market Share"
  - "Market Potential"
  - "Potential Gap"
  - "Market Share"
  - "Absolute Market Share"
  - "Relative Market Share"
  - "Penetration Index"
  - "Weighted Coverage Index"
  - "Selection Index"
  - "Customer Portfolio Quality Index"
---

# Demand Estimation and Market Share

## Definition

**Demand Estimation** and **Market Share Analysis** are the primary quantitative tools used in marketing to assess market attractiveness, establish sales targets, and evaluate competitive performance. It distinguishes between **Market Potential** (the theoretical limit of market size) and **Actual Demand**, analyzing the gaps between them.

---

## 1. Calculating Market Potential

Market Potential is the maximum limit of demand in a specific market over a given time frame under maximum industry marketing expenditure.

### A. Nondurable Goods / Services Formula
For consumer goods consumed recurringly (e.g., toothpaste, soft drinks):
$$\text{MktPot}_t = N_t \times P_t \times O_t \times DP_t$$

Where:
*   $N_t$ = Total size of potential consumer population in year $t$
*   $P_t$ = Penetration rate (fraction of population using the product category)
*   $O_t$ = Number of consumption occasions per day or year
*   $DP_t$ = Dose per occasion (quantity consumed each time)

### B. Durable Goods Formula
For capital or durable goods (e.g., washing machines, flat-screen TVs):
$$\text{MktPot}_t = \text{First-Purchase Potential} + \text{Replacement Potential}$$
$$\text{MktPot}_t = (N'_t \times P'_t) + (U_{t-1} \times R'_t)$$

Where:
*   $N'_t$ = New potential purchasers entering the market in year $t$
*   $P'_t$ = Penetration rate of new purchasers
*   $U_{t-1}$ = Cumulative historical stock of users (installed base)
*   $R'_t$ = Replacement rate (determined by average product lifetime)

---

## 2. The Potential Gap

The **Potential Gap** is the difference between Market Potential and Actual Market Demand:

$$\text{Potential Gap} = \text{Market Potential} - \text{Actual Market Demand}$$

It is decomposed into three structural gaps:
1.  **Non-consumer Gap**: Caused by people who do not use the product category due to lack of interest, price barriers, or accessibility issues.
2.  **Occasion Gap**: Consumers use the product, but on fewer occasions than theoretically possible.
3.  **Dose Gap**: Consumers use the product, but in lower quantities per occasion than optimal.
4.  **Competitive Gap**: The portion of the market held by direct competitors (secondary demand).

---

## 3. Market Share Decomposition (Distributor Level)

A company's competitive performance is measured by its **Absolute Market Share ($MS$)** and **Relative Market Share ($RMS$)**:
*   **Absolute Market Share**: $MS = \frac{\text{Company Sales}}{\text{Total Market Sales}}$
*   **Relative Market Share**: $RMS = \frac{\text{Company Market Share}}{\text{Market Share of the Leading Competitor}}$

*   **Sell-in vs. Sell-out**: Sell-in is the volume a manufacturer sells to distributors; sell-out is the volume distributors sell to end consumers. Discrepancies represent inventory changes in the channel.

### The Fundamental Market Share Theorem
For companies selling through commercial intermediaries, Absolute Market Share is decomposed as:

$$MS = \text{Penetration Index} \times \text{Weighted Coverage Index}$$
$$MS = P_i \times C_w$$

Where:
1.  **Penetration Index ($P_i$)**: The company's share of sales within the customer portfolio of the distributors it serves.
    $$P_i = \frac{\text{Sales of the Company}}{\text{Total Sales of the Product Category by Serviced Distributors}}$$
2.  **Weighted Coverage Index ($C_w$)**: Measures the weight (relative size) of the distributors served by the company.
    $$C_w = \frac{\text{Total Sales of the Product Category by Serviced Distributors}}{\text{Total Market Sales of the Product Category}}$$

### Weighted Coverage Decomposition
The Weighted Coverage Index is further broken down to assess distributor selection:
$$C_w = \text{Numerical Coverage} \times \text{Selection Index}$$
$$C_w = C_n \times S_i$$

Where:
*   **Numerical Coverage ($C_n$)**: The fraction of total active distributors that stock the company's product.
    $$C_n = \frac{\text{Number of Serviced Distributors}}{\text{Total Number of Active Distributors in the Market}}$$
*   **Selection Index ($S_i$)**: Evaluates the average size/quality of the company's distributors compared to the market average.
    $$S_i = \frac{\text{Average Category Sales of Serviced Distributors}}{\text{Average Category Sales of All Distributors in the Market}}$$
    *   $S_i > 1$: The company has selected high-volume, key distributors (**Customer Portfolio Quality** is high).
    *   $S_i < 1$: The company's distributors are smaller than the market average.

---

## Related Concepts

- [[Wiki/Concepts/Sustainable-Marketing-and-Trust|Sustainable Marketing and Trust]]
- [[Wiki/Concepts/Marketing-Environment-and-Competition|Marketing Environment and Competition]]
- [[Wiki/Concepts/Pricing-Policies-and-Bundling|Pricing Policies and Bundling]] — Indifference pricing & margins
- [[Wiki/Concepts/Cost-Accounting|Cost Accounting]]
- [[Wiki/Concepts/Break-Even-Analysis|Break-Even Analysis]]
