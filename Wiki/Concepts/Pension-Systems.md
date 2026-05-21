---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Public-Finance]]"
status: seed
created: 2026-05-18
updated: 2026-05-21
sources:
  - "Raw/Sources/30264 PUBLIC FINANCE/L9 L10 L11_Pension System.md"
  - "Raw/Sources/30264 PUBLIC FINANCE/Formulas.md"
source_count: 2
aliases:
  - "Social Security"
  - "Pay-As-You-Go"
  - "Funded Pension"
---

# Pension Systems

## Definition

Pension systems are public or private frameworks designed to provide financial security and income to individuals after retirement, addressing market failures such as individual myopia (lack of foresight to save) and the absence of private annuity markets (adverse selection).

---

## System Architectures & Mathematical Formulas

Pension designs differ fundamentally based on how they collect contributions and payout benefits.

### 1. Pay-As-You-Go (PAYGO) Systems
In a PAYGO system, current workers' contributions directly finance the benefits of current retirees.

- **Financial Equilibrium**:
  $$P \cdot N_r = \alpha \cdot N_w \cdot w$$
  Where:
  * $P$ is the average pension payment.
  * $N_r$ is the number of retirees.
  * $\alpha$ is the pension contribution rate.
  * $N_w$ is the number of active workers.
  * $w$ is the average wage.

- **PAYGO Rate of Return**:
  The implicit rate of return in a PAYGO system is determined by demographic growth ($n$) and labor productivity/wage growth ($m$):
  $$\text{Implicit Return} = (1 + n)(1 + m) - 1 \approx n + m$$
  The total contribution pool is:
  $$\alpha \cdot W_t = \alpha \cdot W_{t-1} \cdot (1 + n)(1 + m)$$
  Where $W_t$ is total wage bill in period $t$.

- **Benefits Calculation Methods**:
  * **Earnings-Based PAYGO Pension**:
    $$P = L \times w_p \times \beta$$
    Where $L$ is the number of years worked, $w_p$ is a measure of pensionable wage (e.g., average of final years' salary), and $\beta$ is the benefit coefficient (yield rate).
  * **Contribution-Based PAYGO Pension** (e.g., the Italian *Dini* reform):
    Contributions are notionally accumulated over working years at an interest rate indexed to GDP growth. The capitalized sum is then converted into an annuity. For 2 years of contributions $P$:
    $$AV(P) = \frac{P}{1+r_z} + \frac{P}{(1+r_z)^2}$$
    Where $r_z$ is the notional discount/capitalization rate.

### 2. Fully Funded Systems
In a Fully Funded system, each generation's contributions are saved and invested in capital markets. The retirees receive benefits funded by their own past investments plus market returns.

- **Rate of Return**:
  $$\text{Fully Funded Return} = \alpha \cdot W_{t-1} \cdot (1 + i)$$
  Where $i$ is the real capital market interest rate.

- **Aaron-Samuelson Rule**:
  A PAYGO system yields higher welfare than a Funded system if and only if:
  $$g + n > i$$
  Where $g$ is productivity growth ($m$), $n$ is population growth, and $i$ is the capital market interest rate. If interest rates are high ($i > g + n$), Fully Funded systems are superior.

---

## Design and Evaluation Metrics

* **Replacement Ratio**:
  $$\text{Replacement Ratio} = \frac{\text{Pension}}{\text{Salary}}$$
  Measures the percentage of pre-retirement labor income replaced by pension benefits, indicating the level of consumption smoothing achieved.

* **Demographic Challenges**:
  declining birth rates ($n < 0$) and longer life expectancies ($N_r$ increases relative to $N_w$) create a structural funding gap in PAYGO systems, forcing governments to either increase the contribution rate ($\alpha$), raise the retirement age, or reduce the average pension ($P$).

---

## Related Concepts

- [[Wiki/Concepts/Social-Insurance|Social Insurance]]
- [[Wiki/Concepts/Healthcare-Economics|Healthcare Economics]]
- [[Wiki/Concepts/Taxation-Principles|Taxation Principles]]
- [[Wiki/Concepts/Income-Redistribution|Income Redistribution]]
