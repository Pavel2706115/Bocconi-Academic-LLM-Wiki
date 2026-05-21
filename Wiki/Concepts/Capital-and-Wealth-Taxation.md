---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Public-Finance]]"
status: seed
created: 2026-05-21
updated: 2026-05-21
sources:
  - "Raw/Sources/30264 PUBLIC FINANCE/L18 L19_Taxes on savings.md"
  - "Raw/Sources/30264 PUBLIC FINANCE/L20 L21_Taxes on risk taking and wealth.md"
  - "Raw/Sources/30264 PUBLIC FINANCE/Formulas.md"
source_count: 3
aliases:
  - "Taxes on Savings"
  - "Estate Tax"
  - "Wealth Taxes"
---

# Capital and Wealth Taxation

## Intertemporal Choice and Savings

Taxing capital income (the return on accumulated savings) alters the price of future consumption relative to current consumption. This is modeled using the intertemporal choice framework.

### The Intertemporal Budget Constraint
An individual lives for two periods: working ($W$) and retired ($R$).
* **Savings ($S$)**: 
  $$S = Y - c^W$$
* **Retired Consumption ($c^R$)**: 
  $$c^R = (1 + r)S = (1 + r)(Y - c^W)$$
* **Combined Budget Constraint**:
  $$c^W + \frac{c^R}{1 + r} = Y$$

Where:
* $Y$ is first-period labor income.
* $c^W$ is consumption while working.
* $c^R$ is consumption while retired.
* $r$ is the net-of-tax real interest rate.

### Income and Substitution Effects of Capital Taxes
A tax on interest income lowers the interest rate from $r$ to $r(1 - t_k)$, steepening the budget line (making future consumption more expensive). The impact on savings is theoretically ambiguous:
1. **Substitution Effect**: Lowering $r$ decreases the reward for saving, making current consumption ($c^W$) cheaper relative to future consumption ($c^R$). This discourages saving.
2. **Income Effect**: Lowering $r$ reduces lifetime wealth, making the individual poorer overall. To maintain consumption in retirement, they must reduce current consumption ($c^W$) and increase savings.
3. **Net Effect**: If the substitution effect dominates, taxes reduce savings. If the income effect dominates, taxes increase savings. Empirical evidence suggests the net interest elasticity of savings is positive but small.

---

## Inflation and Capital Income Taxation

Inflation severely distorts the taxation of savings because capital taxes are historically levied on **nominal** interest rather than **real** interest.

### Real Interest Rate Formula
$$r = \frac{1 + i}{1 + \pi} - 1 \approx i - \pi$$

Where:
* $r$ is the real interest rate.
* $i$ is the nominal interest rate.
* $\pi$ is the inflation rate.

### Tax Distortion Example
Suppose the real interest rate is $2\%$ and inflation is $0\%$, making the nominal interest rate $2\%$. A $50\%$ tax rate on nominal interest yields:
* Tax paid: $50\% \times 2\% = 1\%$ of asset value.
* Net-of-tax real return: $2\% - 1\% = 1\%$. Effective tax rate on real return is $50\%$.

Now suppose inflation rises to $10\%$, pushing the nominal interest rate to $12\%$ to maintain a $2\%$ pre-tax real return ($12\% - 10\% = 2\%$). The same $50\%$ tax rate yields:
* Tax paid: $50\% \times 12\% = 6\%$ of asset value.
* Net-of-tax nominal return: $12\% - 6\% = 6\%$.
* Net-of-tax real return: $6\% - 10\% = -4\%$.
* The effective tax rate on the real return is $300\%$ (tax paid is $6\%$ on a real return of $2\%$). Inflation combined with nominal-based capital taxes results in negative real returns, actively eroding wealth.

---

## Alternative Behavioral Saving Models

Traditional theory assumes perfect rationality, but empirical savings behavior is better explained by behavioral economics:
* **Precautionary Savings & Buffer Stocks**: Individuals save to protect against unexpected liquidity constraints (e.g., job loss), leading to "buffer stock" saving behavior rather than lifetime consumption smoothing.
* **Self-Control & Behavioral Models**: Individuals suffer from present bias. Saving requires self-control.
* **Commitment Devices & Defaults**: Policies like automatic enrollment in 401(k) plans (default options) dramatically boost participation rates compared to active choices, proving that friction and behavioral nudges shape saving more than net interest rates.

---

## Taxation and Risk-Taking

A primary concern of capital taxation is its potential to suppress entrepreneurial risk-taking.

### Symmetrical Taxation (Domar-Musgrave Model)
If the government taxes investment returns at rate $t$ but provides a **symmetric full offset** (allowing investors to deduct $100\%$ of losses against other income):
* The government becomes a silent partner, sharing both the upside and downside risk.
* Investors can fully undo the tax's effect on their portfolio risk by scaling up their holdings of the risky asset.
* Therefore, a symmetric capital tax does not necessarily reduce aggregate risk-taking and can theoretically increase it.

### Real-World Asymmetries
In practice, full offsets are rarely permitted due to evasion concerns and fiscal constraints:
* **Loss Limitations**: Governments place caps on capital loss deductions or restrict them to offsetting capital gains only.
* **Progressive Taxes**: If tax brackets are progressive, positive returns are taxed at higher rates than the savings shield provided by negative returns.
* **Net Effect**: Under asymmetric taxation, capital taxes suppress risk-taking.

---

## Wealth and Transfer Taxes

Rather than taxing the annual return on capital, wealth taxes levy charges directly on the stock of accumulated assets.

### 1. Estate and Gift (Transfer) Taxes
* **Definitions**: 
  * **Gift Tax**: Tax on assets transferred between living individuals.
  * **Estate Tax**: Tax on the assets of the deceased bequeathed to others.
* **Arguments For**: Highly progressive (concentrated at the top of the wealth distribution), reduces the formation of entrenched wealth dynasties, and encourages heirs to work rather than live off inherited wealth.
* **Arguments Against**: Moral arguments (termed a "death tax"), double taxation (assets taxed as income when earned, and again at death), and administrative avoidance. It is often called a "voluntary tax" because the ultra-wealthy utilize legal trust funds to bypass it entirely.
* **Demographics**: In the US, approximately $98\%$ of estates owe zero estate tax. Italy has one of the lowest inheritance tax revenues in Europe due to very high exemptions and low rates.

### 2. Property Taxes
* **Definition**: A tax levied on the assessed value of real estate (land and structures).
* **Significance**: Property taxes are the primary source of revenue for local governments. Because real estate is the largest saving vehicle for the average household, property taxes heavily influence saving decisions.

### 3. Net Wealth Taxes
* While popular in public debate, annual net wealth taxes have been largely abandoned in Europe (e.g., abolished in France, Sweden, Denmark) due to valuation difficulties, capital flight, and high compliance costs. The global trend has shifted toward taxing realized capital gains and wealth transfers (inheritance).

---

## Related Concepts

- [[Wiki/Concepts/Taxation-Principles|Taxation Principles]]
- [[Wiki/Concepts/Tax-Inefficiency|Tax Inefficiency]]
- [[Wiki/Concepts/Social-Insurance|Social Insurance]]
- [[Wiki/Concepts/Pension-Systems|Pension Systems]]
