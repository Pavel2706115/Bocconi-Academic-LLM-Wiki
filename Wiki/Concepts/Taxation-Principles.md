---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Public-Finance]]"
status: seed
created: 2026-05-18
updated: 2026-05-21
sources:
  - "Raw/Sources/30264 PUBLIC FINANCE/L13_Introduction to taxes.md"
  - "Raw/Sources/30264 PUBLIC FINANCE/L14 L15_Taxation.md"
  - "Raw/Sources/30264 PUBLIC FINANCE/Formulas.md"
source_count: 3
aliases:
  - "Tax Base"
  - "Tax Rates"
  - "Progressivity"
  - "Tax Incidence"
---

# Taxation Principles

## Definition

Taxation is the primary mechanism through which governments raise revenue to finance public goods, redistribute income, and correct market failures. Designing an optimal tax system involves balancing revenue requirements, economic efficiency (minimizing distortions), administrative simplicity, and social equity.

---

## Tax Rates: Average vs. Marginal

To evaluate the efficiency and equity of a tax system, economists analyze two distinct rate definitions:

* **Average Tax Rate ($\bar{t}$)**: The total tax paid divided by total income (or tax base).
  $$ \bar{t} = \frac{T}{Y} $$
* **Marginal Tax Rate ($t'$)**: The tax paid on the next dollar of income.
  $$ t' = \frac{dT}{dY} $$

### Rate Progressivity Dynamics
The relationship between average and marginal tax rates determines how the tax burden shifts as income increases:
$$ \frac{d\bar{t}}{dY} = \frac{d(\frac{T}{Y})}{dY} = \frac{t'Y - T}{Y^2} = \frac{t' - \bar{t}}{Y} $$

* **Progressive**: $\frac{d\bar{t}}{dY} > 0 \implies t' > \bar{t}$ (Average tax rate rises with income).
* **Proportional**: $\frac{d\bar{t}}{dY} = 0 \implies t' = \bar{t}$ (Average tax rate remains constant).
* **Regressive**: $\frac{d\bar{t}}{dY} < 0 \implies t' < \bar{t}$ (Average tax rate falls with income).

---

## Mechanisms for Designing Progressivity

Even with a flat statutory marginal tax rate ($t$), progressivity can be embedded using deductions or credits.

### 1. Progressivity by Tax Credits ($f$)
A tax credit is a direct subtraction from the final tax bill.
$$ T = tY - f $$
* **Marginal Tax Rate**: $t' = t$
* **Average Tax Rate**: 
  $$ \bar{t} = \frac{T}{Y} = t - \frac{f}{Y} \implies \bar{t} < t $$
* **Result**: Because $\bar{t}$ increases as income $Y$ rises ($\frac{d\bar{t}}{dY} = \frac{f}{Y^2} > 0$), the tax is progressive.

### 2. Progressivity by Tax Deductions ($d$)
A tax deduction is a subtraction from taxable income before taxes are calculated.
$$ T = t(Y - d) $$
* **Marginal Tax Rate**: $t' = t$
* **Average Tax Rate**: 
  $$ \bar{t} = \frac{T}{Y} = t - \frac{td}{Y} \implies \bar{t} < t $$
* **Result**: Like the credit, because $\bar{t}$ increases as income $Y$ rises ($\frac{d\bar{t}}{dY} = \frac{td}{Y^2} > 0$), the tax is progressive.

---

## Tax Incidence: Statutory vs. Economic

* **Statutory Incidence**: Who is legally responsible for sending the tax payment to the government.
* **Economic Incidence**: Who actually bears the real economic burden of the tax in the form of changed prices.
* **The Incidence Rule**: The burden of a tax falls on the **less elastic** side of the market, regardless of statutory responsibility.
  * If supply is highly elastic ($\eta_s > \eta_d$) → consumers bear the burden.
  * If demand is highly elastic ($\eta_d > \eta_s$) → producers bear the burden.

---

## Related Concepts

- [[Wiki/Concepts/Tax-Inefficiency|Tax Inefficiency]]
- [[Wiki/Concepts/Income-Redistribution|Income Redistribution]]
- [[Wiki/Concepts/Capital-and-Wealth-Taxation|Capital and Wealth Taxation]]
- [[Wiki/Concepts/Consumption-Taxation|Consumption Taxation]]

