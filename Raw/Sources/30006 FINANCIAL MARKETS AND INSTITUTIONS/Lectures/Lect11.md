---
course: "Financial Markets and Institutions"
course_code: "30006"
tags:
  - "source"
  - course_30006
Title: "✓ The option (gross) **payoff** is the amount the option pays at expiration"
Reference: "Course Material"
Created: 2026-05-18
Processed: true---

## Class 30006 – Financial Markets and Institutions Universit→ Commerciale Luigi Bocconi Fall 2025 Prof. Francesco Bripi **Derivatives: Options (Chapter 24)**

## Outline of today

## Options

## 1. Definition

## 2. Types of options

3. Payoff and profit

4. Prices and determinants

## 5. Options Vs Futures

## Options: Definition

✓ An the holder the to an **option** gives **right** buy (or sell) _asset in the future at a underlying pre-determined price_ (the _**strike**_ or _**exercise** price_ ), _at a pre-determined date_ (at _**expiration**_ )

- ✓ Unlike a forward/future contract …

`o` … the **holder** (or **purchaser** ) of an **option is not obliged** to make the purchase/sale of the underlying asset if this is unfavorable to him

- ✓ Like a forward/future contract…

`o` the **writer (** or **seller** ) of an **option has** the **obligation** of complying with these terms and cannot refuse to buy/sell the asset (under unfavorable conditions)

## Options: Definition

- ✓ In other words, there is a fundamental **asymmetry** between the rights of _**holder**_ of an option vs. those of a _**writer**_

✓ To compensate for his/her weaker rights, the seller/writer of an option will demand a compensation, called the **option premium** (effectively, the _price_ of the option)

- ✓ The buyer of the option will always have to pay the premium, no matter if she exercises the option or not

## Types of Options

There are two main types:

**1. Call option**: gives the _holder_ the right to _buy_ the underlying asset at the strike price within a specified period of time

**2. Put option**: gives the _holder_ the right to _sell_ the underlying asset at the strike price within a specified period of time

Note that you can buy/sell either type! So, it gets complicated

_**Holder Writer**_ **Lon Short ll g (buy) (se ) CALL** Right to buy Obligation to sell **PUT** Ri ht to sell Obli ion g gat to buy

## Options: Simple Example 1

Before we get into more details, let’s work out a simple example. ✓ Suppose you have a call option with a strike price of $100, maturing tomorrow (analogous of delivery date in forwards) and a premium of $5.

1. The stock tomorrow is worth $120

**Q**: Do you exercise the option? What is your profit?

## Options: Simple Example 1

Before we get into more details, let’s work out a simple example. ✓ Suppose you have a call option with a strike price of $100, maturing tomorrow (analogous of delivery date in forwards) and a premium of $5.

1. The stock tomorrow is worth $120

**Q**: Do you exercise the option? What is your profit? **A:** Yes, you exercise it because it is profitable: You can buy at $100 and sell spot at $120 Gain $120- $100-$5=$15

## Options: Simple Example 1

Before we get into more details, let’s work out a simple example. ✓ Suppose you have a call option with a strike price of $100, maturing tomorrow (analogous of delivery date in forwards) and a premium of $5.

2. The stock tomorrow is worth $90

**Q**: Do you exercise the option? What is your profit?

## Options: Simple Example 1

Before we get into more details, let’s work out a simple example.

✓ Suppose you have a call option with a strike price of $100, maturing tomorrow (analogous of delivery date in forwards) and a premium of $5.

2. The stock tomorrow is worth $90

**Q**: Do you exercise the option? What is your profit? **A**: No, you do not You could buy at $100 but then sell at $90: avoid loss of $10 but still need to pay the premium: loss of $5

## Options: Simple Example 2

- Another simple example of a holder of an option ✓ have a Suppose you put option with a strike price of $250, maturing tomorrow and a premium of $10.

1. The stock tomorrow is worth $210

**Q**: Do you exercise the option? What is your profit?

## Options: Simple Example 2

Another simple example of a holder of an option

- ✓ have a Suppose you put option with a strike price of $250, maturing tomorrow and a premium of $10.

1. The stock tomorrow is worth $210

**Q**: Do you exercise the option? What is your profit? **A:** Yes, you exercise it because it is profitable: You can buy spot (if you don’t have it yet!) at $210 and deliver at $250

Gain $250 - $210-$10=$30

## Options: Simple Example 2

- Another simple example of a holder of an option ✓ have a Suppose you put option with a strike price of $250, maturing tomorrow and a premium of $10.

2. The stock tomorrow is worth $325

**Q**: Do you exercise the option? What is your profit?

## Options: Simple Example 2

Another simple example of a holder of an option

- ✓ have a Suppose you put option with a strike price of $250, maturing tomorrow and a premium of $10.

2. The stock tomorrow is worth $325

**Q**: Do you exercise the option? What is your profit? **A**: No, you do not You could buy at $325 but then sell at $250: avoid loss of $75 but still need to pay the premium: loss of $10

## Options Payoff vs Profit

# ✓ The option (gross) **payoff** is the amount the option pays at expiration

- ✓ We call the option payoff the _option_ _**value**_

- ✓ The option **profit** is the (gross) payoff …

`o` … **minus** the premium paid ( _long_ side: holder/purchaser) or `o` … **plus** the premium received ( _short_ side: writer/seller)

## Profit for** _**holder**_ **(long)

- ✓ **Call option**: exercise a call option only if buying at the strike price _X_ is more favorable than spot price _S_ (S>X _)_

- Payoff is the difference between the value _X_ and _S_ , and in any case never below zero (because if _S < X_ , you don’t exercise the option)

𝑐𝑎𝑙𝑙 𝜋 = max 𝑆−𝑋, 0 −𝑝 𝒍𝒐𝒏𝒈

To get the profit subtract 𝑝

## Call Payoff

- ✓ **Put option**: exercise a put option only if selling at the strike price _X_ is more favorable than the spot price _S_ (X>S _)_

- again, payoff (= _X-S)_ is never below zero (because if _S>X_ , you don’t exercise the option)

- 𝑝𝑢𝑡

- 𝜋 = max 𝑋−𝑆, 0 −𝑝 𝒍𝒐𝒏𝒈

Put Payoff

## Profit from** _**holding**_ **(long) a Call

## Profit from** _**holding**_ **(long) a Put

𝑃𝑢𝑡 𝜋 = max 𝑋−𝑆, 0 −𝑝 π 𝒍𝒐𝒏𝒈 X X-p Payoff X S -p Profit Memo: right to **sell**

## Options: Profit for** _**writer**_ **(short)

- ✓ **Call option**: writer is _**obliged** to sell_ if the buyer of the call exercises the option

`o` holder will exercise only if _S>X_ , but he/she always pays the premium `o` hence writer’s profit is: 𝐶𝑎𝑙𝑙 𝜋𝒔𝒉𝒐𝒓𝒕 = 𝑝−𝑚𝑎𝑥 𝑆−𝑋, 0

- ✓ **Put option**: writer is are _obliged to buy_ if the buyer of the put exercises the option

- holder will exercise only if _X>S_ , but he/she always pays the premium

- `o` hence writer’s profit is

𝑃𝑢𝑡 𝜋𝒔𝒉𝒐𝒓𝒕 = 𝑝−𝑚𝑎𝑥 𝑋−𝑆, 0

Let’s see everything graphically

## Profit from** _**writing**_ **(short in) a Call

𝐶𝑎𝑙𝑙 𝜋 𝒔𝒉𝒐𝒓𝒕 = 𝑝−𝑚𝑎𝑥 𝑆−𝑋, 0

Profit S X Payoff Obligation to sell

## Profit from** _**writing**_ **(short in) a Put

## Examples of Options

✓ _Callable bonds_: bonds that can be called back by the issuing corporation (recall!)… they are a _call option_ ! `o` note that the corporation decides not to exercise the option if the price of the bond (spot) is below the face value (strike price) `o` _i_ the firm pays a premium in terms of higher

✓ _: Stock options_ a popular compensation scheme for managers `o` call options at a strike price and at specified dates `o` in theory … it should align the incentives of manager and of the company: pay linked to performance `o` sometimes not so efficient!

## Options Styles

**1. European options:** do not allow early exercise (before expiration date)

## **2. American options:** allow early exercise

Note: the distinction between European and American options has nothing to do with where they are traded!

**3. Exotic options:** payoff structure is determined in a nonstandard way

- such as the average price of an underlying asset in a certain period of time ( _Asian_ option)

- or _rainbow_ options (on a basket of underlying assets) with payoffs

- determined by:

- best of assets max(𝑆1, … , 𝑆𝑛, 𝐾)

- call on max max(max(𝑆1, … , 𝑆𝑛, ) −𝐾, 0)

## Options Terminology

✓ _**In** the money_: exercise is profitable

- ✓ _**At** the money_: the strike equals the current price of the asset (the option’s intrinsic value is zero),

✓ _**Out**_: exercise is un _of the money_ profitable

✓ A call option is

`o` _**in**_ the money `o` _**at**_ the money `o` _**out**_ of the money

if S>X if S=X if S<X

𝐶𝑎𝑙𝑙 𝜋 = max 𝑆−𝑋, 0 −𝑝 𝒍𝒐𝒏𝒈

✓ A put option is

`o` _**in**_ the money if X>S `o` _**at**_ the money if X=S `o` _**out**_ of the money if X<S

𝑃𝑢𝑡 𝜋 = max 𝑋−𝑆, 0 −𝑝 𝒍𝒐𝒏𝒈

## Options Pricing (Premium)

✓ Pricing of options is a difficult business, need mathematical models (most famous _Black-Scholes-Merton_ , economics Nobel prize winners in 1997)

- ✓ We only examine the determinants of the option premium:

**1. Strike price** ( _X_ )

**2. Spot price at expiration** ( _ST_ )*

**3. Volatility of underlying asset price**

**4. Term to expiration**

## Options Pricing Determinants

**Increase in Call option value Put option value variable (premium) (premium)** Spot price ( _ST_ ) ↑ ↓ Strike price ( _X_ ) ↓ ↑ Volatility ↑ ↑ Time to expiration ↑ ↑ ^rnnvng

## Options Pricing Determinants

**Increase in Call option value Put option value variable (premium) (premium)** Spot price ( _ST_ ) ↑ ↓ Strike price ( _X_ ) ↓ ↑ Volatility ↑ ↑ Time to expiration ↑ ↑

## Options Pricing Determinants

- ✓ The effects of increases in **strike and spot prices** ( _S_ and _X_ ) for call and put options have been examined in the previous slides

- ✓ Note the opposite effects for call and put

- ✓ _Both_ **volatility** and **term to expiration** increase the value of both **call** and **put** options. Why?

- ✓ a call or a

- Look at the profit function from _holding_ put option:

## Options Pricing Determinants

## ✓ **Volatility**

`o` can **only** have a **positive effect**: `o` the greater the chance of spot price (S) increase, the greater your expected profit

`o` the greater chance of S decrease does not matter: you can always decide NOT to exercise the option

✓ **Term to expiration** (same logic) `o` it only increases the chance of a positive gain … `o` … with no impact on losses, capped at _-p_

✓ These two results are given by the _non-linearity_ of the profit function (it is kinked!) `o` e.g.: can decide not to exercise option …not so for futures!

## Options: Hedging Exercise

- Let’s see how hedging with options would work ✓ Suppose you have $100M in a stock portfolio indexed to the S&P500.

**Q**: are you _long_ or short in stocks? What type of risk do you want hedge?

**A**: you’re _long_ in stocks; want hedge a fall in S&P500 price

✓ You can buy a put with strike price $90M or a call with strike price $110M. Both have a p=$1M **Q**: What do you buy to hedge?

**A**: you buy the put: guarantee that your portfolio is worth at least $90M….

## Options: Hedging Exercise

Let’s see how hedging with options would work

- ✓ Suppose you have $100M in a stock portfolio indexed to the S&P500.

**Q**: are you _long_ or short in stocks? What type of risk do you want hedge?

- **A**: you’re _long_ in stocks; want hedge a fall in S&P500 price

✓ You can buy a put with strike price $90M or a call with strike price $110M. Both have a p=$1M **Q**: What do you buy to hedge? **A**: you buy the put: guarantee that your portfolio is worth at least $90M….

## Options: Hedging Exercise

Let’s see how hedging with options would work

- ✓ Suppose you have $100M in a stock portfolio indexed to the S&P500.

- **Q**: are you _long_ or short in stocks? What type of risk do you

- want hedge?

- **A**: you’re _long_ in stocks; want hedge a fall in S&P500 price

- ✓ You can buy a put with strike price $90M or a call with strike price $110M. Both have a p=$1M

**Q**: What do you buy to hedge?

**A**: you buy the put: guarantee that your portfolio is worth at least $90M….

## Options: Hedging Exercise

Let’s see how hedging with options would work

- ✓ Suppose you have $100M in a stock portfolio indexed to the S&P500.

- **Q**: are you _long_ or short in stocks? What type of risk do you

- want hedge?

- **A**: you’re _long_ in stocks; want hedge a fall in S&P500 price

- ✓ You can buy a put with strike price $90M or a call with strike price $110M. Both have a p=$1M

- **Q**: What do you buy to hedge?

- **A**: you buy the put: guarantee that your portfolio is worth at least $90M ...

## Options: Example of NOT hedging

- ✓ In the previous example, had you bought the call, you’d be instead betting that the S&P500 will rise!

- ✓ This can increase your gains!

- ✓ _SoftBank bought nearly $4 billion of shares in tech giants such as Amazon.com Inc., Microsoft Corp. and Netflix Inc. this spring, plus a stake in Tesla. Not included in those disclosures is the massive options trade (…) SoftBank bought a roughly equal amount of call options tied to the underlying shares it bought, as well as on other names, according to people familiar with the matter._

- ✓ _- th WSJ, September 5 , 2020_

## Options: Hedging Exercise

# ✓ Suppose the portfolio is worth $120M at maturity

## **Q**: Do you exercise your put option? What is your profit?

13-34

## Options: Hedging Exercise

✓ Suppose the portfolio is worth $120M at maturity

**Q**: Do you exercise your put option? What is your profit?

- **A**: The put has strike price that is _lower_ than spot at maturity ( _X<S_ or $100M<$120M): choose not to exercise it

## Options: Hedging Exercise

✓ Suppose the portfolio is worth $70M at maturity

## **Q**: Do you exercise your put option? What is your profit?

13-36

## Options: Hedging Exercise

✓ Suppose the portfolio is worth $70M at maturity

**Q**: Do you exercise your put option? What is your profit?

## Options: Hedging Exercise

## Key idea of hedging with a put

- ✓ If things turn badly …

- … you _capped_ your portfolio value at $90M, by paying the premium of $1M

- ✓ If things turn well …

`o` … you have also reduced your profits by only $1M.

- ✓ Put option here works like an _insurance_ . This is why it is called _**protective put**_

## Options: Hedging Exercise

## ✓ Recap

|ecap|
|---|---|---|---|
|case (1)|case (2)|
|ST≥X|ST<X|
|Spot price at t=0 (S0)|100|100|
|Strike price (X)|90|90|
|Spot price at  t=T (ST)|120|70|
|Value of put option (pput)|-p= -1|X - ST- p = 90 - 70 - 1  = 19|
|Total profit (pTOT=DS +pput)|= (120 - 100) - 1 =19|=(70 - 100) + 19 = - 11|
|Final value (S0+pTOT)|= 100 +|19 = 119|= 100 - 11 = 89|
|Final value (alternative)|(ST- p)|= 120 - 1 = 119|(X - p) = 90 - 1 = 89|
*(See also: [[Lect11_exercises#^n7aww9]])*

## Options: Hedging Exercise

✓ In general, the **additional value** of buying the **put** option 𝑆 compared to **not buying it** (where 𝑇 is spot price of portfolio at maturity)

## Example of speculation

11 April 2017

## Recap on Options

✓ _Just check out the profit functions from before:_

𝐶𝑎𝑙𝑙 𝜋 = max 𝑆−𝑋, 0 −𝑝 𝒍𝒐𝒏𝒈 𝑃𝑢𝑡 𝜋 = max 𝑋−𝑆, 0 −𝑝 𝒍𝒐𝒏𝒈

_potentially …_ _**limited** losses holder or large gains_

𝑃𝑢𝑡 𝜋𝒔𝒉𝒐𝒓𝒕 = 𝑝−𝑚𝑎𝑥 𝑋−𝑆, 0 𝐶𝑎𝑙𝑙 𝜋𝒔𝒉𝒐𝒓𝒕 = 𝑝−𝑚𝑎𝑥 𝑆−𝑋, 0

_potentially …_ _**large** losses or limited gains_

_writer_

## Options Vs Futures

## ✓ Futures are **one-sided bets**:

`o` you gain if the bet is correct and lose otherwise `o` same is true for the counterparty

- ✓ **a**

- Options are **symmetric bets**

- ✓ the **buyer** of the option will experience:

- **large** gains if his/her bet is correct

- `o` **limited losses** if his/her bet is incorrect

- ✓ the **seller** of the option will experience: `o` **limited gains** if his/her bet is correct `o` **large losses** if his/her bet is incorrect

- ✓ _Just check out the profit functions from each case!_

## Options Vs Futures

## Once again:

## ✓ Future is an obligation for both parties

## ✓ Options

`o` give a right to the option holder `o` but it is an obligation for the option writer (if the holder requests it)

- ✓ Futures are **costless** to initiate `o` no cash is exchanged until the position is closed

- ✓ Options are **not costless** to initiate `o` the buyer has to pay the seller an **option premium**

## Related Notes
- [[Lect11_exercises]]
- [[Lect23_Questions_Answers]]
- [[Lect12_Review_exercises_answers]]