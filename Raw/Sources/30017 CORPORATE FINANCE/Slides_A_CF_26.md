---
course: Corporate Finance
course_code: 30017
tags:
  - "source"
  - course_30017
Title: "Corporate Finance 30017 - Slides A"
Reference: "Course Material"
Created: 2026-05-18
Processed: true---

---
# Corporate Finance 30017 - Slides A

## Overview of Course Content
*   **Part A: Investment decisions and instruments** (Sessions 1 - 8)
*   **Part B: Risk and Return** (Sessions 9 - 16)
*   **Part C: Capital Structure** (Sessions 17 - 24)

---

## Session 1: Kick Off
### Corporate Investment and Financing Decisions
*   **Investment Decisions:** Defined as the purchase of real assets (tangible: machines, factories; intangible: patents, brands) used as inputs to produce goods and services and generate cash flows.
*   **Financing Decisions:** How a firm pays for its investments. Financial markets allow firms to sell financial claims on real assets and their cash flows (e.g., bank loans, issuing bonds, or equity). Ultimately, it is the sale of a financial asset.
*   **Capital Structure Decision:** The choice between debt and equity financing. 
    *   **Debt:** Promise to pay back with fixed interest. Returns are known but subject to default risk.
    *   **Equity:** Shareholders are entitled to a fraction of dividends but are not guaranteed a fixed return.

### The Corporation and Financial Manager
*   **Corporation:** A legal entity owned by shareholders. It can make contracts, borrow/lend, and must pay taxes. Separation of ownership and management means shareholders elect a Board of Directors to supervise management.
*   **Goal of the Corporation:** Maximizing market value (shareholder value). This aligns the interests of different shareholders (who can manage personal risk via efficient financial markets).
*   **Opportunity Cost of Capital:** The expected return shareholders could obtain by investing their cash in financial markets at the same level of risk. 
    *   *Rule:* Pursue an investment project if its rate of return is greater than the opportunity cost of capital.

---

## Session 2: What Do Real Firms Look Like?
### Financial Data and WRDS
*   **WRDS (Wharton Research Data Services):** Aggregates financial data (Compustat, CRSP, FactSet, etc.) into a standard format. 
*   **CRSP:** Provides stock price data for US firms. Variable `prc` typically denotes the closing stock price.
*   **Stock Returns:** Must adjust for stock splits and dividends. 
    *   Return without split adjustment: $R_1 = \frac{P_1 - P_0}{P_0}$
    *   Return with $x$-for-$y$ stock split: $R_1 = \frac{\frac{x}{y} P_1 + D_1 - P_0}{P_0}$
*   Firms perform stock splits to increase liquidity/accessibility, improve market perception, and trigger psychological effects for retail investors.

### Industry Categorization and Identifiers
*   **Why Categorize?** Useful for benchmarking performance/valuation and finding comparable firms for calculating the opportunity cost of capital.
*   **Classification Systems:** SIC, NAICS, Fama-French, GICS, NACE. 
*   **Market Structure:** Industries differ in firm concentration due to barriers to entry (fixed costs, regulation) and competition (monopolies/oligopolies vs. fragmented markets).

**Financial Data Identifiers:**
*   **Company Name / Ticker:** Terrible identifiers (change frequently, reused).
*   **CUSIP / SEDOL / ISIN:** So-so identifiers (regional constraints, changes during mergers).
*   **CIK:** Great identifier for US firms (SEC filings).
*   **CRSP PERMNO / PERMCO:** Perfect identifiers for US securities/companies. Never reassigned.
*   **Compustat GVKEY:** Almost perfect global identifier.

---

## Session 4: NPV and Investment Decisions
### Present Value (PV) and Future Value (FV)
*   $FV = PV \times (1 + r)^T$
*   $PV = \frac{FV}{(1 + r)^T}$
*   **Net Present Value (NPV):** $NPV = PV - \text{Investment Cost}$
*   *Rule:* Invest if $NPV > 0$. The discount rate $r$ should reflect the risk of the project (opportunity cost of capital).

### Internal Rate of Return (IRR)
*   The discount rate that makes $NPV = 0$. 
*   *Rule:* Invest if $IRR > r$ (opportunity cost of capital).
*   **Pitfalls of IRR:**
    1.  **Lending or Borrowing:** Fails when NPV increases as the discount rate increases (borrowing projects).
    2.  **Multiple Rates of Return:** Cash flows with multiple sign changes can have multiple IRRs, or no IRR at all.
    3.  **Mutually Exclusive Projects:** Ignores the magnitude of the project.
    4.  **Term Structure Assumption:** Assumes the discount rate is constant over time.

### Practical Capital Budgeting
1.  **Inflation:** Treat consistently. Discount nominal cash flows with nominal rates, and real cash flows with real rates. 
    *   $1 + r_{real} = \frac{1 + r_{nominal}}{1 + \text{inflation rate}}$
2.  **Depreciation Tax Shield:** Depreciation reduces taxable income. Tax Shield = Depreciation $\times$ Corporate Tax Rate.
3.  **Working Capital:** The *change* in Net Working Capital (NWC) is a cash flow. Increases in inventory/receivables drain cash (negative CF), while increases in payables retain cash (positive CF).

---

## Session 5: Fixed Income Instruments
### Valuing Bonds
*   Bonds pay a fixed stream of cash flows (coupons + face value).
*   $PV = \sum \frac{Coupon}{(1+r)^t} + \frac{Face Value}{(1+r)^T}$
*   Bond prices and yields are inversely related.

### Spot Rates and Forward Rates
*   **Spot Rate ($r_t$):** The interest rate today on a zero-coupon bond that pays in $t$ periods. Spot rates are the "atoms" for discounting cash flows.
*   **Forward Rate ($f_{T-t, t}$):** The interest rate fixed today on a bond bought in the future. Derived using no-arbitrage:
    *   $(1+r_T)^T = (1+r_{T-t})^{T-t} \times (1+f_{T-t,t})^t$
*   **Yield Curve:** A plot of the term structure of interest rates. Typically slopes upward due to expectations of higher future short-term rates, interest rate risk, and inflation risk.

### Credit Risk and Yield Spread
*   **Default Risk:** The risk that the issuer fails to make promised payments. Rated by agencies (Investment Grade vs. Junk Bonds).
*   **Yield Spread:** The difference in yield between a corporate bond and the risk-free rate (e.g., US Treasury Bill). Equal to the Credit Risk Premium.

---

## Session 6: Equity Instruments
### Markets and Trading
*   **Primary Markets:** Sale of new shares to raise capital.
*   **Secondary Markets:** Trading existing shares (Exchanges like NYSE, or Dealer markets like NASDAQ).
*   **Instruments:** Common stock (voting + cash flow rights), Preferred stock (cash flow rights, higher priority, usually no voting rights), ADRs (foreign stocks trading in US markets).

### Dividend Discount Model (DDM)
*   $P_0 = \sum_{t=1}^{\infty} \frac{DIV_t}{(1+r)^t}$
*   **Constant Growth DDM (Gordon Growth Model):** $P_0 = \frac{DIV_1}{r - g}$
*   **Estimating Growth ($g$):** $g = \text{Plowback Ratio} \times ROE$
    *   Where Plowback Ratio = $1 - \text{Payout Ratio}$ (Fraction of earnings reinvested).

### Present Value of Growth Opportunities (PVGO)
*   $P_0 = \frac{EPS}{r} + PVGO$
*   The firm's value is the PV of earnings under a no-growth policy plus the PV of future growth opportunities.
*   **Growth vs. Income Stocks:** Growth stocks have a high PVGO component; income stocks pay established, stable dividends.

### Free Cash Flow Valuation
*   Instead of dividends per share, value the entire equity/enterprise using Free Cash Flow (FCF).
*   $PV = \sum \frac{FCF_t}{(1+r)^t} + \frac{\text{Horizon Value}}{(1+r)^H}$
*   Horizon Value (Terminal Value) is often estimated using the constant growth model from year $H$ onwards.


## Related Notes
- [[Slides_C_CF_26]]
- [[Frederic S. Mishkin_ Stanley Eakins - Financial Markets and Institutions-Pearson (2018)]]
- [[Libby_12e_Chap012_PPT print]]
- [[Full-material presentation Chapter 10]]
- [[L16 & L17 Expectations Financial Markets Bonds]]
