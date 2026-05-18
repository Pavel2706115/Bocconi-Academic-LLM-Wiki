Class 30006 – Financial Markets and Institutions Università Commerciale Luigi Bocconi Fall 2025 Prof. Francesco Bripi 

# **Interest Rates and Valuation (Chapter 3)** 

**==> picture [360 x 192] intentionally omitted <==**

**----- Start of picture text -----**<br>
Copyright ©2015 Pearson Education, Ltd. All rights reserved.<br>**----- End of picture text -----**<br>


**==> picture [360 x 191] intentionally omitted <==**

**----- Start of picture text -----**<br>
2-1<br>**----- End of picture text -----**<br>


# **Interest rates variation over time** 

**==> picture [719 x 360] intentionally omitted <==**

**==> picture [68 x 44] intentionally omitted <==**

## **Chapter Preview** 

Interest rates are among the most closely watched variables in the economy. 

This lecture: Lots of definitions and (some) math. 

**IMPORTANT: LEARN by UNDERSTANDING, DO NOT LEARN BY HEART!** 

## **Topics** 

1. Present value 

2. Yield to maturity 

3. Zero coupon bonds 

4. Coupon bonds 

5. Perpetuity 

6. Nominal Vs real interest rate 

7. Rate of return and interest rate risk 

8. Duration 

## **Present Value: Introduction** 

Suppose we have 100€ and 50$. What is our total wealth? 

100€ + 50$ = ?? 

We need an exchange rate to express everything in a common unit (base currency) 

× 100€ + 50$ (0.84 €/$)=142€ 100€×(1.19 $/€) + 50$=169$ 

Now consider 1$ today (t=0) and 1$ tomorrow (t=1): 1$0 + 1$1= **??** No change of currency, but change of **time** ! 

## **Present Value: Introduction** 

- Consider a 1$ today (t=0) and a 1$ tomorrow (t=1) 

- 1$ today (time t=0: $0) is **NOT** equal to 1$ tomorrow (time t=1: $1). 

## Why? 

- Presumably 1$ today is better than a 1$ tomorrow,  because: a. the future is uncertain b. people are impatient 

- To find the value of $0 corresponding $1 we need a conversion rate 

- (or a sort of “ _exchange_ rate”) between today and tomorrow ($0 /$1): **discount factor** 

## **Present Value: Introduction** 

## **Discount factor** 

 Invest 1 today, get (1+ 𝑖 ), with 𝑖 >0 tomorrow. Hence: 

$1= (1+ 𝑖 )$0 , with 𝑖 >0 

- $1= (1+ 𝑖 )$0 

- $2= (1+ 𝑖 )$1 = (1+ 𝑖 )(1+ 𝑖 )$0 = (1+ 𝑖 )[2] $0 

- $3= (1+ 𝑖 )$2 = (1+ 𝑖 )(1+ 𝑖 )(1+ 𝑖 )$0 =(1+ 𝑖 )[3] $0 

_…_ $ _n_ = (1+ 𝑖 )$n-1 = … =(1+ 𝑖 ) _[n]_ $0 

At each period t have a cash flow ( 𝐶𝐹𝑡 = $𝑡) that is fully reinvested with interest earned in the previous period: 

**==> picture [542 x 92] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝐶𝐹 𝐶𝐹 𝐶𝐹 𝐶𝐹 𝐶𝐹<br>1 2 3 𝑛−1 𝑛<br>$1 $2 $3 $n-1 $n<br>0 1 2 3 n-1 n t<br>**----- End of picture text -----**<br>


**==> picture [659 x 22] intentionally omitted <==**

**----- Start of picture text -----**<br>
Copyright ©2015 Pearson Education, Ltd. All rights reserved. 2-7<br>**----- End of picture text -----**<br>


## **Present Value: Introduction** 

## **Discount factor** 

- the _discount factor_ is a function of the **interest rate** ( 𝑖 ) between today and tomorrow 

- it’s called _discount_ because you are _discounting_ the future 

- can see the discount factor in this way: $1= (1+ 𝑖 )$0 , with 𝑖 >0 

$0 1 = (1 period) 1+𝑖[= 𝛿] $1 $0 = $0 ∙ $1 = 1 $1 = 1 1 1 (2 periods) 1+𝑖[∙] 1+𝑖[∙] 1+𝑖[=] 1+𝑖[𝟐][= 𝛿][𝟐] $2 $1 $2 $2 $0 = $0 ∙ $1 ∙ $2 = 1 $2 = 1 1 1[∙][∙] (3 periods) 1+𝑖[2] 1+𝑖[2] 1+𝑖[=] 1+𝑖[𝟑][= 𝛿][𝟑] $3 $1 $2 $3 $3 … … $0 = $0 ∙⋯∙ $n−1 = 1[∙] $n−1 = 1[∙] 1 1 1+𝑖[𝑛−1] 1+𝑖[𝑛−1] 1+𝑖[=] 1+𝑖[𝒏][= 𝛿][𝒏][(] _[n]_[ periods)] $ n $1 $n $n 

## **Present Value: Introduction** 

## PV useful to compare various financial instruments 

 EX: consider 2 financial instruments (4 ex.: bonds, loans, etc…): A and B 

200 200 200 200 

Asset A: 

Asset B: 

**==> picture [10 x 26] intentionally omitted <==**

**==> picture [10 x 26] intentionally omitted <==**

**==> picture [10 x 26] intentionally omitted <==**

**==> picture [10 x 26] intentionally omitted <==**

**==> picture [9 x 27] intentionally omitted <==**

**==> picture [190 x 15] intentionally omitted <==**

**==> picture [40 x 21] intentionally omitted <==**

**==> picture [41 x 21] intentionally omitted <==**

**==> picture [40 x 21] intentionally omitted <==**

**==> picture [40 x 20] intentionally omitted <==**

50 50 50 650 _0 1 2 3 4_ 

**==> picture [40 x 21] intentionally omitted <==**

**==> picture [41 x 21] intentionally omitted <==**

**==> picture [40 x 21] intentionally omitted <==**

**==> picture [40 x 21] intentionally omitted <==**

**==> picture [6 x 13] intentionally omitted <==**

**==> picture [6 x 13] intentionally omitted <==**

## The interest rate is 𝑖= 0.1 = 10% . Then: 

200 200 200 200  𝑃𝑉𝐴,𝑇𝑂𝑇 =[+][+][= 634 ≠] 200 + 200 + 200 + 200 1.1[+] 1.1[2] 1.1[3] 1.1[4] 50 50 50 650  𝑃𝑉𝐵,𝑇𝑂𝑇 =[+][+][= 568.3 ≠] 50 + 50 + 50 + 650 1.1[+] 1.1[2] 1.1[3] 1.1[4]  So at _t=0_ , asset A is more valueable than asset B, even though sum of Copyright ©2015 Pearson Education, Ltd. All rights reserved.cash flows is the same (800 in both cases)! _Why?_ 

## **Present Value: Introduction** 

Debt instruments differ by: 

- streams of cash payments ( **cash flows** ) 

… and … 

- timing 

The **evaluation** of amounts at different points in time is called _**Present Value (PV)** analysis_ 

All present value calculations are of this kind: 

**==> picture [355 x 52] intentionally omitted <==**

PV computes the value at time 0 (=present) of future cash flows 

## **Present Value: Introduction** 

In previous formula we call 𝑖 the **yield-to-maturity (YTM)*** or simply **interest rate** 

## _**IF**_ 

the price of the security ( _P_ ) is equal to the Present Value ( _PV_ ) of its future cash flows 

if 𝑃= 𝑃𝑉→𝑖= 𝑌𝑇𝑀 

Definition: _YTM is the interest rate that equates the PV of the cash flows with the value (price) of the debt instrument today_ 

_Note that:_ _**i**_ **≠ RATE OF RETURN** We will see examples where _**i**_ >0 but Return<0 

*: think of YTM as the int. rate that allows to make PV of an asset until maturityCopyright ©2015 Pearson Education, Ltd. All rights reserved. 

## **Present Value: Introduction** 

In most finance applications: 

_P=PV(cash flows)_ 

where P is the Security’s Price P=PV is true under certain on investors’ assumption rationality and **efficiency** of financial markets 

We will see this later in the course … 

- … for now, just assume it: financial markets are efficient 

## **Present Value: Applications** 

- There are two basic types of debt instruments which incorporate present value concepts: 

   - **LOANS** (for ex.: mortgages) 

   - **BONDS** (for ex.: Treasury or corporate bonds) 

- We’ll only look at bonds in this class (examples with loans in the book). In particular: **1. Zero Coupon Bond (or Discount Bond)** `o` No coupon 

- **2. Coupon Bond** `o` With coupon 

## **Coupon and Zero-coupon bonds** 

**==> picture [264 x 358] intentionally omitted <==**

**==> picture [316 x 220] intentionally omitted <==**

Zero Coupon bond from US Treasury 

## Coupon bond from US Treasury 

## **Discount or Zero-Coupon Bond (ZCB)** 

A ZCB (or call ir **discount bond** ): 

- does _not_ give _any_ interest (coupon) payments before maturity =zero- 

- ( coupon _) …_ 

- … but it only pays the face value ( _FV_ ) to the holder of the bond at the end (=maturity) 

## **Discount or Zero-Coupon Bond (ZCB)** 

A ZCB (or call ir **discount bond** ): 

- does _not_ give _any_ interest (coupon) payments before maturity =zero- 

- ( coupon _) …_ 

- … but it only pays the face value ( _FV_ ) to the holder of the bond at the end (=maturity) 

- It normally sells at a price _below_ the face value (at discount) 

- Ex: pay $0.95 today, get $1 at maturity. Earning=$0.05. YTM? 

## **Discount or Zero-Coupon Bond (ZCB)** 

A ZCB (or call ir **discount bond** ): 

- does _not_ give _any_ interest (coupon) payments before maturity 

   - =zero- 

   - ( coupon _) …_ 

- … but it only pays the face value ( _FV_ ) to the holder of the bond at the end (=maturity) 

- It normally sells at a price _below_ the face value (at discount) 

- Ex: Calculate the **YTM** for a zero-coupon that pays $0.95 today, get $1 at maturity (assume 1 year maturity). Intuitively: 

1−0.95 𝑖= 0.95[= 0.053][ (read: 5.3%)] 

𝐹𝑉−𝑃 So, formula is: 𝑖= 𝑃 

- Government bills are typically ZCBs 

`o` Copyright ©2015 Pearson Education, Ltd. All rights reserved.The US T-bills are the most widely traded discount bonds 

## **Discount or zero-coupon Bond** 

##  Price of a discount bond with **1** year maturity: 

𝐹𝑉−𝑃 𝐹𝑉 𝐹𝑉 𝐹𝑉 𝑖= ⟹𝑖= 𝑃 𝑃[−1 ⟹1 + 𝑖=] 𝑃[⟹𝑃=] 1 + 𝑖 

## **Discount or zero-coupon Bond** 

##  Price of a discount bond with **1** year maturity: 

**==> picture [468 x 43] intentionally omitted <==**

##  Price of a discount bond with _**n**_ years maturity instead: 

**==> picture [611 x 130] intentionally omitted <==**

## **Discount or zero-coupon Bond** 

##  Price of a discount bond with **1** year maturity: 

**==> picture [468 x 43] intentionally omitted <==**

##  Price of a discount bond with _**n**_ years maturity instead: 

**==> picture [250 x 68] intentionally omitted <==**

**==> picture [611 x 50] intentionally omitted <==**

`o` _Example_ : what is the YTM for a discount bond with 5 years maturity with a face value of $1,000, selling at $750? 

**==> picture [257 x 19] intentionally omitted <==**

**==> picture [659 x 50] intentionally omitted <==**

## **Coupon Bonds** 

## A **coupon bond** 

- is a bond that makes a fixed payment at specific dates (coupons) plus a final amount (face value or par value) at maturity 

- The price today of a coupon bond is the PV of its future cash flows 

- Consider _**2**_ periods: 

𝐶 𝐶 𝑭𝑽 𝑃=[+] 1 + 𝑖[+] 1 + 𝑖[2] 𝟏+ 𝒊[𝟐] 

`o` where 𝐶 is the coupon payment, 𝐹𝑉 is the face value, 𝑛 the years to maturity, _i_ is the **YTM** ( 𝐶 , 𝑖 fixed over time) 

## **Coupon Bonds** 

 Consider **many** periods. For ex., a 10% coupon bond with a face value of $1,000 and 10 years to maturity will have a cash flow of $100 each year plus a payment of $1,000 at the end: 

𝐶 𝐶 𝐶 𝑪 𝑭𝑽 𝑃=[+][+ ⋯+] 1 + 𝑖[+] 1 + 𝑖[2] 1 + 𝑖[3] 𝟏+ 𝒊[𝟏𝟎][+] 𝟏+ 𝒊[𝟏𝟎] $100 $100 $100 $𝟏𝟎𝟎 $𝟏, 𝟎𝟎𝟎 𝑃=[+][+ ⋯+] 1 + 𝑖[+] 1 + 𝑖[2] 1 + 𝑖[3] 𝟏+ 𝒊[𝟏𝟎][+] 𝟏+ 𝒊[𝟏𝟎] Generic formula of price of CB’s: 𝐶 𝐹𝑉 𝑃= σ𝑛𝑡=𝟏 (1+𝑖)[𝑡][+] (1+𝑖)[𝑛] 

##  Generic formula of price of CB’s: 

`o` Note time convention: Σ starts at 𝑡= 𝟏 (assume buy coupon bond at 𝑡= 0 , but bond only starts paying the following year) and it ends at 𝑛 maturity 

## **Coupon Bonds** 

## _**Useful terminology**_ 

- _**Coupon rate**_ : the amount it pays every year is expressed as a % of face value: 

𝐶𝑜𝑢𝑝𝑜𝑛 𝐶 = 𝑖 𝑐𝑜𝑢𝑝𝑜𝑛𝑟𝑎𝑡𝑒 𝐹𝑎𝑐𝑒𝑉𝑎𝑙𝑢𝑒[=] 𝑭𝑽 

 If 𝑃= 𝐹𝑉 we have a **par bond** 

- If 𝑃< 𝐹𝑉 we have a bond **at discount** 

 If 𝑃 > 𝐹𝑉 we have a bond **at premium** 

## **CBs Example: P, YTM and coupon rate** 

Recall the previous example: 𝐶 𝐶 𝐶 𝐹𝑉 𝑃=[+ ⋯+][+] 1 + 𝑖[+] (1 + 𝑖)[2] (1 + 𝑖)[10] (1 + 𝑖)[10] **Q:** if the YTM=11.75%, what is the price today of a “10% coupon bond” with a face value of $1,000 and 10 years maturity? 

## **CBs Example: P, YTM and coupon rate** 

## Recall the previous example: 

**==> picture [372 x 43] intentionally omitted <==**

**Q:** if the YTM=11.75%, what is the price today of a “10% coupon bond” with a face value of $1,000 and 10 years maturity? 

## **A:** First recover coupon value 𝐶 : 

𝐶 𝑖 = 𝑐𝑜𝑢𝑝𝑜𝑛𝑟𝑎𝑡𝑒 𝐹𝑉[⟹𝐶= 𝑖][𝑐𝑟][× 𝐹𝑉⟹𝐶= 0.1 × $1,000 = $100] 

## Then, calculate price of CB using PV of cash flows: 

**==> picture [659 x 160] intentionally omitted <==**

## **CBs Example: P, YTM and coupon rate** 

A 3-year corporate bond has a face value of $1,000 and a 7% coupon rate; the current market interest rate is 6%. [ 𝑛= 3; 𝐹𝑉= $1,000; 𝑖𝑐𝑟 = 0.07; 𝑖= 0.06] 

**Q** : What should be the bond's price? 

## **CBs Example: P, YTM and coupon rate** 

A 3-year corporate bond has a face value of $1,000 and a 7% coupon rate; the current market interest rate is 6%. [ 𝑛= 3; 𝐹𝑉= $1,000; 𝑖𝑐𝑟 = 0.07; 𝑖= 0.06] 

**Q** : What should be the bond's price? 

**R** : Recall: 

𝐶 = `o` 𝑖 𝑐𝑟 𝐹𝑉[; 𝐶= 𝑖][𝑐𝑟][× 𝐹𝑉= 0.07 × $1,000;𝐶= $70] 

$70 $70 $70 $1,000 𝑃=[+][+][= $1,026.73] 1.06[+] (1.06)[2] (1.06)[3] (1.06)[3] `o` So 𝑃= $1,026.73 

## **Special case of CB: Perpetuity** 

## A special case of a coupon bond is a **perpetuity** (or **consol** ) 

- It is a coupon bond providing a periodic coupon _**forever**_ (=with no maturity date) 

- It is convenient in finance because it is easy to calculate its price ( _i.e._ its present value) 

**==> picture [659 x 264] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝐶 1 𝐶 𝑪<br>𝑃𝑉= σ∞𝑡=1 ∞<br>1+𝑖 [𝑡] [= 𝐶σ][𝑡=1] 1+𝑖 [𝑡] [=] 𝑖 [⟹𝑷𝑽=] 𝒊<br>o can see  immediately inverse relation btw  𝑷 and  𝒊<br>Why? If you like math here is why. It is a geometric series:<br>1<br>∞ 𝑡 ∞ 𝑡<br>1 + 𝑥+ 𝑥 [2] + +𝑥 [3] … = σ𝑡=0 𝑥 = 1 + σ𝑡=1 𝑥 = for  |𝑥| < 1<br>1−𝑥<br>1<br>Set  𝑥=<br>1+𝑖 [, then:]<br>1 1 1 1+𝑖 1<br>σ∞𝑡=1 ∞ 1 −1 =<br>1+𝑖 [𝑡] [= σ][𝑡=][0] 1+𝑖 [𝑡] [−1][ =] 1− 𝑖 [−1 =] 𝑖<br>1+𝑖<br>Copyright ©2015 Pearson Education, Ltd. All rights reserved. 2-28<br>**----- End of picture text -----**<br>


- Why? If you like math here is why. It is a geometric series: 

## **Do perpetuities exist?** 

#  UK government issued perpetual war bonds in WWIWWII: 

   - “ _If you cannot fight, you can help your country by investing all you can in 5 per cent Exchequer Bonds ... Unlike the soldier, the investor runs no risk._ ” 

- These war bonds were redeemed by the UK government in October 2014 

- Other remaining consols dating even further back (1850s) were redeemed in July 2015 

- Nowadays perpetuities are issued by banks for regulatory purposes 

## **Current yield** 

##  The perpetuity allows us to introduce the concept of **current** : **yield** 

𝐶 = 𝑖 𝑐𝑢𝑟𝑟𝑒𝑛𝑡 𝑃 

- The current yield is a useful approximation to the YTM for long-term bonds, with price near par. 

- Why? Because CF very distant in time have a low PV, so a 30-year bond is pretty much like a perpetuity! 

## : _Example_ 

- $100 

- i. 𝑖 = a perpetuity bond with P=$2,000 and C=$100 has 𝑐𝑢𝑟𝑟𝑒𝑛𝑡 $2,000[[= 0.05]][[ (][=5]][[=5]] 

- ii. a coupon bond with same price and coupon, with **30** years of maturity (and a FV=$2,500) has…………………………………………. _i_ = 5.354% 

- iii. a coupon bond similar to above with **50** years maturity: _i_ = 5.115%; iv. a coupon bond similar to above with **100** ys maturity: _i_ = 5.010% v. … and so on 

- Copyright ©2015 Pearson Education, Ltd. All rights reserved. 

$2,000[[= 0.05]][[ (][=5]][[=5]] %) 

## **Current yield and Coupon Rate** 

## Notice the distinction between 

- The _**current yield**_ (Coupon divided by the Price): 

𝐶 = 𝑖 𝑐𝑢𝑟𝑟𝑒𝑛𝑡 𝑷  The _**coupon rate**_ (Coupon divided by the Face Value) 𝐶 = 𝑖 𝑐𝑜𝑢𝑝𝑜𝑛 𝑭𝑽 

- of course for a _par-bond_ the two coincide (bcs 𝑃= 𝐹𝑉 ). 

   - Copyright ©2015 Pearson Education, Ltd. All rights reserved. **Learn these definitions well so avoid confusion later!** 

## **YTM and Price** 

## So what is more important, the YTM or the price? 

- mathematically, it does not matter: given one, the other one is determined via the PV formula 

- but economically we think of the YTM determining the price, not viceversa. 

- Why? Think about the YTM as the **“fair” return** an investor **requires** considering the risk 

- Then the investors will price the bonds so that in equilibrium they get this fair return 

## **Relationships between Price, YTM and Coupon rate** 

**Table 3.1** Yields to Maturity on a 10% Coupon rate bond, maturing in 10 years (Face Value = $1,000) 

**==> picture [656 x 157] intentionally omitted <==**

## Three interesting facts in Table 3.1: 

**1. When bond is at par** (P=FV) **, YTM equals coupon rate** 

**2. Price and yield are negatively related (VERY IMPORTANT!)** 

**3. Yield greater than coupon rate when bond price is below par value** 

## **Relationships between Price, YTM and Coupon rate** 

. **1) When bond is at par, yield equals coupon rate** 𝐶 𝐶 = = `o` math: if 𝑃= 𝐹𝑉, then 𝑖𝑐𝑢𝑟𝑟𝑒𝑛𝑡 𝑃[and][ 𝑖][𝑐𝑜𝑢𝑝𝑜𝑛] 𝐹𝑉[coincide] `o` intuition: a _par bond_ is like a bank account, if you put down $1,000 ( _P_ ) today ( _t=0_ ) and you cash in the interest payment every year ( _C_ =$100), you are left with $1,000 (FV) at maturity (say _t=10_ ) … 𝐶 $100 `o` … similar to bond with 𝑖 = 10% and 10 coupon 𝐹𝑉[=] $1,000[= 0.1] years maturity 

## **2) Price and yield are negatively related** 

`o` **If** _**i**_ **increases, the PV of any given cash flow is lower; hence, the price of the bond must be lower** 

`o` a bit more obvious from perpetuity and zero-coupon bond formulas, but it emerges also from coupon bonds 

## **Relationships between Price, YTM and Coupon rate** 

## **3) The YTM is greater than the coupon rate when bond price is below par value** 

- 𝐶 

- `o` According to (1): 𝑖𝑓𝑃= 𝐹𝑉⇒𝑖= 𝐹𝑉 

- `o` According to (2): 𝑖𝑓𝑖↑𝑡ℎ𝑒𝑛𝑃↓ 

- `o` Putting (1) and (2) together, it must be that: 

𝐶 𝑌𝑇𝑀> 𝑖 = ~~തതതത 𝑎𝑛𝑑𝑠𝑖𝑛𝑐𝑒𝑃↓⇒𝑃< 𝐹𝑉~~ 𝑖𝑓𝑖↑⇒ 𝑐𝑟 𝐹𝑉 

## What does this mean? 

- If the required yield on the bond is higher than what the bond actually pays (that is, the coupon rate), then it needs **to sell at discount to attract investors** (=price is too high, not attractive!) 

- In other words, because investors can make a larger return the financial market (=other securities), they need an extra incentive to 

- Copyright ©2015 Pearson Education, Ltd. All rights reserved.invest in the bond 2-35 

## **Real and Nominal Interest Rates** 

- The **real interest rate** ( _ir_ ) is the nominal interest rate ( _i_ ) adjusted for **expected inflation** (expected changes in the price level). 

   - From the Fisher equation: 

**==> picture [104 x 41] intentionally omitted <==**

- Technically, this definition of _ir_ is the _**ex-ante**_ **real rate of interest** because it is adjusted for the _**expected**_ level of inflation, p _[e]_ 

- We can calculate the _**ex-post**_ real rate based on the p 

- observed level of inflation ( ) 

## **Real and Nominal Interest Rates** 

- When the real rate ( _ir_ ) is low: 

   - there are **greater** incentives to **borrow** (money is less costly) 

`o` and **less** incentives to **lend** (money is not very profitable) 

- In response to the Financial Crisis (2008), Fed & ECB turned = 

- 𝑖 0 so 𝑖 < 0 was low but to stimulate , ~~𝑟~~ (inflation still positive) 

- aggregate spending (consumption and investment) 

- _Case of Deflation_ (p _[e] <0_ ): 

   - 𝑖 𝑖= 0 : 

   - the real rate will always be positive: consider case of lowest  𝑖 =-p _[e]_ >0 bcs p _[e]_ <0 𝑟 

   - Deflation can be a big problem: 

      - expectations of deflation lead to higher real rates and may cause deflationary _spirals_ : The Economist, 07 Jan 2015 

      - but some evidence says it is not so bad: CEPR, Jan 2022 

## **Do not hold bond until maturity** 

# Let ℎ= holding period and 𝑛= maturity 

 _So far mostly considered_ ℎ= 𝑛 _(hold bond until maturity)_ 

- _Now consider 2 cases where_ holding period ≠ maturity 

- Case **1** : you sell the bond at time 𝑡 **before** maturity ( 𝑛 ) `o` holding period shorter than maturity ( 𝒉< 𝒏 ) 

`o` need consider price of sale at time ℎ ( 𝑃ℎ may be different from 𝑃0 ), bcs do not get FV 

**==> picture [517 x 73] intentionally omitted <==**

**----- Start of picture text -----**<br>
20 20 120<br>0 1 2 ℎ 𝑛 t<br>**----- End of picture text -----**<br>


- Case **2** : you sell bond at time 𝑡 **after** maturity ( 𝑛 ) 

- `o` holding period shorter than maturity ( 𝒉> 𝒏 ) 

`o` 𝑛 𝑃 > 𝑜𝑟< 𝑃 ? need consider price of bond you buy at time ( 0 𝑛 ) 

**==> picture [659 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
20 20 120<br>0 1 2 𝑛 ℎ t<br>Copyright ©2015 Pearson Education, Ltd. All rights reserved. 2-38<br>**----- End of picture text -----**<br>


## **Interest Rate ≠ Rate of Return** 

## **Rate of return** 

- we we one 

- Suppose buy a coupon bond, hold it for only period and we don’t keep it up to maturity, but we **sell it before maturity (** 𝒉< 𝒏 **)** 

`o` with sale _before_ maturity, price may change (we don’t wait to get FV) `o` so, we need to consider the **capital gain** (say: if cap. gain is negative, we may have a loss!) 

- The _rate of return_ on our investment is all the payments received during the holding period, divided by the initial price: 

## where : 

𝐶 = 𝑖 𝑐 𝑃 𝑡 

𝐶+𝑃 −𝑃 𝐶 𝑃 −𝑃 𝑡+1 𝑡 𝑡+1 𝑡 = 𝑅𝑒𝑡𝑢𝑟𝑛= = 𝑖 𝑐 + 𝑔 𝑃 𝑃 𝑃 𝑡 𝑡[+] 𝑡 (current yield) 

and 

𝑃𝑡+1−𝑃𝑡 Copyright ©2015 Pearson Education, Ltd. All rights reserved. 𝑔= 𝑃 𝑡 

(capital gain) 

## **Example: Interest Rate ≠ Rate of Return** 

Assume you paid $1,000 for a 10-year coupon bond with a face value of $1,000, and a coupon rate of 10%. One year after the purchase, you sold the bond for: a. $1,200 b. $   800 

**Q** : What is your _rate of return_ ? What is the (initial) YTM? 

## **Example: Interest Rate ≠ Rate of Return** 

Assume you paid $1,000 for a 10-year coupon bond with a face value of $1,000, and a coupon rate of 10%. One year after the purchase, you sold the bond for: a. $1,200 

b. $   800 

**Q** : What is your _rate of return_ ? What is the (initial) YTM? **A:** 𝐶= 𝑖𝑐𝑟 × 𝐹𝑉= 0.1 × $1,000 = $100 

$100+ 1,200−$1,000 $300 = _(a):_ 𝑅𝑒𝑡𝑢𝑟𝑛= 0.3 read: 30% $1,000 $1,000[=] $100+ $800−$1,000 $100 _(b):_ 𝑅𝑒𝑡𝑢𝑟𝑛= = − read: −10% $1,000 $1,000[=][ −0.1] = 𝑌𝑇𝑀 𝑖 bcs bond is at 𝑐𝑟 par; YTM=10% So returns differ between (a) and (b), even though same 𝑌𝑇𝑀= 10% Copyright ©2015 Pearson Education, Ltd. All rights reserved. 

## **Example: Interest Rate ≠ Rate of Return** 

What happened after one year? 

 by the time you wanted to sell the bond, its yield `o` went **down** (=price went up)       in case a `o` went **up** (=price went down)   in case b 

- Case a: new investors are willing to pay a higher price for a bond whose coupon rate (10%) is higher than current interest rates at prevailing market conditions `o` reverse in case b 

- Let’s see in the next table what happens to bonds’ returns if **the interest rate increases** on the bond , depending 

- _different maturities_ 

## **Key Facts about the Relationship between Rates and Returns** 

**Table 3.2 One-Year Returns** on 10% Coupon Par Bonds (FV=$1,000) **When interest rate rises from 10% to 20%** 

**==> picture [569 x 292] intentionally omitted <==**

Recall the coupon bond formula and return formula: 𝑃= σ𝑛𝑡=1 𝐶 𝐹𝑉 𝑅𝑒𝑡𝑢𝑟𝑛= 𝐶+𝑃𝑡+1−𝑃𝑡 = 𝑖𝑐 + 𝑔 1+𝑖[𝑡][+] 1+𝑖[𝑛] 𝑃𝑡 

## **Key Facts about the Relationship between Rates and Returns** 

**Table 3.2 One-Year Returns** on 10% Coupon Par Bonds (FV=$1,000) **When interest rate rises from 10% to 20%** 

**==> picture [569 x 292] intentionally omitted <==**

Recall the coupon bond formula and return formula: 𝑃= σ𝑛𝑡=1 𝐶 𝐹𝑉 𝑅𝑒𝑡𝑢𝑟𝑛= 𝐶+𝑃𝑡+1−𝑃𝑡 = 𝑖𝑐 + 𝑔 1+𝑖[𝑡][+] 1+𝑖[𝑛] 𝑃𝑡 

## **Summary on relationship between rates and returns** 

Key findings from Table 3.2 

1. For bonds with holding period < maturity ( ℎ< 𝑛 ), 𝑖↑⇒𝑃↓ implying capital loss 

   - ∆𝑅 ) for any ∆𝑖 

3. The only bond whose return = yield is the one with maturity = holding period (obvious: at maturity, no risk of capital gain/loss!) 

4. Even if a bond has a high initial int. rate, the return can turn if _i_  

negative 

## **Interest Rate Risk** 

- For the same Δ _i_  Δ _P ,_ is more negative for L-T bonds … so 

- prices are **more “volatile” for long-term (L-T)** bonds `o` and thus, these bonds are riskier than short term bonds 

- The risk of losing money ( Δ𝑃< 0 _)_ if interest rates change is called **Interest Rate Risk (IRR)** 

- IRR comes from the fact that the bonds may be **sold before maturity** ℎ< 𝑛 

`o` in this case you don’t know what the interest rate (and **hence the price** ) will be at the time you wan to sell it 𝑡= ℎ 

`o` it is very important for investors (and banks in particular) to manage IRR, not just from bonds, but also other securities 

## **Interest Rate Risk** 

- So have IRR only for bonds whose holding period is shorter than maturity ℎ< 𝑛 

- No IRR for any bond whose maturity equals holding period ( _i_ =return): obvious! ℎ= 𝑛 

   - call this case as **hold-to-maturity (HTM)** 

- Of course, we always have ALSO other risks: `o` _**default** risk_ 

   - _**inflation** risk_ [that’s true of any investment in securities that pays a nominal return (some bonds are indexed with interest that adjusts with inflation rate)] 

## **Reinvestment Risk** 

 If ℎ> 𝑛 **holding period is longer than maturity** , you don’t have IRR, but you have **reinvestment risk** `o` at the moment of reinvesting, you may fail to get the same interest rate as before! `o` coupon payments of a coupon bond are $’s that could/should be re-invested in other bonds. But the **future** _**i**_ **is uncertain** ! 

## **Reinvestment Risk** 

- If ℎ> 𝑛 **holding period is longer than maturity** , you 

- don’t have IRR, but you have **reinvestment risk** `o` at the moment of reinvesting, you may fail to get the same interest rate as before! 

`o` coupon payments of a coupon bond are $’s that could/should be re-invested in other bonds. But the **future** _**i**_ **is uncertain** ! 

- **Q** : Is it better to invest at time _t_ in: a. a **2** -year coupon bond with 𝑖= 10% with ℎ= 𝑛 _or_ 

- b. a **1** -year coupon bond with 𝑖= 10% , and re-invest the proceeds at 𝑡+ 1 in another 1-year coupon bond with 𝑖= 10% ? ( ℎ> 𝑛 )? 

**==> picture [434 x 113] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑃 𝑃<br>1 2<br>0 𝑛= 1 ℎ= 2 t<br>**----- End of picture text -----**<br>


Uncertainty about 𝑖1 at 𝑡= 0 determines Reinvestment risk Copyright ©2015 Pearson Education, Ltd. All rights reserved. 

## **Reinvestment Risk** 

 If ℎ> 𝑛 **holding period is longer than maturity** , you don’t have IRR, but you have **reinvestment risk** `o` at the moment of reinvesting, you may fail to get the same interest rate as before! 

`o` coupon payments of a coupon bond are $’s that could/should be re-invested in other bonds. But the **future** _**i**_ **is uncertain** ! 

- **Q** : Is it better to invest at time _t_ in: a. a **2** -year coupon bond with 𝑖= 10% with ℎ= 𝑛 _or_ 

- b. a **1** -year coupon bond with 𝑖= 10% , and re-invest the proceeds at 𝑡+ 1 in another 1-year coupon bond with 𝑖= 10% ? ( ℎ> 𝑛 )? 

## **A** : it depends … 

   - in case a, ℎ= 2 years, while 𝑛= 1 is 1 year for each bond 

   - `o` in case b, if interest rate **falls** / **rise** in 𝑡+ 1 , you **lose** / **gain** : at the moment of reinvesting, you may fail to get the same interest rate as before! 

- Copyright ©2015 Pearson Education, Ltd. All rights reserved. Bottom line: even very short maturities have risks ... 

## **Duration** 

## Can we **quantify** the **IRR** of a bond? 

   - the further in the future the _payments_ of a bond lie, the more the bond is exposed IRR 

   - idea: we could use a measure of time of each payment (c.d. “effective maturity”) of a bond to quantify IRR 

   - in practice: to construct this measure of “effective maturity”, for each period: 

      - 1[st] : calculate the % of the total PV of a bond is contributed by cash flows in each year payments are due (4 ex.: 1, 2, etc…) 

      - 2[nd] : use these weights to calculate a “weighted” maturity 

- Duration is the **weighted average of the maturities of the cash payments** 

`o` it’s like an effective maturity `o` useful because it allows to _quantify_ the IRR because … 

```
o
```

Copyright ©2015 Pearson Education, Ltd. All rights reserved. 

## **Duration** 

## Before we get to the formula, let’s see the intuition 

- We want a measure of IRR 

- Use the idea that the longer the maturity the higher IRR 

Two bonds with same original maturity do **not** same IRR necessarily have 

1: a zero-coupon bond (ZCB) makes all payments at the end 2: a coupon bond (CB) spreads them out in each period 

**Q** : is the IRR (measured by the _effective maturity_ ) higher or lower for a ZCB with the same maturity of the coupon bond? 

## **Duration** 

## Before we get to the formula, let’s see the intuition 

- We want a measure of IRR 

- Use the idea that the longer the maturity the higher IRR 

Two bonds with same original maturity do **not** same IRR necessarily have 

- 1: a zero-coupon bond (ZCB) makes all payments at the end 2: a coupon bond (CB) spreads them out in each period. 

**Q** : is the IRR (measured by the _effective maturity_ ) higher or lower for a ZCB with the same maturity of the coupon bond? 

**A** : **higher** for ZCB, because ZCB makes all payments at the end, while CB makes payments earlier than ZCB 

## **Formula for Duration** 

**==> picture [610 x 139] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝐶𝑃<br>𝑛 𝑛 𝑡 𝑛<br>𝑃𝑉𝑡 1 + 𝑖 [𝑡]<br>𝑡 𝑡∙ 𝑡∙𝛼<br>𝑡<br>𝐷𝑈𝑅= ෍ 𝑃𝑉𝑇𝑂𝑇 = ෍ 𝑛 𝐶𝑃𝑡 = ෍<br>𝑡=1 𝑡=1 σ𝑡=1 1 + 𝑖 [𝑡] 𝑡=1<br>t  = maturity of cash flow payment ( 𝐶𝑃𝑡) weight<br>**----- End of picture text -----**<br>


where: 𝐶𝑃𝑡 = 𝐶 for 𝑡< 𝑛 ; 𝐶𝑃𝑡 = 𝐶+ 𝐹𝑉 for 𝑡= 𝑛 

- Formula intuition: the _effective_ of bonds is a _maturity_ coupon 

- weighted average of effective maturities on discount bonds 

`o` each coupon payment is like a discount bond 

`o` 𝛼 the weights ( 𝑡 ) are equal to the proportion of the total value (in terms 𝐶𝑃 𝑡 1+𝑖[𝑡] 𝛼 = of PV) represented by each discount bond: 𝑡 𝐶𝑃 

**==> picture [70 x 59] intentionally omitted <==**

`o` 𝛼 = 1 Copyright ©2015 Pearson Education, Ltd. All rights reserved. **Duration of a ZCB equal to its maturity** (in fact: 𝑡 ) 

## **Explaining formula for Duration** 

**==> picture [542 x 95] intentionally omitted <==**

**==> picture [349 x 23] intentionally omitted <==**

**==> picture [368 x 44] intentionally omitted <==**

𝐷𝑈𝑅 = 𝛼 … 𝐷𝑈𝑅 = 𝛼 1 1 × 1 4 4 × 4 

𝐷𝑈𝑅 = 𝐷𝑈𝑅 𝑡 1 + 𝐷𝑈𝑅2 + 𝐷𝑈𝑅3 + 𝐷𝑈𝑅4 

- if the weights are the proportion of the total value (in terms of PV) represented by each discount bond … 

- … why is the d **uration of a ZCB equal to its maturity** ? 

`o` Because having only one time in which payment takes place (say 𝑡 ), then: 𝛼 = 1 𝑡 by definition Copyright ©2015 Pearson Education, Ltd. All rights reserved. 2-55 

## **Calculating Duration -** _**i**_ **=12%, 5 Year, Coupon Bond** 

**==> picture [671 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
i    = 0.12<br>time 1 2 3 4 5<br>CF 100 200 0 450 1000<br>PVt 89.3 159.4 0.0 286.0 567.4 PVTOT= 1102.1<br>a t 8.1% 14.5% 0.0% 25.9% 51.5%<br>DURt 0.1 0.3 0.0 1.0 2.6 DUR= 3.98<br>**----- End of picture text -----**<br>


## Decompose 𝑃𝑉𝑇𝑂𝑇: 

**==> picture [474 x 82] intentionally omitted <==**

**==> picture [655 x 117] intentionally omitted <==**

 At home try to replicate it and then change values ( _i, CF’s, n_ ) … …    see what happens to DUR (properties: nextCopyright ©2015 Pearson Education, Ltd. All rights reserved. slide!) 

2-56 

## **Calculating Duration -** _**i**_ **=10%, 10 Year, 10% Coupon Bond** 

**==> picture [534 x 358] intentionally omitted <==**

**Duration for a coupon bond always less than actual maturity (see next page)** 

2-57 

## **Properties of Duration** 

**==> picture [343 x 72] intentionally omitted <==**

## **Properties: DUR**  **if:** 

- 

- **1. Maturity** (obvious) 

**2.** 𝒊  𝒄𝒓(= 𝑪/𝑭𝑽) (ZCBs have max duration=actual maturity because 

they pay all at the end) 

**3.** 𝒊  sensitivity to changes in rates increases as rates fall (because duration is a linear approximation: as int. falls, discount the future less, far distant weights from now are higher) 

Recall also: 

a. for **ZCB: Duration=Maturity** b. for **CB: Duration<Maturity** Copyright ©2015 Pearson Education, Ltd. All rights reserved. 

## **Duration and Interest-Rate Risk** 

- Recall that IRR is given by the price change of a coupon bond if _i_ changes 

- With the duration we can approximate (for **small changes** in interest rate) the % price change with: 

∆𝑖 

%∆𝑃≈−𝐷𝑈𝑅× 

1 + 𝑖 0 

`o` note: ∆𝑖= 𝑖 1 −𝑖0 

- the formula comes from a 1[st] order Taylor approximation 

Ex: if 𝑖↑ from 10% to 11% for coupon bond with a duration of 6.76 years: 

Δi =0.11-0.1=0.01 

0.01 

**==> picture [659 x 37] intentionally omitted <==**

## **Duration and** 

## **Interest-Rate Risk (cont.)** 

- The **greater** the duration of a security, the **greater** the percentage change in the market value of the security ( Δ𝑃 ) for a given change in interest rates ( 𝛥𝑖 ) 

- Therefore, the greater the duration of a security, the greater its IRR 

- The duration is not quite the same as the IRR, but it measures its **intensity** ! 

## **Exercise: Duration** 

A 5% coupon bond has a YTM of 6% and a price of $965 . The interest rate then falls to 5.5%. The duration is 4 years. **Q** : What is the new price? 

## **Exercise: Duration** 

A 5% coupon bond has a YTM of 6% and a price of $965 . The interest rate then falls to 5.5%. The duration is 4 years. **Q** : What is the new price? **A** : 𝑃= $983.2 Indeed: 

- – Δi =0.055 0.06= 0.005 

1+i = 1+ 0.06 = 1.06 

− Δ𝑖 0.005 %Δ𝑃≈−𝐷𝑈𝑅× 1 + 𝑖[= −4 ×] 1.06 

= +0.019 

- 𝑃1 = 𝑃0 1 + 0.019 = $965 × 1.019 = $983.2 

## **Duration of a Portfolio** 

Consider not a single security, but a portfolio of securities 

## **Duration is additive (∑)** 

- The duration of a _portfolio of securities_ is the **weighted-** of the durations of the individual securities … 

- **average** 

- … with the **weights** equaling the proportion of the portfolio value invested in each security 

- Ex: if have _n_ bonds in the portfolio: 

   - _DURportfolio_ = _DUR1_ × _w1_ + _DUR2_ × _w_ 2 +...+ _DURn_ × _w_ 𝑛 

   - _where w k is the weight of bond k over total value of bonds in the_ 

   - _portfolio_ 

## **Exercise: Duration of a Portfolio** 

 Assume that you have a portfolio of 2 bonds `o` One has a duration of 3 years, and the other has a duration of 7 years `o` The market values of the bonds are $600 and $900, respectively `o` Both bonds have the face value of $1,000 **Q** : What is the **duration of your portfolio** ? 

## **Exercise: Duration of a Portfolio** 

- Assume that you have a portfolio of 2 bonds 

`o` One has a duration of 3 years, and the other has a duration of 7 years `o` The market values of the bonds are $600 and $900, respectively `o` Both bonds have the face value of $1,000 

## **Q** : What is the **duration of your portfolio** ? 

**==> picture [418 x 38] intentionally omitted <==**

**==> picture [296 x 38] intentionally omitted <==**

𝐷𝑈𝑅𝑝𝑜𝑟𝑡𝑓𝑜𝑙𝑖𝑜= 3 × 0.4 + 7 × 0.6 = 1.2 + 4.2 = 5.4 (years) 

**N.B.1** The weights reflect the values (market prices) of the securities in the portfolio, not their face values 

## **Chapter 3 Summary (1/2)** 

1. We examined how to price various debt instruments using the Present Value formula 

2. We defined the YTM as the interest rate that makes the price of debt (P) equal to its PV 

3. We defined the concept of the current yield = C/P 

4. We discussed the relation between YTM, P and C `o` Especially that YTM and P are negatively related! 

5. We distinguished between real and nominal interest rate 

## **Chapter 3 Summary (2/2)** 

6. We distinguished between _i_ and rate of return and found out that only if we HTM the two coincide 

7. Hence, we defined IRR, which makes investment in L-T bonds risky 

8. And we’ve seen how to measure IRR using Duration 

Lots of definitions, but these are all **fundamental concepts** for the rest of the semester. Make sure you understand them! 

