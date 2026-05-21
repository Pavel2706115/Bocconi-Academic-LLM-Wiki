---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Financial-Markets-and-Institutions]]"
status: seed
created: 2026-05-21
updated: 2026-05-21
sources:
  - "Raw/Sources/Economics PDF Books/The-Intelligent-Investor-Excerpt.md"
  - "Raw/Sources/Economics PDF Books/EMH-Professional-Status.md"
source_count: 2
aliases:
  - "EMH"
  - "Market Efficiency"
  - "Joint Hypothesis Problem"
---

# Efficient Market Hypothesis (EMH)

The **Efficient Market Hypothesis (EMH)** is an academic theory asserting that financial market prices fully and instantaneously reflect all available information. Under this hypothesis, it is impossible for an investor to consistently earn abnormal (risk-adjusted) returns, as assets are always priced at their fair value, rendering both fundamental and technical analysis ineffective at generating alpha.

---

> [!NOTE] Ingested Sources & Original PDF Materials
> * **Related Book**: [[Wiki/Books/The-Intelligent-Investor|The Intelligent Investor]]
> * **Book Source & File**: [[Raw/Sources/Economics PDF Books/The-Intelligent-Investor-Excerpt|The Intelligent Investor Excerpt (Raw Source)]] | [[Raw/Files/Economics PDF Books/The_intelligent_investor.pdf|The_intelligent_investor.pdf (Original PDF)]]
> * **Academic Paper Source & File**: [[Raw/Sources/Economics PDF Books/EMH-Professional-Status|EMH & Professional Status (Raw Source)]] | [[Raw/Files/Economics PDF Books/most_similar_papers_to_this_one/The_Efficient_Market_Hypothesis_theFinan.pdf|The_Efficient_Market_Hypothesis_theFinan.pdf (Original PDF)]]

---

## 1. The Three Forms of Market Efficiency
Eugene Fama (1970) formalized the EMH by defining the information sets reflected in asset prices. He categorized efficiency into three distinct levels:

```
┌─────────────────────────────────────────────────────────┐
│                    STRONG FORM                          │
│  (All information: Past prices + Public + Insider)     │
│   ┌─────────────────────────────────────────────────┐   │
│   │               SEMI-STRONG FORM                  │   │
│   │   (Public information: Past prices + Earnings)  │   │
│   │   ┌─────────────────────────────────────────┐   │   │
│   │   │               WEAK FORM                 │   │   │
│   │   │  (Historical trading data: Prices)      │   │   │
│   │   └─────────────────────────────────────────┘   │   │
│   └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### Weak-Form Efficiency
*   **Information Set**: All historical price and volume data.
*   **Implication**: Future price movements cannot be predicted using past price patterns. Therefore, **technical analysis** (charting) is useless.
*   **Empirical Tests**: Serial correlation tests and run tests show that price changes are essentially a random walk.

### Semi-Strong-Form Efficiency
*   **Information Set**: All publicly available information (historical price data, corporate financial statements, earnings reports, dividend announcements, macroeconomic news).
*   **Implication**: Prices adjust instantaneously to new public disclosures. Therefore, **fundamental analysis** (evaluating balance sheets and industry trends) cannot consistently generate abnormal returns.
*   **Empirical Tests**: Event studies (e.g., measuring stock price reactions immediately following stock splits or earnings announcements) confirm extremely fast adjustment times.

### Strong-Form Efficiency
*   **Information Set**: All information, both public and private (insider/proprietary information).
*   **Implication**: Even corporate insiders with non-public material information cannot consistently earn abnormal profits.
*   **Empirical Tests**: Studies on corporate insider trading and specialist returns generally reject strong-form efficiency, showing that insiders do earn abnormal returns before their trades are disclosed.

---

## 2. Theoretical Challenges & Practical Limitations

### The Joint Hypothesis Problem
A major methodological issue in testing EMH is that any test of market efficiency is simultaneously a test of the asset pricing model used to calculate risk-adjusted returns (e.g., CAPM).
*   If a study finds that an investment strategy consistently beats the market, it is impossible to know whether the market is genuinely inefficient or if the asset pricing model failed to properly adjust for the risk of the strategy.

### Behavioral Finance Counterarguments
Modern financial economists (such as Robert Shiller and Richard Thaler) argue that stock markets are subject to systematic behavioral biases that violate EMH:
*   **Overreaction and Underreaction**: Investors tend to overreact to dramatic news (causing stocks to become underpriced/overpriced) and underreact to gradual changes.
*   **Herd Behavior**: Investors often copy the actions of others, leading to speculative bubbles and crashes.
*   **Limits to Arbitrage**: Rational investors cannot always exploit mispricings because of liquidity constraints, short-sale restrictions, or high transaction costs.

---

## 3. Related Concepts

*   [[Wiki/Concepts/Stock-Markets|Stock Markets]] — Contextualizes EMH within actual exchange mechanics and active vs. passive debates.
*   [[Wiki/Concepts/Index-Investing|Index Investing]] — Passive indexation is the logical investment strategy under EMH.
*   [[Wiki/Concepts/Value-Investing|Value Investing]] — Active value strategy, which assumes markets are inefficient and prices diverge from intrinsic values.
*   [[Wiki/Concepts/CAPM|CAPM]] — The equilibrium pricing model commonly paired with EMH to test efficiency.
