---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Financial-Markets-and-Institutions]]"
  - "[[Wiki/Topics/Corporate-Finance]]"
status: seed
created: 2026-05-18
updated: 2026-05-18
sources:
  - "Raw/Sources/30017 CORPORATE FINANCE/Slides_A_CF_26.md"
  - "Raw/Sources/30006 FINANCIAL MARKETS AND INSTITUTIONS/Lectures/Lect4.md"
  - "Raw/Sources/30006 FINANCIAL MARKETS AND INSTITUTIONS/Lectures/Lect5.md"
source_count: 3
aliases:
  - "Bond Pricing"
  - "Yield Curve"
  - "Fixed Income"
---

# Bond Valuation

## Definition

A bond is a fixed-income security that pays a stream of coupon payments plus face value at maturity. Bond valuation determines the present value of these future cash flows.

## Valuation Formula

PV = Σ Coupon/(1+r)^t + Face Value/(1+r)^T

## Key Relationships

- Bond prices and yields are **inversely related**
- When coupon rate = yield → bond trades at **par**
- When coupon rate > yield → bond trades at **premium**
- When coupon rate < yield → bond trades at **discount**

## Spot Rates and Forward Rates

- **Spot rate (rₜ)**: yield on a zero-coupon bond maturing at time t
- **Forward rate (f)**: implied future interest rate derived from spot rates
- No-arbitrage: (1+rT)^T = (1+rₜ)^t × (1+f)^(T−t)

## Credit Risk

- **Default risk**: rated by agencies (Moody's, S&P, Fitch)
- **Investment grade** vs **Junk/High-yield** bonds
- **Yield spread**: corporate yield − risk-free rate = credit risk premium

## Related Concepts

- [[Wiki/Concepts/Interest-Rates|Interest Rates]]
- [[Wiki/Concepts/Net-Present-Value|Net Present Value]]
- [[Wiki/Concepts/Equity-Valuation|Equity Valuation]]
- [[Wiki/Concepts/Expectations-in-Macro|Expectations in Macro]] — expectations affect bond prices
