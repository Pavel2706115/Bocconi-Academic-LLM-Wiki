---
course: "Financial Markets and Institutions"
course_code: "30006"
tags:
  - "source"
  - course_30006
Title: "Interest Rates and Valuation (Chapter 3)"
Reference: "Course Material"
Created: 2026-05-18
Processed: true
  - "source"
---

# Interest Rates and Valuation (Chapter 3)

# Interest rates variation over time

## Chapter Preview

Interest rates are among the most closely watched variables in the economy.

This lecture: Lots of definitions and (some) math.

**IMPORTANT: LEARN by UNDERSTANDING, DO NOT LEARN BY HEART!**

## Topics

1. Present value

2. Yield to maturity

3. Zero coupon bonds

4. Coupon bonds

5. Perpetuity

6. Nominal Vs real interest rate

7. Rate of return and interest rate risk

8. Duration

## Present Value: Introduction

Suppose we have 100€ and 50$. What is our total wealth?

100€ + 50$ = ??

We need an exchange rate to express everything in a common unit (base currency)

× 100€ + 50$ (0.84 €/$)=142€ 100€×(1.19 $/€) + 50$=169$

Now consider 1$ today (t=0) and 1$ tomorrow (t=1): 1$0 + 1$1= **??** No change of currency, but change of **time** !

## Present Value: Introduction

- Consider a 1$ today (t=0) and a 1$ tomorrow (t=1)

- 1$ today (time t=0: $0) is **NOT** equal to 1$ tomorrow (time t=1: $1).

## Why?

- Presumably 1$ today is better than a 1$ tomorrow,  because: a. the future is uncertain b. people are impatient

- To find the value of $0 corresponding $1 we need a conversion rate

- (or a sort of “ _exchange_ rate”) between today and tomorrow ($0 /$1): **discount factor**

## Present Value: Introduction

## Discount factor

- Invest 1 today, get (1+ 𝑖 ), with 𝑖 >0 tomorrow. Hence:

- $1= (1+ 𝑖 )$0

- $2= (1+ 𝑖 )$1 = (1+ 𝑖 )(1+ 𝑖 )$0 = (1+ 𝑖 )(2) $0

- $3= (1+ 𝑖 )$2 = (1+ 𝑖 )(1+ 𝑖 )(1+ 𝑖 )$0 =(1+ 𝑖 )(3) $0

_…_ $ _n_ = (1+ 𝑖 )$n-1 = … =(1+ 𝑖 ) _(n)_ $0

At each period t have a cash flow ( 𝐶𝐹𝑡 = $𝑡) that is fully reinvested with interest earned in the previous period:

## Present Value: Introduction

## Discount factor

- the _discount factor_ is a function of the **interest rate** ( 𝑖 ) between today and tomorrow

- it’s called _discount_ because you are _discounting_ the future

- can see the discount factor in this way: $1= (1+ 𝑖 )$0 , with 𝑖 >0

## Present Value: Introduction

## PV useful to compare various financial instruments

- EX: consider 2 financial instruments (4 ex.: bonds, loans, etc…): A and B

200 200 200 200

Asset A:

Asset B:

50 50 50 650 _0 1 2 3 4_

## The interest rate is 𝑖= 0.1 = 10% . Then:

## Present Value: Introduction

Debt instruments differ by:

- streams of cash payments ( **cash flows** )

… and …

- timing

The **evaluation** of amounts at different points in time is called _**Present Value (PV)** analysis_

All present value calculations are of this kind:

PV computes the value at time 0 (=present) of future cash flows

## Present Value: Introduction

In previous formula we call 𝑖 the **yield-to-maturity (YTM)*** or simply **interest rate**

## IF

the price of the security ( _P_ ) is equal to the Present Value ( _PV_ ) of its future cash flows

if 𝑃= 𝑃𝑉→𝑖= 𝑌𝑇𝑀

Definition: _YTM is the interest rate that equates the PV of the cash flows with the value (price) of the debt instrument today_

_Note that:_ _**i**_ **≠ RATE OF RETURN** We will see examples where _**i**_ >0 but Return<0

## Present Value: Introduction

In most finance applications:

_P=PV(cash flows)_

where P is the Security’s Price P=PV is true under certain on investors’ assumption rationality and **efficiency** of financial markets

We will see this later in the course …

- … for now, just assume it: financial markets are efficient

## Present Value: Applications

- There are two basic types of debt instruments which incorporate present value concepts:

- **LOANS** (for ex.: mortgages)

- **BONDS** (for ex.: Treasury or corporate bonds)

- We’ll only look at bonds in this class (examples with loans in the book). In particular: **1. Zero Coupon Bond (or Discount Bond)** `o` No coupon

- **2. Coupon Bond** `o` With coupon

## Coupon and Zero-coupon bonds

Zero Coupon bond from US Treasury

## Coupon bond from US Treasury

## Discount or Zero-Coupon Bond (ZCB)

A ZCB (or call ir **discount bond** ):

- does _not_ give _any_ interest (coupon) payments before maturity =zero-

- ( coupon _) …_

- … but it only pays the face value ( _FV_ ) to the holder of the bond at the end (=maturity)

## Discount or Zero-Coupon Bond (ZCB)

A ZCB (or call ir **discount bond** ):

- does _not_ give _any_ interest (coupon) payments before maturity =zero-

- ( coupon _) …_

- … but it only pays the face value ( _FV_ ) to the holder of the bond at the end (=maturity)

- It normally sells at a price _below_ the face value (at discount)

- Ex: pay $0.95 today, get $1 at maturity. Earning=$0.05. YTM?

## Discount or Zero-Coupon Bond (ZCB)

A ZCB (or call ir **discount bond** ):

- does _not_ give _any_ interest (coupon) payments before maturity

- =zero-

- ( coupon _) …_

- … but it only pays the face value ( _FV_ ) to the holder of the bond at the end (=maturity)

- It normally sells at a price _below_ the face value (at discount)

- Ex: Calculate the **YTM** for a zero-coupon that pays $0.95 today, get $1 at maturity (assume 1 year maturity). Intuitively:

1−0.95 𝑖= 0.95(= 0.053)( (read: 5.3%))

𝐹𝑉−𝑃 So, formula is: 𝑖= 𝑃

- Government bills are typically ZCBs

## Discount or zero-coupon Bond

- Price of a discount bond with **1** year maturity:

𝐹𝑉−𝑃 𝐹𝑉 𝐹𝑉 𝐹𝑉 𝑖= ⟹𝑖= 𝑃 𝑃(−1 ⟹1 + 𝑖=) 𝑃(⟹𝑃=) 1 + 𝑖

## Discount or zero-coupon Bond

- Price of a discount bond with **1** year maturity:

- Price of a discount bond with _**n**_ years maturity instead:

## Discount or zero-coupon Bond

- Price of a discount bond with **1** year maturity:

- Price of a discount bond with _**n**_ years maturity instead:

`o` _Example_: what is the YTM for a discount bond with 5 years maturity with a face value of $1,000, selling at $750?

## Coupon Bonds

## A **coupon bond**

- is a bond that makes a fixed payment at specific dates (coupons) plus a final amount (face value or par value) at maturity

- The price today of a coupon bond is the PV of its future cash flows

- Consider _**2**_ periods:

𝐶 𝐶 𝑭𝑽 𝑃=(+) 1 + 𝑖(+) 1 + 𝑖(2) 𝟏+ 𝒊(𝟐)

`o` where 𝐶 is the coupon payment, 𝐹𝑉 is the face value, 𝑛 the years to maturity, _i_ is the **YTM** ( 𝐶 , 𝑖 fixed over time)

## Coupon Bonds

- Consider **many** periods. For ex., a 10% coupon bond with a face value of $1,000 and 10 years to maturity will have a cash flow of $100 each year plus a payment of $1,000 at the end: ^bbgalg

𝐶 𝐶 𝐶 𝑪 𝑭𝑽 𝑃=(+)(+ ⋯+) 1 + 𝑖(+) 1 + 𝑖(2) 1 + 𝑖(3) 𝟏+ 𝒊(𝟏𝟎)(+) 𝟏+ 𝒊(𝟏𝟎) $100 $100 $100 $𝟏𝟎𝟎 $𝟏, 𝟎𝟎𝟎 𝑃=(+)(+ ⋯+) 1 + 𝑖(+) 1 + 𝑖(2) 1 + 𝑖(3) 𝟏+ 𝒊(𝟏𝟎)(+) 𝟏+ 𝒊(𝟏𝟎) Generic formula of price of CB’s: 𝐶 𝐹𝑉 𝑃= σ𝑛𝑡=𝟏 (1+𝑖)(𝑡)(+) (1+𝑖)(𝑛)

- Generic formula of price of CB’s:

`o` Note time convention: Σ starts at 𝑡= 𝟏 (assume buy coupon bond at 𝑡= 0 , but bond only starts paying the following year) and it ends at 𝑛 maturity

## Coupon Bonds

## Useful terminology

- _**Coupon rate**_: the amount it pays every year is expressed as a % of face value:

𝐶𝑜𝑢𝑝𝑜𝑛 𝐶 = 𝑖 𝑐𝑜𝑢𝑝𝑜𝑛𝑟𝑎𝑡𝑒 𝐹𝑎𝑐𝑒𝑉𝑎𝑙𝑢𝑒(=) 𝑭𝑽

- If 𝑃= 𝐹𝑉 we have a **par bond**

- If 𝑃< 𝐹𝑉 we have a bond **at discount**

- If 𝑃 > 𝐹𝑉 we have a bond **at premium**

## CBs Example: P, YTM and coupon rate

Recall the previous example: 𝐶 𝐶 𝐶 𝐹𝑉 𝑃=(+ ⋯+)(+) 1 + 𝑖(+) (1 + 𝑖)(2) (1 + 𝑖)(10) (1 + 𝑖)(10) **Q:** if the YTM=11.75%, what is the price today of a “10% coupon bond” with a face value of $1,000 and 10 years maturity?

## CBs Example: P, YTM and coupon rate

## Recall the previous example:

**Q:** if the YTM=11.75%, what is the price today of a “10% coupon bond” with a face value of $1,000 and 10 years maturity?

## **A:** First recover coupon value 𝐶:

𝐶 𝑖 = 𝑐𝑜𝑢𝑝𝑜𝑛𝑟𝑎𝑡𝑒 𝐹𝑉(⟹𝐶= 𝑖)(𝑐𝑟)(× 𝐹𝑉⟹𝐶= 0.1 × $1,000 = $100)

## Then, calculate price of CB using PV of cash flows:

## CBs Example: P, YTM and coupon rate

A 3-year corporate bond has a face value of $1,000 and a 7% coupon rate; the current market interest rate is 6%. ( 𝑛= 3; 𝐹𝑉= $1,000; 𝑖𝑐𝑟 = 0.07; 𝑖= 0.06)

**Q**: What should be the bond's price?

## CBs Example: P, YTM and coupon rate

A 3-year corporate bond has a face value of $1,000 and a 7% coupon rate; the current market interest rate is 6%. ( 𝑛= 3; 𝐹𝑉= $1,000; 𝑖𝑐𝑟 = 0.07; 𝑖= 0.06)

**Q**: What should be the bond's price?

**R**: Recall:

𝐶 = `o` 𝑖 𝑐𝑟 𝐹𝑉(; 𝐶= 𝑖)(𝑐𝑟)(× 𝐹𝑉= 0.07 × $1,000;𝐶= $70)

## Special case of CB: Perpetuity

## A special case of a coupon bond is a **perpetuity** (or **consol** )

- It is a coupon bond providing a periodic coupon _**forever**_ (=with no maturity date)

- It is convenient in finance because it is easy to calculate its price ( _i.e._ its present value)

- Why? If you like math here is why. It is a geometric series:

## Do perpetuities exist?

- UK government issued perpetual war bonds in WWIWWII:

- “ _If you cannot fight, you can help your country by investing all you can in 5 per cent Exchequer Bonds ... Unlike the soldier, the investor runs no risk._ ”

- These war bonds were redeemed by the UK government in October 2014

- Other remaining consols dating even further back (1850s) were redeemed in July 2015

- Nowadays perpetuities are issued by banks for regulatory purposes

## Current yield

- The perpetuity allows us to introduce the concept of **current**: **yield**

𝐶 = 𝑖 𝑐𝑢𝑟𝑟𝑒𝑛𝑡 𝑃

- The current yield is a useful approximation to the YTM for long-term bonds, with price near par.

- Why? Because CF very distant in time have a low PV, so a 30-year bond is pretty much like a perpetuity!

## Example

- $100

- i. 𝑖 = a perpetuity bond with P=$2,000 and C=$100 has 𝑐𝑢𝑟𝑟𝑒𝑛𝑡 $2,000(= 0.05)

- ii. a coupon bond with same price and coupon, with **30** years of maturity (and a FV=$2,500) has…………………………………………. _i_ = 5.354%

- iii. a coupon bond similar to above with **50** years maturity: _i_ = 5.115%; iv. a coupon bond similar to above with **100** ys maturity: _i_ = 5.010% v. … and so on

## Current yield and Coupon Rate

## Notice the distinction between

- The _**current yield**_ (Coupon divided by the Price):

𝐶 = 𝑖 𝑐𝑢𝑟𝑟𝑒𝑛𝑡 𝑷 - The _**coupon rate**_ (Coupon divided by the Face Value) 𝐶 = 𝑖 𝑐𝑜𝑢𝑝𝑜𝑛 𝑭𝑽

- of course for a _par-bond_ the two coincide (bcs 𝑃= 𝐹𝑉 ).

## YTM and Price

## So what is more important, the YTM or the price?

- mathematically, it does not matter: given one, the other one is determined via the PV formula

- but economically we think of the YTM determining the price, not viceversa.

- Why? Think about the YTM as the **“fair” return** an investor **requires** considering the risk

- Then the investors will price the bonds so that in equilibrium they get this fair return

## Relationships between Price, YTM and Coupon rate

**Table 3.1** Yields to Maturity on a 10% Coupon rate bond, maturing in 10 years (Face Value = $1,000)

## Three interesting facts in Table 3.1:

**1. When bond is at par** (P=FV) **, YTM equals coupon rate**

**2. Price and yield are negatively related (VERY IMPORTANT!)**

**3. Yield greater than coupon rate when bond price is below par value**

## Relationships between Price, YTM and Coupon rate

. **1) When bond is at par, yield equals coupon rate** 𝐶 𝐶 = = `o` math: if 𝑃= 𝐹𝑉, then 𝑖𝑐𝑢𝑟𝑟𝑒𝑛𝑡 𝑃(and)( 𝑖)(𝑐𝑜𝑢𝑝𝑜𝑛) 𝐹𝑉(coincide) `o` intuition: a _par bond_ is like a bank account, if you put down $1,000 ( _P_ ) today ( _t=0_ ) and you cash in the interest payment every year ( _C_ =$100), you are left with $1,000 (FV) at maturity (say _t=10_ ) … 𝐶 $100 `o` … similar to bond with 𝑖 = 10% and 10 coupon 𝐹𝑉(=) $1,000(= 0.1) years maturity ^0m0ker
*(See also: Chapter 3#^vagpac)*

## 2) Price and yield are negatively related

`o` **If** _**i**_ **increases, the PV of any given cash flow is lower; hence, the price of the bond must be lower**

`o` a bit more obvious from perpetuity and zero-coupon bond formulas, but it emerges also from coupon bonds

## Relationships between Price, YTM and Coupon rate

## 3) The YTM is greater than the coupon rate when bond price is below par value

- 𝐶

- `o` According to (1): 𝑖𝑓𝑃= 𝐹𝑉⇒𝑖= 𝐹𝑉

- `o` According to (2): 𝑖𝑓𝑖↑𝑡ℎ𝑒𝑛𝑃↓

- `o` Putting (1) and (2) together, it must be that:

𝐶 𝑌𝑇𝑀> 𝑖 = ~~തതതത 𝑎𝑛𝑑𝑠𝑖𝑛𝑐𝑒𝑃↓⇒𝑃< 𝐹𝑉~~ 𝑖𝑓𝑖↑⇒ 𝑐𝑟 𝐹𝑉

## What does this mean?

- If the required yield on the bond is higher than what the bond actually pays (that is, the coupon rate), then it needs **to sell at discount to attract investors** (=price is too high, not attractive!)

- In other words, because investors can make a larger return the financial market (=other securities), they need an extra incentive to

## Real and Nominal Interest Rates

- The **real interest rate** ( _ir_ ) is the nominal interest rate ( _i_ ) adjusted for **expected inflation** (expected changes in the price level).

- From the Fisher equation:

- Technically, this definition of _ir_ is the _**ex-ante**_ **real rate of interest** because it is adjusted for the _**expected**_ level of inflation, p _(e)_

- We can calculate the _**ex-post**_ real rate based on the p

- observed level of inflation ( )

## Real and Nominal Interest Rates

- When the real rate ( _ir_ ) is low:

- there are **greater** incentives to **borrow** (money is less costly)

`o` and **less** incentives to **lend** (money is not very profitable)

- In response to the Financial Crisis (2008), Fed & ECB turned =

- 𝑖 0 so 𝑖 < 0 was low but to stimulate , ~~𝑟~~ (inflation still positive)

- aggregate spending (consumption and investment)

- _Case of Deflation_ (p _(e) <0_ ):

- 𝑖 𝑖= 0:

- the real rate will always be positive: consider case of lowest - 𝑖 =-p _(e)_ >0 bcs p _(e)_ <0 𝑟

- Deflation can be a big problem:

- expectations of deflation lead to higher real rates and may cause deflationary _spirals_: The Economist, 07 Jan 2015

- but some evidence says it is not so bad: CEPR, Jan 2022

## Do not hold bond until maturity

# Let ℎ= holding period and 𝑛= maturity

- _So far mostly considered_ ℎ= 𝑛 _(hold bond until maturity)_

- _Now consider 2 cases where_ holding period ≠ maturity

- Case **1**: you sell the bond at time 𝑡 **before** maturity ( 𝑛 ) `o` holding period shorter than maturity ( 𝒉< 𝒏 )

`o` need consider price of sale at time ℎ ( 𝑃ℎ may be different from 𝑃0 ), bcs do not get FV

- Case **2**: you sell bond at time 𝑡 **after** maturity ( 𝑛 )

- `o` holding period shorter than maturity ( 𝒉> 𝒏 )

`o` 𝑛 𝑃 > 𝑜𝑟< 𝑃 ? need consider price of bond you buy at time ( 0 𝑛 )

## Interest Rate ≠ Rate of Return

## Rate of return

- we we one

- Suppose buy a coupon bond, hold it for only period and we don’t keep it up to maturity, but we **sell it before maturity (** 𝒉< 𝒏 **)**

`o` with sale _before_ maturity, price may change (we don’t wait to get FV) `o` so, we need to consider the **capital gain** (say: if cap. gain is negative, we may have a loss!)

- The _rate of return_ on our investment is all the payments received during the holding period, divided by the initial price:

## where:

𝐶 = 𝑖 𝑐 𝑃 𝑡

𝐶+𝑃 −𝑃 𝐶 𝑃 −𝑃 𝑡+1 𝑡 𝑡+1 𝑡 = 𝑅𝑒𝑡𝑢𝑟𝑛= = 𝑖 𝑐 + 𝑔 𝑃 𝑃 𝑃 𝑡 𝑡(+) 𝑡 (current yield)

and

(capital gain)

## Example: Interest Rate ≠ Rate of Return

Assume you paid $1,000 for a 10-year coupon bond with a face value of $1,000, and a coupon rate of 10%. One year after the purchase, you sold the bond for: a. $1,200 b. $   800

**Q**: What is your _rate of return_ ? What is the (initial) YTM?

## Example: Interest Rate ≠ Rate of Return

Assume you paid $1,000 for a 10-year coupon bond with a face value of $1,000, and a coupon rate of 10%. One year after the purchase, you sold the bond for: a. $1,200

b. $   800

**Q**: What is your _rate of return_ ? What is the (initial) YTM? **A:** 𝐶= 𝑖𝑐𝑟 × 𝐹𝑉= 0.1 × $1,000 = $100

## Example: Interest Rate ≠ Rate of Return

What happened after one year?

- by the time you wanted to sell the bond, its yield `o` went **down** (=price went up)       in case a `o` went **up** (=price went down)   in case b

- Case a: new investors are willing to pay a higher price for a bond whose coupon rate (10%) is higher than current interest rates at prevailing market conditions `o` reverse in case b

- Let’s see in the next table what happens to bonds’ returns if **the interest rate increases** on the bond , depending

- _different maturities_

## Key Facts about the Relationship between Rates and Returns

**Table 3.2 One-Year Returns** on 10% Coupon Par Bonds (FV=$1,000) **When interest rate rises from 10% to 20%**

Recall the coupon bond formula and return formula: 𝑃= σ𝑛𝑡=1 𝐶 𝐹𝑉 𝑅𝑒𝑡𝑢𝑟𝑛= 𝐶+𝑃𝑡+1−𝑃𝑡 = 𝑖𝑐 + 𝑔 1+𝑖(𝑡)(+) 1+𝑖(𝑛) 𝑃𝑡

## Key Facts about the Relationship between Rates and Returns

**Table 3.2 One-Year Returns** on 10% Coupon Par Bonds (FV=$1,000) **When interest rate rises from 10% to 20%**

Recall the coupon bond formula and return formula: 𝑃= σ𝑛𝑡=1 𝐶 𝐹𝑉 𝑅𝑒𝑡𝑢𝑟𝑛= 𝐶+𝑃𝑡+1−𝑃𝑡 = 𝑖𝑐 + 𝑔 1+𝑖(𝑡)(+) 1+𝑖(𝑛) 𝑃𝑡

## Summary on relationship between rates and returns

Key findings from Table 3.2

1. For bonds with holding period < maturity ( ℎ< 𝑛 ), 𝑖↑⇒𝑃↓ implying capital loss

- ∆𝑅 ) for any ∆𝑖

3. The only bond whose return = yield is the one with maturity = holding period (obvious: at maturity, no risk of capital gain/loss!)

4. Even if a bond has a high initial int. rate, the return can turn if _i_ - negative

## Interest Rate Risk

- For the same Δ _i_ - Δ _P ,_ is more negative for L-T bonds … so

- prices are **more “volatile” for long-term (L-T)** bonds `o` and thus, these bonds are riskier than short term bonds

- The risk of losing money ( Δ𝑃< 0 _)_ if interest rates change is called **Interest Rate Risk (IRR)**

- IRR comes from the fact that the bonds may be **sold before maturity** ℎ< 𝑛

`o` in this case you don’t know what the interest rate (and **hence the price** ) will be at the time you wan to sell it 𝑡= ℎ

`o` it is very important for investors (and banks in particular) to manage IRR, not just from bonds, but also other securities

## Interest Rate Risk

- So have IRR only for bonds whose holding period is shorter than maturity ℎ< 𝑛

- No IRR for any bond whose maturity equals holding period ( _i_ =return): obvious! ℎ= 𝑛

- call this case as **hold-to-maturity (HTM)**

- Of course, we always have ALSO other risks: `o` _**default** risk_

- _**inflation** risk_ (that’s true of any investment in securities that pays a nominal return (some bonds are indexed with interest that adjusts with inflation rate))

## Reinvestment Risk

- If ℎ> 𝑛 **holding period is longer than maturity** , you don’t have IRR, but you have **reinvestment risk** `o` at the moment of reinvesting, you may fail to get the same interest rate as before! `o` coupon payments of a coupon bond are $’s that could/should be re-invested in other bonds. But the **future** _**i**_ **is uncertain** !

## Reinvestment Risk

- If ℎ> 𝑛 **holding period is longer than maturity** , you

- don’t have IRR, but you have **reinvestment risk** `o` at the moment of reinvesting, you may fail to get the same interest rate as before!

`o` coupon payments of a coupon bond are $’s that could/should be re-invested in other bonds. But the **future** _**i**_ **is uncertain** !

- **Q**: Is it better to invest at time _t_ in: a. a **2** -year coupon bond with 𝑖= 10% with ℎ= 𝑛 _or_

- b. a **1** -year coupon bond with 𝑖= 10% , and re-invest the proceeds at 𝑡+ 1 in another 1-year coupon bond with 𝑖= 10% ? ( ℎ> 𝑛 )?

## Reinvestment Risk

- If ℎ> 𝑛 **holding period is longer than maturity** , you don’t have IRR, but you have **reinvestment risk** `o` at the moment of reinvesting, you may fail to get the same interest rate as before!

`o` coupon payments of a coupon bond are $’s that could/should be re-invested in other bonds. But the **future** _**i**_ **is uncertain** !

- **Q**: Is it better to invest at time _t_ in: a. a **2** -year coupon bond with 𝑖= 10% with ℎ= 𝑛 _or_

- b. a **1** -year coupon bond with 𝑖= 10% , and re-invest the proceeds at 𝑡+ 1 in another 1-year coupon bond with 𝑖= 10% ? ( ℎ> 𝑛 )?

## **A**: it depends …

- in case a, ℎ= 2 years, while 𝑛= 1 is 1 year for each bond

- `o` in case b, if interest rate **falls** / **rise** in 𝑡+ 1 , you **lose** / **gain**: at the moment of reinvesting, you may fail to get the same interest rate as before!

## Duration

## Can we **quantify** the **IRR** of a bond?

- the further in the future the _payments_ of a bond lie, the more the bond is exposed IRR

- idea: we could use a measure of time of each payment (c.d. “effective maturity”) of a bond to quantify IRR

- in practice: to construct this measure of “effective maturity”, for each period:

- 1(st): calculate the % of the total PV of a bond is contributed by cash flows in each year payments are due (4 ex.: 1, 2, etc…)

- 2(nd): use these weights to calculate a “weighted” maturity

- Duration is the **weighted average of the maturities of the cash payments**

`o` it’s like an effective maturity `o` useful because it allows to _quantify_ the IRR because …

```
o
```

## Duration

## Before we get to the formula, let’s see the intuition

- We want a measure of IRR

- Use the idea that the longer the maturity the higher IRR

Two bonds with same original maturity do **not** same IRR necessarily have

1: a zero-coupon bond (ZCB) makes all payments at the end 2: a coupon bond (CB) spreads them out in each period

**Q**: is the IRR (measured by the _effective maturity_ ) higher or lower for a ZCB with the same maturity of the coupon bond?

## Duration

## Before we get to the formula, let’s see the intuition

- We want a measure of IRR

- Use the idea that the longer the maturity the higher IRR

Two bonds with same original maturity do **not** same IRR necessarily have

- 1: a zero-coupon bond (ZCB) makes all payments at the end 2: a coupon bond (CB) spreads them out in each period.

**Q**: is the IRR (measured by the _effective maturity_ ) higher or lower for a ZCB with the same maturity of the coupon bond?

**A**: **higher** for ZCB, because ZCB makes all payments at the end, while CB makes payments earlier than ZCB

## Formula for Duration

where: 𝐶𝑃𝑡 = 𝐶 for 𝑡< 𝑛 ; 𝐶𝑃𝑡 = 𝐶+ 𝐹𝑉 for 𝑡= 𝑛

- Formula intuition: the _effective_ of bonds is a _maturity_ coupon

- weighted average of effective maturities on discount bonds

`o` each coupon payment is like a discount bond

`o` 𝛼 the weights ( 𝑡 ) are equal to the proportion of the total value (in terms 𝐶𝑃 𝑡 1+𝑖(𝑡) 𝛼 = of PV) represented by each discount bond: 𝑡 𝐶𝑃

## Explaining formula for Duration

𝐷𝑈𝑅 = 𝛼 … 𝐷𝑈𝑅 = 𝛼 1 1 × 1 4 4 × 4

𝐷𝑈𝑅 = 𝐷𝑈𝑅 𝑡 1 + 𝐷𝑈𝑅2 + 𝐷𝑈𝑅3 + 𝐷𝑈𝑅4

- if the weights are the proportion of the total value (in terms of PV) represented by each discount bond …

- … why is the d **uration of a ZCB equal to its maturity** ?

## Calculating Duration -** _**i**_ **=12%, 5 Year, Coupon Bond

## Decompose 𝑃𝑉𝑇𝑂𝑇:

2-56

## Calculating Duration -** _**i**_ **=10%, 10 Year, 10% Coupon Bond

**Duration for a coupon bond always less than actual maturity (see next page)**

2-57

## Properties of Duration

## Properties: DUR** - **if:

- **1. Maturity** (obvious)

**2.** 𝒊 - 𝒄𝒓(= 𝑪/𝑭𝑽) (ZCBs have max duration=actual maturity because

they pay all at the end)

**3.** 𝒊 - sensitivity to changes in rates increases as rates fall (because duration is a linear approximation: as int. falls, discount the future less, far distant weights from now are higher)

Recall also:

## Duration and Interest-Rate Risk

- Recall that IRR is given by the price change of a coupon bond if _i_ changes

- With the duration we can approximate (for **small changes** in interest rate) the % price change with:

∆𝑖

%∆𝑃≈−𝐷𝑈𝑅×

1 + 𝑖 0

`o` note: ∆𝑖= 𝑖 1 −𝑖0

- the formula comes from a 1(st) order Taylor approximation

Ex: if 𝑖↑ from 10% to 11% for coupon bond with a duration of 6.76 years:

Δi =0.11-0.1=0.01

0.01

## Duration and

## Interest-Rate Risk (cont.)

- The **greater** the duration of a security, the **greater** the percentage change in the market value of the security ( Δ𝑃 ) for a given change in interest rates ( 𝛥𝑖 )

- Therefore, the greater the duration of a security, the greater its IRR

- The duration is not quite the same as the IRR, but it measures its **intensity** !

## Exercise: Duration

A 5% coupon bond has a YTM of 6% and a price of $965 . The interest rate then falls to 5.5%. The duration is 4 years. **Q**: What is the new price?

## Exercise: Duration

A 5% coupon bond has a YTM of 6% and a price of $965 . The interest rate then falls to 5.5%. The duration is 4 years. **Q**: What is the new price? **A**: 𝑃= $983.2 Indeed:

- – Δi =0.055 0.06= 0.005

1+i = 1+ 0.06 = 1.06

− Δ𝑖 0.005 %Δ𝑃≈−𝐷𝑈𝑅× 1 + 𝑖(= −4 ×) 1.06

= +0.019

- 𝑃1 = 𝑃0 1 + 0.019 = $965 × 1.019 = $983.2

## Duration of a Portfolio

Consider not a single security, but a portfolio of securities

## Duration is additive (∑)

- The duration of a _portfolio of securities_ is the **weighted-** of the durations of the individual securities …

- **average**

- … with the **weights** equaling the proportion of the portfolio value invested in each security

- Ex: if have _n_ bonds in the portfolio:

- _DURportfolio_ = _DUR1_ × _w1_ + _DUR2_ × _w_ 2 +...+ _DURn_ × _w_ 𝑛

- _where w k is the weight of bond k over total value of bonds in the_

- _portfolio_

## Exercise: Duration of a Portfolio

- Assume that you have a portfolio of 2 bonds `o` One has a duration of 3 years, and the other has a duration of 7 years `o` The market values of the bonds are $600 and $900, respectively `o` Both bonds have the face value of $1,000 **Q**: What is the **duration of your portfolio** ? ^qe7lwr

## Exercise: Duration of a Portfolio

- Assume that you have a portfolio of 2 bonds

`o` One has a duration of 3 years, and the other has a duration of 7 years `o` The market values of the bonds are $600 and $900, respectively `o` Both bonds have the face value of $1,000

## **Q**: What is the **duration of your portfolio** ?

𝐷𝑈𝑅𝑝𝑜𝑟𝑡𝑓𝑜𝑙𝑖𝑜= 3 × 0.4 + 7 × 0.6 = 1.2 + 4.2 = 5.4 (years)

**N.B.1** The weights reflect the values (market prices) of the securities in the portfolio, not their face values

## Chapter 3 Summary (1/2)

1. We examined how to price various debt instruments using the Present Value formula

2. We defined the YTM as the interest rate that makes the price of debt (P) equal to its PV

3. We defined the concept of the current yield = C/P

4. We discussed the relation between YTM, P and C `o` Especially that YTM and P are negatively related!

5. We distinguished between real and nominal interest rate

## Chapter 3 Summary (2/2)

6. We distinguished between _i_ and rate of return and found out that only if we HTM the two coincide

7. Hence, we defined IRR, which makes investment in L-T bonds risky

8. And we’ve seen how to measure IRR using Duration

Lots of definitions, but these are all **fundamental concepts** for the rest of the semester. Make sure you understand them!

## Related Notes
- Chapter 3
- [[Lect3_exercises]]
- [[Full-material presentation Chapter 10]]