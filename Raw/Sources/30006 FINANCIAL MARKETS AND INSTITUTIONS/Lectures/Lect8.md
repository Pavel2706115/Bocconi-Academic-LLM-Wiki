# Class 30006 – Financial Markets and Institutions Università Commerciale Luigi Bocconi Fall 2025 Prof. Francesco Bripi **Valuation of a stock (Chapter 13)** 

**==> picture [311 x 193] intentionally omitted <==**

**----- Start of picture text -----**<br>
Copyright ©2015 Pearson Education, Ltd. All rights reserved.<br>**----- End of picture text -----**<br>


**==> picture [300 x 193] intentionally omitted <==**

**----- Start of picture text -----**<br>
13-1<br>**----- End of picture text -----**<br>


## **Price of a Stock** 

- We all know **Apple** to be a successful company 

✓ any idea how much a stock of Apple would cost? `o` check it out 

- ✓ and check out the growth rate: on 1[st] Aug 1997 it was selling for 65.8 cents 

- ✓ it really only took off when first i-Phone was announced in 2007 

- ✓ they are now the company with the largest market capitalization in the world: $3.47 trillion! 

   - it was $2.4 trillion 2 ys ago 

## **Price of a Stock** 

- ✓ Ever heard of **Berkshire Hathaway Inc.** ? 

`o` it’s Warren Buffett’s investment company 

   - Warren Buffett is one of the richest man on earth, he’s been running the company for 50+ years 

- ✓ Buying a share in Berkshire Hathaway seems like a good investment. 

`o` want to buy? Check out the price 

- ✓ It’s one of the few financial companies in the US among the top 20 by market cap 

## **Computing the Price of a Stock** 

- ✓ The principle of valuing common stock is no different from valuing debt securities: 

   1. Determine the cash flows 

   2. Discount them to the present 

   3. Price them at their PV 

- ✓ But … the pricing of a stock is much **harder** in practice than it is for bonds. Why? 

## **Computing the Price of a Stock** 

**Q** : what are the two items that compose a stock cash flow? ( _i.e._ how do you make money by owning a stock?) Are they both certain? 

## **Computing the Price of a Stock** 

**Q** : what are the two items that compose a stock cash flow? ( _i.e._ how do you make money by owning a stock?) Are they both certain? 

## **A:** 

**1. Dividends** (share of company’s profits distributed to stockholders) 

## **2. Future sales price** 

No, neither one is certain … 

- … and different stockholders may have different information about the stock and thus they have different valuations 

## **The One-Period Valuation Model** 

✓ Take the simplest model, just take the expected dividend and the expected price over the next year. 

𝐷𝑖𝑣 𝑃 1 1 = 𝑃 + 0 1 + 𝑘 1 + 𝑘 𝑒 𝑒 

## where: 

`o` 𝑃 0 is the price today `o` 𝑃 1 is the (forecasted) price next year `o` 𝐷𝑖𝑣 1 is the (expected) dividend next year `o` 𝑘 𝑒 : rate for discounting stocks 

▪ works like YTM, but _usually it’s higher …_ ▪ because stocks are riskier, so you discount future cash flows more! 

## **The One-Period Valuation Model** 

- ✓ Suppose you see a stock trading at $50 paying $0.16 in dividend per year 

✓ You read an analyst forecast that price is expected to rise to $60 next year 

✓ You decide you want to have 12% to be compensated for risk 

**Q** : Find the price using your compensation for risk 𝑃0∗ . Should you buy? 

## **The One-Period Valuation Model** 

$0.16 $60 ∗ = 𝑃 0 1 + 0.12[+] 1 + 0.12[= $53.71] 

- ✓ 𝑃 ≤𝑃∗ if market price is lower than (or equal to) your value ( 0 0 or also: $50 ≤$53.71 ): **buy** 

- ✓ 𝑃 > 𝑃∗ or also: if market price is higher than your value ( 0 0 $50 > $53.71 ): do **not** buy 

- ✓ 𝑘 or 𝑃∗ … or Obviously, other investors may have different 𝑒 0 the model is wrong 

## **The Generalized Dividend Valuation Model** 

✓ 𝑛 Using the same logic, extend to periods: 

**==> picture [459 x 48] intentionally omitted <==**

✓ but as _n_ grows, last item in the summation gets smaller (higher discounting). So, end up with: 

**==> picture [155 x 64] intentionally omitted <==**

✓ Note: 

`o` ∞ is the end of summation … firms are supposed to be infinitely lived 𝑃 𝑛 `o` no final (1+𝑘𝑒)[𝑛][ in the second expression, bcs for ][𝑛][ large enough it is a ] 𝑃 very low number, so that you don’t need to forecast 𝑛 `o` just PV of _all_ future dividends matter ( _fundamentals)_ 

✓ Copyright ©2015 Pearson Education, Ltd. All rights reserved.But it is “difficult” to forecast an infinite stream of payments …13-10 

## **The Gordon Growth Model** 

✓ Same as the previous model, but just _assume_ that dividend : grow at a constant rate 𝑔 𝐷𝑖𝑣 𝑡+1 = (1 + 𝑔)𝐷𝑖𝑣𝑡 

✓ Then price of stock is: 𝐷𝑖𝑣 1 + 𝐷𝑖𝑣 1 + 𝐷𝑖𝑣 1 + 0 𝑔 0 𝑔[2] 0 𝑔[𝑛] = 𝑃 + + ⋯+ 0 1 + 𝑘 1 + 𝑘 1 + 𝑘 𝑒 𝑒[2] 𝑒[𝑛] 

**==> picture [592 x 138] intentionally omitted <==**

**----- Start of picture text -----**<br>
✓ With some  algebra  we can show that:<br>∞<br>𝐷𝑖𝑣 𝐷𝑖𝑣 1 +  𝐷𝑖𝑣<br>𝑡 0 𝑔 1<br>=<br>𝑃 𝑜𝑟 𝑃<br>0 0<br>= ෍ 𝑘 𝑘<br>(1 + 𝑘𝑒) [𝑡] [=] 𝑒 −𝑔 𝑒 −𝑔<br>𝑡=1<br>✓ How convenient!<br>**----- End of picture text -----**<br>


`o` we don’t need to forecast an infinite stream of payments 

`o` **an estimate of** and of 𝒌 just get 𝒈 𝒆 (“ _required rate of return”_ ) Copyright ©2015 Pearson Education, Ltd. All rights reserved. 

## **The Gordon Growth Model: Example** 

Let’s get back to previous example, with 𝑃0 = $53.71 

- ✓ What is the implied dividend growth ( 𝑔 ) with a required rate of 𝑘 

- return ( 𝑒 ) of 10%? 

**==> picture [468 x 54] intentionally omitted <==**

✓ 𝐷𝑖𝑣 = But conveniently by definition 1 1 + 𝑔𝐷𝑖𝑣0 , so: 

𝐷𝑖𝑣 $0.16 0 1 + 𝑔 (1 + 𝑔) = $53.71 = (0.1 −𝑔) (0.1 −𝑔) ✓ _Solve for :_ 𝑔 $53.71 ∙ 0.1 −𝑔= $0.16 1 + 𝑔 ⇒0.1 ∙$5.371 −$53.71𝑔= $0.16 + 0.6𝑔 ⇒$5.371 −$0.16 = 𝑔 $53.71 + $0.16 𝒈= 𝟗. 𝟔𝟕% 

## **The Gordon Growth Model: Assumptions** 

- 1) Do dividends grow at a constant rate forever? 

`o` No, but if they grow constantly for some time the model is reasonable … `o` … after “some” time? Again, cash flows 20 years from now are _very difficult to predict_ , but they are also very small when discounted 

- 𝒌 

- 2) Note another assumption: 𝒆 > 𝒈 

𝐷1 = `o` 𝑃 otherwise, we can’t simplify to 0 𝑘𝑒−𝑔 **[  …]** 

- but this is also reasonable: if 𝑘 𝑒< 𝑔 Gordon formula no longer valid: 

- why? 

- 𝑘 ? 

- at home: what happens if 𝑒 = 𝑔 

## **The Gordon Growth Model: Interpretation** 

- ✓ How about companies (the majority) **that do not pay dividends** to shareholders? 

`o` Suppose Google Dividend=0, is its price=0? `o` No! Investors buy Google because expect the company’s profits  

- ✓ Even if earnings are not distributed, they are re-invested within the firm … 

   - … at some point in the future, shareholders will get paid … 

`o` … at an increased value of the firm ▪ (suppose for sake of simplicity, that re-investment of earnings is at the same rate of return 𝑘𝑒 ) 

- ✓ So, the “unpaid” dividends still “belong” to the stockholder 

- ✓ Dividends can be loosely interpreted as any cash flow stockholders are entitled to 

## **EXERCISE: Volkswagen Dieselgate** 

✓ It’s Jan 2015. Suppose Volkswagen announced dividends for €4.8 per share this year, growing at 10% forever. 

- ✓ However in September 2015, following the ‘‘dieselgate’’ scandal, VW announces: 

`o` it will only pay dividends of €0.11 in 2016 `o` from 2017 it will pay €4 and growing at 8% thereafter 

**Q** : what is VW expected price today (2015) before and after the dieselgate happens? What is %P? Assume 𝑘 = 12% 𝑒 (round to nearest integer) 

## **EXERCISE: Volkswagen Dieselgate** 

✓ _a_ (before the dieselgate): 

𝐷𝑖𝑣 €4.8 × 1.1 2016,𝑎 = = 𝑃 2015,𝑎 𝑘 12% −10%[= €264] 𝑒 −𝑔𝑎 = 𝑃 _b_ (after the dieselgate): 2016,𝑏 𝐷𝑖𝑣 𝑃 𝐷𝑖𝑣 𝐷𝑖𝑣 1 2016, 𝑏 2016, 𝑏 2016,𝑏 2017,𝑏 𝑃 = + ⟹𝑃 = + × 2015,𝑏 2015,𝑏 1 + 𝑘 1 + 𝑘 1 + 𝑘 𝑘 1 + 𝑘 𝑒 𝑒 𝑒 𝑒 −𝑔𝑏 𝑒 €0.11 €4 1 = 𝑃 2015,𝑏 1.12[+] 0.12 −0.08[×] 1.12[⟹𝑃][2015,𝑏][= €89.4] 𝑃 −𝑃 €89 ~~.~~ 4 −€264 2015,𝑏 2015,𝑎 = = %Δ𝑃 = −195 ~~.~~ 4% 2015 𝑃 €89 2015,𝑏 

✓ _b_ (after the dieselgate): 

`o` Note that numerator of 𝑃2016,𝑏 is 𝐷𝑖𝑣2017,𝑏 , not 𝐷𝑖𝑣2016,𝑏 1 + 𝑔𝑏 , because Copyright ©2015 Pearson Education, Ltd. All rights reserved. 𝐷𝑖𝑣 ≠𝐷𝑖𝑣 𝐷𝑖𝑣 13-16 in this example 2016,𝑏 1 + 𝑔𝑏 2017,𝑏 , cannot apply 2016,𝑏 1 + 𝑔𝑏 

## **Price Earnings Valuation** 

✓ The **price earnings ratio** (PE ot P/E) `o` PE is a measure of how much the market is willing to pay for $1.00 of 𝑃 company’s earnings: 𝑃𝐸= 𝐸 

- widely watched measure 

- easy to calculate and avoids dividends (often they are not distributed) by looking at earnings 

✓ Trivially then, by definition: **This is the PE** 𝑃 𝑃𝑟𝑖𝑐𝑒= 𝐸[× 𝐸𝑎𝑟𝑛𝑖𝑛𝑔𝑠] 

- where E are the earnings per share (EPS) and, obviously, P is the share price 

✓ If PE is 20 it means that investors are willing to pay $20 today Copyright ©2015 Pearson Education, Ltd. All rights reserved. 13-17 for each $ of company’s earnings per share 

## **Price Earnings Valuation** 

## 𝑃𝑟𝑖𝑐𝑒= 𝑃𝐸× 𝐸𝑎𝑟𝑛𝑖𝑛𝑔𝑠 

- ✓ _E_ is **expected earnings per share** 

   - since future earning are unknown, in practice it is common to use _actual_ earnings per share from the last 12-months 

- ✓ Is the PE high or low? It depends on relatively to what! 

- ✓ As a reference the PE can also be taken from **industry average** . Why? 

   - because it is expected that a firm PE will _equal_ the industry average PE in the run long 

## **Price Earnings Valuation** 

- ✓ A PE of a firm higher than industry-average 𝑃𝐸 > 𝑃𝐸 𝑓 𝑗 

- has two interpretations ( 𝑓= 𝑓𝑖𝑟𝑚; 𝑗= 𝑖𝑛𝑑𝑢𝑠𝑡𝑟𝑦 ): 

`o` in a “high PE” company, _earnings_ are **expected to rise** in the future compared to low PE companies 

   - the company is **low risk** , hence the market pays a premium for its earnings 

- ✓ Growth/Glamour stocks are those with high PE 

- ✓ A “low PE” 𝑠𝑎𝑦: 𝑃𝐸 < 𝑃𝐸 means: 𝑓 𝑗 

`o` firm will have **lower** future _earnings_ that are **already** reflected in the stock price (note P/E is obtained by dividing by the _higher current_ earnings) 

`o` that the firm is **quite risky** and thus the stockholders require more compensation (in form of current earnings) to hold this stock 

## **Price Earnings Valuation** 

Example 

- ✓ Firm A’s stock currently earns $1.55 per share and costs at the moment $24.01. Its P/E is in line with industry 

- ✓ Firm B’s stock currently earns $1.96 per share. Assume that it belongs to the same industry as firm A 

- **Q.** : How much we would expect it is valued today? Assume that it has a PE in line with that of the industry 

## **Price Earnings Valuation** 

Example 

- ✓ Firm A’s stock currently earns $1.55 per share and costs at the moment $24.01. Its P/E is in line with industry 

- ✓ Firm B’s stock currently earns $1.96 per share. Assume that it belongs to the same industry as firm A 

- **Q.** : How much we would expect it is valued today? Assume that it has a PE in line with that of the industry **A** :  P/E (firm A)=$24.01/$1.55 = 15.49 

× P/E (firm B)= $1.96 15.49 = $30.36 

## **Errors in Valuation** 

✓ Wow! We can price stocks … let’s go make some money! 

- ✓ note that all the models require to compute **expected earnings/dividends/growth rates** 

- ✓ sometimes far ahead in the future 

- ✓ and _small errors_ in evaluating each can lead to _big mistakes_ (read: big losses!) 

- ✓ For example, in the Gordon model we need two items: 𝒈 and 𝑘 and 𝑘 𝑒 , errors could depend on both 𝒈 𝑒 

## **The Gordon Growth Model: Example** 

## Let’s see how assumptions on 𝑔 and on 𝑘𝑒 may create large evaluation errors Example: 

`o` dividend is $2 

`o` fix 𝑘 =0.2 and let 𝑒 𝑔 **vary** 

𝐷𝑖𝑣 1 = 𝑃 0 − 𝑘 𝑒 𝑔 

**==> picture [420 x 254] intentionally omitted <==**

`o` different (projected) growth rates result in very different valuations of the stock! 

## **The Gordon Growth Model: Example** 

## Same example: 

`o` dividend is $2 

`o` fix =0.11 and let 𝑘 𝑔 𝑒 **vary** 

𝐷𝑖𝑣 1 = 𝑃 0 𝑘 𝑒 −𝑔 

**==> picture [432 x 260] intentionally omitted <==**

`o` different (projected) required rates of return imply very different valuations of the stock! 

## **Errors in Valuation:** _**g**_ 

## **Table 13.1** Stock Prices for a Security with _D_ 0 = $2.00, _ke_ = 15%, and Constant Growth Rates as Listed 

**==> picture [25 x 190] intentionally omitted <==**

**==> picture [25 x 178] intentionally omitted <==**

**ΔP (and also mistakes) getting bigger as** _**g**_ **grows** 

## **The 2007–2009 Financial Crisis and the Stock Market** 

✓ The Financial Crisis, which started in August 2007, was the start of one of the worst _bear_[(1)] markets in history 

**Q** : What may contribute to low prices in a recession according to Gordon model? 

- (1): bear markets if stock prices fall, bull markets if they rise 

## **The 2007–2009 Financial Crisis and the Stock Market** 

- ✓ The Financial Crisis, which started in August 2007, was the start of one of the worst _bear_[(1)] markets in history 

**Q** : What may contribute to low prices in a recession according to Gordon model? 

_1._ is revised **downward** _g_ as expectation of future growth for US companies are revised downward 

_2. ke_ is also **higher** due to higher uncertainty `o` discount the future more 

- ✓ both contributed to **a fall** in _price of stocks_ 

(1): bear markets if stock prices fall, bull markets if they rise 

## **How the Market sets Prices** 

- ✓ Suppose there are three investors interested in a stock 

1. You: _do not know much_ about the company, just read on WSJ that dividends are expected to be $2 and grow at 3%. 𝒌 **=15%** . 

Uncertainty requires 𝒆 

2. Jennifer: she knows the industry. Feels _confident_ the 𝒌 **=12%** . 

estimates are quite accurate. Lower 𝒆 

3. Bud: is _dating_ the CEO of the company. He knows what the company’s plans are. He only requires 𝒌𝒆 **=7%** . 

## **How the Market sets Prices** 

✓ Applying the Gordon model yields the following prices: 

**==> picture [507 x 156] intentionally omitted <==**

- ✓ The prices reflect the willingness-to-pay (maximum acceptable price) of each investor 

- ✓ In a market auction, Bud would get the stock. He would bid just above Jennifer’s price 

## **How the Market sets Prices** 

- ✓ : Two important lessons about competitive auction markets 

   1. the price is set by the buyer with the highest _w_ illingness _t_ o _p_ ay (but _not necessarily_ at P= _w_ . _t_ . _p_ .) 

   2. the price is set by the buyer who can take best advantage of the asset 

- ✓ Information matters!! This is why stock prices fluctuate widely on news reports 

- ✓ Price may also be due to overoptimism driven by market euphoria (after all, Bud is in love…): 

`o` if the expectations are wrong, we have a **bubble** (prices too high) that will burst and create damage 

## **How the Market sets Prices** 

✓ Given different evaluations (4 ex.: _g_ and _k_ in the Gordon model), stock analysts are _seldom_ certain that their stock price projections are accurate 

✓ So, should we be skeptical on investing in stock markets? `o` no, because short term fluctuations in **stock prices** are **normal** `o` in the long-term stock **prices will reflect true earnings of the firm** 

**==> picture [549 x 253] intentionally omitted <==**

## **Next class** 

We will discuss derivatives: Forwards and Futures 

