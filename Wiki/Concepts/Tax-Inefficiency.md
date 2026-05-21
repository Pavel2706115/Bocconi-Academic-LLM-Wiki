---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Public-Finance]]"
status: seed
created: 2026-05-18
updated: 2026-05-21
sources:
  - "Raw/Sources/30264 PUBLIC FINANCE/L16 L17_Tax Inefficiencies.md"
  - "Raw/Sources/30264 PUBLIC FINANCE/Formulas.md"
source_count: 2
aliases:
  - "Deadweight Loss"
  - "Excess Burden"
---

# Tax Inefficiency

## Definition

All taxes (except lump-sum taxes) distort relative prices, inducing individuals and firms to alter their behavior (e.g., working less, consuming less). This behavioral distortion generates **Deadweight Loss (DWL)** (or *excess burden*) — a reduction in social surplus that exceeds the revenue raised by the government.

---

## Deadweight Loss & Elasticities

The efficiency cost of a tax is measured by the size of the behavioral change relative to the tax rate.

### 1. The Deadweight Loss Formula
$$DWL = -\frac{1}{2} \times \Delta Q \times \tau$$
Where:
* $\Delta Q$ is the change in equilibrium quantity caused by the tax.
* $\tau$ is the size of the tax.

### 2. Supply and Demand Elasticity Formulas
The magnitude of $\Delta Q$ is driven by market responsiveness, defined by elasticities:
* **Supply Elasticity ($\eta_s$)**:
  $$\eta_{s} = \frac{\Delta Q}{\Delta P} \times \frac{P}{Q}$$
* **Demand Elasticity ($\eta_d$)**:
  $$\eta_{d} = \frac{\Delta Q}{\Delta P + \tau} \times \frac{P}{Q}$$

Where $P$ is the pre-tax price, $Q$ is the pre-tax quantity, and $\Delta P$ is the change in price.

### 3. The Harberger Triangle (Quadratic Distortions)
By combining elasticities, the DWL formula can be approximated as:
$$DWL \approx \frac{1}{2} \times \eta \times \frac{Q}{P} \times \tau^2$$
* **Key Distortions Rule**: Distortions are **quadratic** in the tax rate ($\tau^2$). Doubling a tax rate quadruples the deadweight loss, meaning that a system with moderate, flat tax rates is vastly more efficient than a system with high, highly variable rates.
* **Elasticity Influence**: DWL is directly proportional to elasticities. Taxing highly elastic markets leads to large behavioral shifts ($\Delta Q$) and high DWL.

---

## Optimal Commodity Taxation: The Ramsey Rule

The Ramsey optimal taxation framework calculates the tax rates on commodity goods that minimize aggregate DWL while meeting a public revenue requirement.

* **Marginal Efficiency Rule**:
  To minimize DWL, the marginal deadweight loss per dollar of marginal revenue raised ($MR$) must be equalized across all taxed commodities ($i$):
  $$\frac{MDWL_{i}}{MR_{i}} = \lambda$$
  Where $\lambda$ represents the marginal social cost of raising revenue.

* **The Inverse Elasticity Rule**:
  Assuming zero cross-price elasticities, this rule implies that optimal tax rates ($\tau_i^*$) are inversely proportional to the elasticity of demand:
  $$\tau_{i}^{*} = -\frac{1}{\eta_{i}} \times \lambda$$
  * **Implication**: Goods with highly inelastic demand (e.g., insulin, basic food) should be taxed at higher rates to minimize deadweight loss. This highlights a fundamental conflict between efficiency (taxing inelastic goods is efficient) and vertical equity (taxing inelastic goods is highly regressive).

---

## Related Concepts

- [[Wiki/Concepts/Taxation-Principles|Taxation Principles]]
- [[Wiki/Concepts/Consumption-Taxation|Consumption Taxation]]
- [[Wiki/Concepts/Capital-and-Wealth-Taxation|Capital and Wealth Taxation]]
- [[Wiki/Concepts/Market-Failures|Market Failures]] — Pigouvian taxes correct DWL instead of creating it

