---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Public-Finance]]"
status: seed
created: 2026-05-18
updated: 2026-05-21
sources:
  - "Raw/Sources/30264 PUBLIC FINANCE/L6_Social Insurance.md"
  - "Raw/Sources/30264 PUBLIC FINANCE/Formulas.md"
source_count: 2
aliases:
  - "Welfare State"
  - "Insurance Markets"
---

# Social Insurance

## Definition

Social insurance programs are mandatory, government-provided insurance systems designed to shield individuals against adverse economic shocks (e.g., unemployment, disability, illness, old age). The welfare state intervenes in these sectors because private insurance markets suffer from pervasive market failures—primarily asymmetric information, adverse selection, and moral hazard.

---

## Consumer Utility and Demand for Insurance

Consumers purchase insurance because they are risk-averse, meaning they prefer a certain payout over an uncertain gamble with the same expected value (diminishing marginal utility of wealth).

### 1. Expected Utility without Insurance
In the absence of insurance, if a consumer faces an adverse event with a probability ($p$) that inflicts a loss/damage ($d$) on their initial wage ($w$):
$$EU_{\text{uninsured}} = (1 - p) \times U(w) + p \times U(w - d)$$

Assuming a standard risk-averse utility function $U(w) = \sqrt{w}$:
$$EU_{\text{uninsured}} = (1 - p) \times \sqrt{w} + p \times \sqrt{w - d}$$

### 2. Expected Utility with Insurance
When purchasing insurance, the consumer pays a premium ($r$) to receive a benefit payout ($b$) if the adverse event occurs. 
* Let $r = m \cdot b$, where $m$ is the premium markup rate. Under **actuarially fair pricing** (where the insurer makes zero expected profit), the premium equals the expected payout ($m = p$).
* **Expected Utility with Insurance**:
  $$EU_{\text{insured}} = (1 - p) \times U(w - mb) + p \times U(w - mb - d + b)$$

Assuming $U(w) = \sqrt{w}$:
$$EU_{\text{insured}} = (1 - p) \times \sqrt{w - mb} + p \times \sqrt{w - mb - d + b}$$

* **Optimal Consumption**: If pricing is actuarially fair ($m = p$), a risk-averse individual will choose **full insurance** ($b^* = d$), fully smoothing consumption across both states of nature so that $c_{\text{healthy}} = c_{\text{sick}} = w - pd$.

---

## Why Private Markets Fail

1. **Asymmetric Information & Adverse Selection**:
   * Individuals know their own risk levels better than insurers do.
   * At any given premium, high-risk individuals are more likely to buy insurance than low-risk individuals.
   * If insurers cannot distinguish risk levels, they charge average premiums → healthy people drop out → premiums rise → high-risk spiral leads to market collapse.
   * **Government Remedy**: Mandating universal participation pools risks together, solving the selection collapse.

2. **Moral Hazard**:
   * Insuring individuals against loss reduces their incentive to prevent the adverse event (e.g., being less careful, staying unemployed longer).
   * **Government Trade-off**: The optimal social insurance design must balance the welfare gains from consumption smoothing (coverage) against the deadweight loss of behavioral distortion (reduced incentive to work or avoid risk).

---

## Related Concepts

- [[Wiki/Concepts/Market-Failures|Market Failures]]
- [[Wiki/Concepts/Asymmetric-Information|Asymmetric Information]]
- [[Wiki/Concepts/Healthcare-Economics|Healthcare Economics]]
- [[Wiki/Concepts/Pension-Systems|Pension Systems]]

