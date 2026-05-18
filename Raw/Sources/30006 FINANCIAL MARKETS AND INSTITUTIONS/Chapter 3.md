# Present Value: Introduction
### Suppose we have €100 and $50. What is our total wealth?

## €100 + $50 = ??

### We need an exchange rate to express everything in a common unit (base currency)

€100 + $50x(0.84 €/$) = €142
€100x(1.19 $/€) + $50 = $169

### Now consider $1 today (t=0) and $1 tommorrow (t=1):
### $₀1 + $₁1 = ??
### No change of currency, but change of time!

### Consider a $1 today (t=0) and $1 tomorrow (t=1)
### $1 today (time t=0: $₀) is NOT equal to $1 tomorrow (time t=1: $₁)

### Why?
### Presumably $1 today is better than a $1 tomorrow, because:
1. The future is uncertain 
2. People are impatient
To find the value of $₀ corresponding $₁ we need a conversion rate (or a sort of "exchange rate") between today and tomorrow $₀ / $₁ : discount factor 

## Discount factor
### Invest 1 today, get (1+i), with i>0 tomorrow. Hence:

### $₁ = ( 1+i ) x $₀  
### $₂ = (1 + i) x $₁ = (1 + i) x (1 + i) x $₀ = (1 + i)² x $₀ 

### $₃ = (1+𝑖) x $₂ = (1+𝑖)(1+𝑖)(1+𝑖) x $₀ =(1+𝑖)³ x $₀
### …
### $ₙ = (1 + i) x $ₙ ₋ ₁ = … = (1+i)ⁿ x $₀

### At each period t have a cash flow (CFₜ = $ₜ) that is fully reinvested with earned in the previous period: 
![[Pasted image 20251122125247.png]]

### The *discount factor* is a function of the interest rate (i) between today and tomorrow

### It's called *discount*, because you are *discounting* the future

### You can see the discount factor in this way:

### $₁ = (1 + i) x $₀, with i>0 
### ![[Pasted image 20251122125842.png]]
## PV is useful to compare various financial instruments
### Example:
Consider 2 financial instruments (for example: bonds, loans, etc. …): A and B
 ![[Pasted image 20251122130014.png]]
The interest rate is i = 0.1 (= 10%). Then:
	![[Pasted image 20251122130347.png]]
So at t=0, asset A is more valuable than asset B, even though the sum of cash flows is the same (800 in both cases)! Why?

## Debt instruments differ by:
### - streams of cash payments (cash flows)
### … and …
### - timing
### The evaluation of amounts at different points in the time is called **Present Value (PV) analysis**

### All present value calculations are of this kind:
### ![[Pasted image 20251122132139.png]]
### PV computes the value at time 0 (=present) of future cash flows

### In the previous formula cell:
### IF
### The price of the security (P) is equal to the Present Value (PV) of its future cash flows

### THEN
###  *i* is the yield-to-maturity (YTM) or simple the interest rate.
### ![[Pasted image 20251122132621.png]]
### <u>Definition: YTM is the interest rate that equates the PV of the cash flows with the value (price) of the debt instrument today</u>
### *Note that: i ≠ RATE OF RETURN*
### *We will see examples where i > 0 but Return < 0*

### In most finance applications:

### P = PV (cash flows)*, where P is the Security's Price*

### P = PV is true under certain assumption on investors' rationality and **efficiency** of financial markets
---
# Present Value: Applications
## Loans and Bonds:
- **LOANS** (ex.: mortgage)
- **BONDS** (ex.: Treasury or corporate bonds)
	1. Zero Coupon Bond (or Discount Bond)
		- No coupon
	2. Coupon Bond
		- With coupon

## Discount or Zero-Coupon Bond (ZCB)
### A ZCB (or irl: discount bond):
- **Definition:**
	- A bond that pays no periodic interest, is issued at a discount below its face value, and repays the full face value only at maturity
- Government bills are typically ZCBs
	- The US T-bills are the most widely traded discount bonds
- Example: 
	- Pay $0.95, get $1 at maturity ⇒ Earning = $0.05
- Example task:
	- Calculate the YTM for a zero-coupon that pays $0.95, get $1 at maturity (assume 1 year maturity). Intuitively:
	 ### ![[Pasted image 20251122143955.png]]
- The formula for calculating the price of a discount bond with 1 year maturity is:
	 ### ![[Pasted image 20251122144200.png]]
- The formula for calculating the price of a discount bond with n years maturity is:
	 ### ![[Pasted image 20251122145249.png]]
- Example for *n* year bond:
	- What is the YTM for a discount bond with 5 years maturity with a face value of $1000, selling at $750?
		- n = 5; FV = $1000; P = $750
		### ![[Pasted image 20251122145548.png]]
## Coupon Bonds
### A coupon bond:
- **Definition**:
	- A bond that makes a fixed payment at specific dates (coupons) plus a final amount (face value or par value) at maturity
	- The price today of a coupon bond is the PV of its future cash flows
- Considering 2 periods:
	 ![[Pasted image 20251122145816.png]]
	- Where *C* is the coupon payment, *FV* is the face value, *n* is the years to maturity, *i* is the YTM (*C* and *i* fixed over time)
- Considering many periods:
	- For example, a 10% coupon bond with a face value of $1000 and 10 years to maturity will have a cash flow of $100 each year plus a payment of $1000 at the end:
	 ![[Pasted image 20251122150128.png]]
- Generic formula of price of CB's:
     ![[Pasted image 20251122150225.png]]
	- *Note time convention: ∑ starts at t = 1 (assume buy coupon bond at t = 0, but the bond only starts paying the following year) and it ends at maturity n*
- **Coupon rate:** the amount it pays every year is expressed as a % of face value:
	 ![[Pasted image 20251122150606.png]]
	- If *P* = *FV* we have a par bond
	- If *P* **<** *FV* we have a bond at **discount**
	- If *P* **>** *FV* we have a bond at **premium**
- Examples of CBs (P, YTM, and coupon rate):
	- Q1: 
		If the YTM=11.75%, what is the price today of a “10% coupon bond” with a face value of $1000 and 10 years maturity?
		So, FV = $1000, i<sub>current</sub> = 10%, YTM = 11.75% 
	- A1: 
		First recover coupon value *C* : 
		### ![[Pasted image 20251122171511.png]]
		Then, calculate price of CB using PV of cash flows:
		### ![[Pasted image 20251122171639.png]]
		
		or
		
		### ![[Pasted image 20251122171953.png]]
	- Q2:
		A 3-year corporate bond has a face value of $1000 and a 7% coupon rate; the current market interest rate is 6%. What should be the bond's price?
		So n = 3, FV = $1000, icr = 0.07, i = 0.06
	- A2: 
		C = FV x Laurent</sub> = $1000 x 0.07 = $70
		P = $70/(1 + 0.06) + $70/(1 + 0.06)² + $70/(1 + 0.06)³ + $1000/(1 + 0.06)³ = $1026.73
- Special case: Perpetuity (or Consol)
	- It is a coupon bond providing a periodic coupon ***forever*** (=with no maturity date)
	- It is convenient in finance because it is easy to calculate the price (i.e. its PV)
		### ![[Pasted image 20251122183307.png]]
		Can see *immediately* inverse relation between ***P*** and ***i***
		It is a geometric series:
		![[Pasted image 20251122183505.png]]
	- How and when perpetuities exist?
		- UK government issued perpetual war bonds in WWI-WWII:
			- *“If you cannot fight, you can help your country by investing all you can in 5 percent Exchequer Bonds ... Unlike the soldier, the investor runs no risk.”*
		- These war bonds were redeemed by the UK government in October 2014
		- Other remaining perpetuities dating even further back (1850s) were redeemed in July 2015
		- Nowadays, perpetuities are issued by banks for regulatory purposes
## Current yield
- **Definition**:
	- The perpetuity allows us to introduce the concept of current **yield**:
		![[Pasted image 20251122184044.png]]
	- The current yield is a useful approximation to the YTM for long-term bonds, with **price near par**. The reason being that cash flows (CF) that are very distant in time have a low present value (PV), so a 30-year bond is pretty much like a perpetuity
- Example:
	- A perpetuity bond with P = $2000 and C = $100 has i<sub>current</sub> = $100 / $2000 = 0.05
		- A coupon bond with the same price and coupon, with **30 years** of maturity (and a FV of $2500) has i<sub>current</sub> = 0.05453
		- A coupon bond with the same price and coupon, with **50 years** of maturity (and a FV of $2500) has i<sub>current</sub> = 0.05115
		- A coupon bond with the same price and coupon, with **100 years** of maturity (and a FV of $2500) has i<sub>current</sub> = 0.05010
## Current yield and Coupon Rate
### Notice the distinction between:
### - The current yield (Coupon divided by the Price):
![[Pasted image 20251122192810.png]]

### - The coupon rate (Coupon divided by the Face Value)
![[Pasted image 20251122192909.png]]

### Of course for a par-bond, the two coincide (because P = FV)

### So what is more important, the YTM or the price?
- **Mathematically**, it doesn't matter: given one, the other one is determined via the PV formula
- **Economically**, we think of the **YTM determining the price**, not viceversa, because if we think of the YTM as the **"fair" return** an investor requires considering the risk. Then the investors will price the bonds so that in equilibrium they get this fair return

### When bond is at par (P = FV), YTM equals coupon rate
### **Price and yield are negatively related (VERY IMPORTANT!!!)**
### Yield greater than coupon rate when bond price is below par value

## Relationship between Price, YTM and Coupon rate

1) **When bond is at par, yield equals coupon rate.**
	1) Math: if P = FV, then i<sub>current</sub> and i<sub>coupon</sub> coincide
	2) Intuition: a par bond is like a bank account, if you put down $1000 (P) today (t=0) and you cash in the interest payment every year (C = $100), you are left with $1000 (FV) at maturity (say t=10) …
	3) … similar to coupon bond with *i* = 10% and 10 years maturity
2) **Price and yield are negatively related**
	1) If *i* increases, the PV of any given cash flow is lower; hence, the price of the bond must be lower
	2) a bit more obvious from perpetuity and zero-coupon bond formulas, but it emerges also from coupon bonds
3) **The YTM is greater than the coupon rate when bond price is below par value**
	1) According to (1): *if P = FV ⇒ i = C/FV*
	2) According to (2): *if ↑ then P ↓ *
	3) Putting (1) and (2) together, it must be that:
		*if i ↑ ⇒ YTM > i<sub>cr</sub> (= C/FV) and since P ↓ ⇒ P < FV*
	<center>What does this mean?</center>
	- If the <u>required yield on the bond is higher than what the bond actually pays</u> (that is, the coupon rate), then it needs **to sell at discount to attract investors** (=price is too high, not attractive!)
	- In other words, because investors can make a larger return the financial market (=other securities), they need an extra incentive to invest in the bond
## Real and Nominal Interest Rates
### The real interest rate (i<sub>r</sub>) is the nominal interest rate (i) adjusted for expected inflation (<u>expected changes in the price level</u>).
#### - From the Fischer equation:
<center>i<sub>r</sub> = i - π<sup>e</sup></center>

### Technically, this definition of i<sub>r</sub> is the ***ex-ante*** **real rate of interest** because it is adjusted for the ***expected*** level of inflation, π<sup>e</sup> 

### We can calculate the ***ex-post*** real rate based on the observed level of inflation (π)

### When the real rate (i<sub>r</sub>) is low:
#### - there are **greater** incentives to **borrow** (money is less costly)
#### - and **less** incentives to **lend** (money is not very profitable)

### In response to the Financial Crisis (2008), Fed & ECB turned <u>i = 0,</u> so <u>0>i<sub>r</sub></u> (inflation was low but still positive) to stimulate aggregate spending (consumption and investment)

### <u>Case of definition</u> (π<sup>e</sup><0):
#### - The real rate will always be positive: consider case of lowest i (i=0):
- i<sub>r</sub> = -π<sup>e</sup>>0 because π<sup>e</sup><0
#### - Deflation can be a big problem:
- Expectations of deflation lead to higher real rates and may cause deflationary spirals
- But some evidence says it is not so bad

### Do not hold bond until maturity
#### Let h = holding period and n = maturity
##### *So far mostly considered h = n (hold bond until maturity)*
##### *Now consider 2 cases where holding period ≠ maturity*
##### Case 1: you sell the bond at time t before maturity (n)
- Holding period is shorter than maturity (h<n)
- Need to consider the price of sale at time h (P<sub>h</sub> may be different from P<sub>0</sub>), because you don't get
	![[Pasted image 20251123192256.png]]
##### Case 2: you sell a bond at time t after maturity (n)
- Holding period shorter than maturity (h>n)
- Need to consider the price of the bond that you buy at time n (P<sub>n</sub> > or < P<sub>n</sub>)?
	![[Pasted image 20251123192655.png]]
## Relationship between Interest Rate and Rate of Return
### Interest Rate ≠ Rate of Return
### Rate of return
#### Suppose we buy a coupon bond, we hold it for only one period, and we don't keep it up to maturity, but we sell it before maturity (h<n)
- With sale before maturity, <u>price</u> may <u>change</u> (we don't wait to get FV)
- So, we need to consider the **<u>capital gain</u>** (say: if capital gain is negative, we may have a loss!)
#### The <u>the rate of return</u> on our investment is all the payments received during the holding period, divided by the initial price:
![[Pasted image 20251124130807.png]]
**where:**
*i*<sub>c</sub> = C / P<sub>t</sub> (current yield)
**and**
*g* = (P<sub>t+1</sub> - P<sub>t</sub>) / P<sub>t</sub> (capital gain)

### Example: Interest Rate ≠ Rate of Return
#### Assume you paid $1000 for a 10-year coupon bond with a FV of $1000, and a coupon rate of 10%. One year after the purchase, you sold the bond for:
##### a. $1200
##### b. $800
#### Q: 
##### Where is your *rate of return*? What is the (initial) YTM?
#### A:
##### C = i<sub>cr</sub> x FV = 0.1 x $1000 = $100
##### (a): Return = ($100 + ($1200 - $1000))/$1000 = $300/$1000 = 0.3 (read: 30%)
##### (b): Return = ($100 + ($800 - $1000))/$1000 = - $100/$1000 = - 0.1 (read: -10%)

##### YTM = *i*<sub>cr</sub> because bond is at par; YTM = 10%
##### So returns differ between (a) and (b), even though same YTM = 10%

#### What happened after one year?
##### By the time you wanted to sell the bond, its yield
- went down (=price went up) in case a
- went up (=price went down) in case b

##### Case a: new investors are willing to pay a higher price for a bond whose coupon rate (10%) is higher than current interest rates at prevailing market conditions
- reverse case in b

#### Let's see in the next table what happens to bonds' returns if the **interest rate increases**, depending on the bond *of different maturities*


### Key Facts about the Relationship between Rates and Returns

![[Pasted image 20251124132640.png]]

### Summary on the Relationship between Rates and Returns
#### Key findings from Table 3.2
#### 1. For bonds with holding period < maturity (h<n), i ↑ ⇒ P ↓, implying capital loss
#### 2. The longer the maturity, the greater the ∆P (and also the greater of ∆R) for any ∆*i*
#### 3. The only bond whose return = yield is the one with maturity = holding period (obvious: at maturity, no risk of capital gain/loss!)
#### 4. Even if a bond has a high initial interest rate, the <u>return</u> can turn <u>negative</u> if the *i*↑

## Interest Rate Risk
### For same ∆*i*↑, ∆P is more negative for L-T bonds … so prices are more "volatile" for long-term (L-T) bonds
- and thus, these bonds are riskier than short term bonds
### The risk of losing money (∆P<0) if interest rates change is called Interest Rate Risk (IRR)
### IRR comes from the fact that the bonds may be **sold before maturity** (h<n)
- In this case, you don't know the interest rate (and **hence the price**) will be at the time you want to sell it (t=h)
- It is very important for investors (and banks in particular) to manage IRR, not just from bonds, but also other securities
### So have IRR only for bonds whose holding period is shorter than maturity (h<n)
### No IRR for any bond whose maturity equals holding period (*i* = return): obvious! (h = n)
- Call this case as **hold-to-maturity** **(HTM)**
### Of course, we always have ALSO other risks:
- **default** risk
- **Inflation** risk {that's true of any investment in securities that pays a nominal return (some bonds are indexed with interest that adjusts with the inflation rate)}
## Reinvestment Risk
### If **the holding period is longer than maturity** (h > n), you don't have IRR, but you have **reinvestment risk**
- At the moment of reinvesting, you may fail to get the<u> same interest rate</u> as before!
- Coupon payments of a coupon bond are $'s that could/should be reinvested in other bonds. But the **future *i* is uncertain!**
### Q: 
#### Is it better to invest at time t in:
##### a. A 2-year bond with *i* = 10%, and re-invest the proceeds at *t* + 1 in another 1-year coupon bond with *i* = 10%? (*h>n*)
##### b. A 1-year bond with *i* = 10%, and re-invest the proceeds at t + 1 in another 1-year bond with *i* = 10% (*h>n*)?
#### ![[Pasted image 20251124142724.png]]
Uncertainty about *i*<sub>t</sub> at *t* = 0 determines Reinvestment risk

### A:
#### It depends:
##### In case a, h = 2 years, while n = 1 is 1 for year for each bond
##### In case b, if interest rate **falls/rises** in t + 1, you **lose/gain**: at the moment of reinvesting, you may fail to get the <u>same interest rate</u> as before!

## Duration
### Can we quantify the **IRR** of a bond?
#### - The further in the future the *payments* of a bond lie, the more the bond is exposed IRR

#### - Idea: we could use a measure of time of each payment (c.d. "Effective maturity") of a bond to quantify IRR
#### In practice: to construct this measure of "Effective maturity", for each period:
##### - 1<sup>st</sup>: Calculate the % of the total PV of a bond is contributed by cash flows in each year payments are due ( for example: 1, 2, etc.)
##### - 2<sup>nd</sup>: Use the weights to calculate a "weighted" maturity

#### **Duration:** weighted average of the maturities of the cash payments
##### - It is like an <u>effective maturity</u>
##### - Useful because it allows to *quantify* the IRR because the **longer** the duration, the **higher** the IRR!

### Intuition behind the measure of Duration:
#### - We want a measure of IRR
#### - Use the idea that the longer the maturity, the higher the IRR
#### - Two bonds <u>with the same original maturity</u> **do not** necessarily have <u>same</u> IRR
#### - Example ↑:
1. A zero-coupon bond (ZCB) makes all payments at the end
2. A coupon bond (CB) spreads them out in each period

##### Q:
###### Is the IRR (measured by the effective maturity) higher or lower for a ZCB with the <u>same</u> maturity of the coupon bond?

##### <sub></sub> A:
###### Higher for ZCB, because ZCB makes all payments at the end, while CB makes payments earlier than ZCB
### Formula for Duration
#### ![[Pasted image 20251125114028.png]]
#### Where: CP<sub>t</sub> = C for t < n; CP<sub>t</sub> = C + FV for t = n
#### Formula intuition: the *effective maturity* of coupon bonds is a <u>weighted average</u> of <u>effective maturities</u> on discount bonds
- Each coupon <u>payment</u> is like a discount bond
- The weights (α<sub>t</sub>) are equal to the proportion of the total value (in terms of PV) represented by each discount bond:
	 ![[Pasted image 20251125114514.png]]
- Duration of a ZCB is equal to its maturity (in fact: α<sub>t</sub> = 1)
	![[Pasted image 20251125114719.png]]
#### PV<sub>TOT</sub>=PV<sub>1</sub>+PV<sub>2</sub>+PV<sub>3</sub>+PV<sub>4</sub>
#### α<sub>1</sub> = PV / PV<sub>TOT</sub> … and so also α<sub>2</sub>, α<sub>3</sub>, α<sub>4</sub>
#### DUR<sub>1</sub> = α<sub>1</sub> x 1 … DUR<sub>4</sub> = α x 4
#### DUR<sub>t</sub> = DUR<sub>1</sub> + DUR<sub>2</sub> + DUR<sub>3</sub> + DUR<sub>4</sub>
##### - If the weights are the proportions of the total value (in terms of PV) represented by each discount bond, why is the duration **of a ZCB** equal to its maturity?

##### - Because having only one time in which payment takes place (say *t*), then: α<sub>t</sub> = 1 by definition

![[Pasted image 20251125120509.png]]

### Properties of Duration
![[Pasted image 20251125123617.png]]
#### Properties: DUR ↑ if:
##### 1. Maturity ↑
##### 2. *i*<sub>cr</sub>(=C/FV) ↓ (ZCBs have max duration = actual maturity because they pay all at the end)
##### 3. *i* ↓ sensitivity to changes in rates increases as rates fall (because duration is a linear approximation: as interest falls, discount the future less, far distant weights from now are higher)
##### Recall also:
###### a. for ZCB: Duration = Maturity
###### b. for CB: Duration < Maturity
### Duration and Interest-Rate Risk
#### - Recall that IRR is given by the price change of a coupon bond if *i* changes
#### - With the duration, we can <u>approximate</u> (for **small changes** in interest rate) the % price change with:
![[Pasted image 20251125124317.png]]
- Note: ∆*i* = *i*<sub>1</sub> - *i*<sub>0</sub> 
- The formula comes from a 1<sup>st</sup> Order Taylor approximation
##### Example: If *i*↑ from 10% to 11% for coupon bond with a duration of 6.76 years:
###### ∆i = 0.11 - 0.1 = 0.01
%∆P ≈ -6.76 x 0.01/(1+0.1) = - 0.0615 = -6.15%
#### - The **greater** the duration of a security, the **greater** the percentage change in the market value of the security (∆P) for a given change in interest rates (∆*i*)
#### - Therefore, <u>the greater the duration of a security, the greater its IRR</u>
#### - The duration is not quite the same as the IRR, but it measures its **intensity**!
### Exercise: Duration
#### Q:
##### A 5% coupon bond has a YTM of 6% and a price of $965. The interest rate then falls to 5.5%. The duration is 4 years. What is the new price?
#### A:
##### P = $983.2
##### Indeed:
##### ∆ i = 0.055 - 0.06 = - 0.005
##### 1 + i = 1 + 0.06 = 1.06
##### %∆P ≈ -DUR x ∆*i*/(1 + *i*) = -4 x (-0.005)/1.06 = 0.019
##### P<sub>1</sub> = P<sub>0</sub>(1 + 0.019) = $965 x 1.019 = $983.2
### Duration of a Portfolio
#### Consider not a single security, but a portfolio of securities
#### Duration is additive (∑)
##### - The duration of a <u>portfolio of securities</u> is the <u>weighted average of the durations</u> of the individual securities, with the **weights** equaling the <u>proportion of the portfolio value invested in each security</u>
##### - Example: If have *n* bonds in the portfolio:
- DUR<sub>portfolio</sub> = DUR<sub>1</sub> x w<sub>1</sub> + DUR<sub>2</sub> x w<sub>2</sub> + … + DUR<sub>n</sub> x w<sub>n</sub>
- Where w<sub>k</sub> is the weight of bond k over total balue of bonds in the portfolio
### Exercise: Duration of a Portfolio
#### Assume that you have a portfolio of 2 bonds
##### One has a duration of 3 years, and the other has a duration of 7 years
##### The <u>market values</u> of the bonds are $600 and $900, respectively
##### Both bonds have the face value of $1000
#### Q: What is the duration of your portfolio?
#### A:
##### DUR<sub>portfolio</sub> = 3 x $600/($600 + $900) + 7 x $900/($600 + $900) = 3 x 0.4 + 7 x 0.6 = 5.4 (years)

##### ==N.B.1:== The weights reflect the values (market prices) of the securities in the portfolio, not their face values
# Chapter 3 Summary
## 1. We examined how to price various debt instruments using the <u>Present Value</u> formula
## 2. We defined the YTM as the interest rate that makes the price of debt (P) equal to its PV
## 3. We defined the concept of the current yield = C/P
## 4. We discussed the relation between YTM, P and C
### Especially that YTM and P are negatively related!
## 5. We distinguished between <u>real</u> and <u>nominal</u> interest rate
## 6. We distinguished between *i* and rate of return and found out that only if we HTM the two coincide
## 7. Hence, we defined IRR, which makes instruments in L-T bonds risky
### And we have seen how to measure IRR using Duration
# Chapter 3 Exercises
## EX 1
### The price of a 3-year zero coupon bond with face value of $1,100 is $900. What is the yield-to-maturity? 
#### a) 1.9% 
#### b) 5.2% 
#### c) 3.6% 
#### ==d) None of the others==

#### FV = $1100
#### P = $900
#### n = 3
$$
YTM = \sqrt[3]{\frac{1100}{900}} = 1.069
$$
#### ⇒ r ≈ 0.069 = 6.9%
## EX 2
### Consider two securities with the same yield to maturity. Security A pays $1,150 four years from now, while security B pays $1,200 three years from now. Which of these two securities has a higher price? 
#### a) The answer is ambiguous and depends on the market interest rate 
#### b) Security A 
#### c) They have the same price 
#### ==d) Security B==

#### FV<sub>A</sub> = $1150
#### n<sub>A</sub> = 4
#### FV<sub>B</sub> = $1200
#### n<sub>B</sub> = 3
#### YTM<sub>A</sub> = YTM<sub>B</sub>
#### Having the same YTM, means that one of them should start from a lower price and build up to reach the other. Knowing that, we can assume that Security B has higher price.

## EX 3
### A bond with a face value of $2,000 and a coupon rate of 10% is selling for $2,200. Which of the following is true? 
#### a) the yield to maturity is 10.5% 
#### ==b) the yield to maturity is less than 10% ==
#### c) the yield to maturity is 10% 
#### d) the yield to maturity is 11%

#### FV = $2000
#### P = $2200
#### C = 10%
#### We can not determine the actual YTM since we do not know the years for maturity, but we know for sure that it will be less than the coupon rate.
## EX 4
### Consider a perpetuity with annual coupon of 𝐶, initial price 𝑃<sub>0</sub> and interest rate 𝑖<sub>0</sub>. If the interest rate doubles, what’s the new price 𝑃<sub>1</sub> of the perpetuity? 
#### a) 𝑃<sub>0</sub> ∗ 2 
#### b) 𝐶/2 
#### c) 𝑃<sub>0</sub> 
#### ==d) 𝑃0/2==

## EX 5
### Consider an annual coupon bond with a duration of 2 years. If the interest rate, which currently is 15%, raises to 16%, what will be the approximate percentage change in the bond's price?
#### a) The price will go down by 0.91% 
#### ==b) The price will go down by 1.74% ==
#### c) The price will go up by 0.91% 
#### d) The price will go down by 1.65%
#### ![[Pasted image 20251125124317.png]]

#### %∆P ≈ -2 x 0.01/(1 + 0.15)
#### ∆P ≈ −0.0174
#### %∆P ≈ -1.74%
## EX 6
### The price of a 5-year zero coupon bond with face value of $1,000 is $903. The current interest rate is 1.5%. What is the bond’s duration?
#### a) 1.82 
#### b) 2.21 
#### ==c) 5== 
#### d) Not enough information
#### n = 5
#### FV = $1000
#### P = $903
#### i<sub>cr</sub> = 1.5%
#### DUR = 5 (since it is a ZCB)

