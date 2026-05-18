## **1. Descriptive Statistics** 

Frequency notation f_i = absolute frequency p_i = f_i/n = relative frequency F_i = cumulative frequency n = Σ f_i = sample size 

## **Central Tendency Measures** 

Mean: xI = (1/n) Σ x_i Grouped data: xI = Σ x*_k p_k Approximation using midpoints: xI ≈ Σ m_k p_k Median (odd n): Me = x_{(n+1)/2} Median (even n): Me = (x_{(n/2)} + x_{(n/2)+1}) / 2 Mode: value with highest frequency 

## **Dispersion Measures** 

Range: R = max(x_i) - min(x_i) Variance (sample): s² = (1/(n-1)) Σ (x_i - xI)² Standard deviation: s = √s² Coefficient of variation: CV = s / xI Interquartile range: IQR = Q3 - Q1 

## **Correlation** 

Covariance: s_xy = (1/(n-1)) Σ (x_i - xI)(y_i - I) Correlation coefficient: r = s_xy / (s_x s_y) 

## **2. Probability and Random Variables** 

Probability: P(A∪B)=P(A)+P(B)-P(A∩B) Conditional probability: P(A|B)=P(A∩B)/P(B) Independent events: P(A∩B)=P(A)P(B) Expected value: E[X]=Σ x_i P(X=x_i) − − Variance: Var(X)=E[(X E[X])²]=E[X²] (E[X])² 

## **3. Common Distributions** 

− − − Bernoulli(p): P(X=x)=p^x(1 p)^{1 x}, E[X]=p, Var(X)=p(1 p) Normal(µ,σ²): f(x)=1/(√(2πσ²)) e^{−(x−µ)²/(2σ²)}, E[X]=µ, Var(X)=σ² Standardization: Z=(X−µ)/σ 

## **4. Sampling Distributions** 

Sample mean: E[xI]=µ, Var(xI)=σ²/n, SE=σ/√n Sample proportion: E[pI]=p, Var(pI)=p(1−p)/n, SE=√(p(1−p)/n) 

## **5. Point Estimation** 

Unbiasedness: E[θI]=θ Bias: Bias(θI)=E[θI]−θ Asymptotic unbiasedness: lim(n→∞)Bias(θI)=0 Efficiency: smaller Var(θI) ⇒ more efficient 

## **6. Estimators and Standard Errors** 

Population mean: θI=xI, SE=σ/√n or s/√n Population proportion: θI=pI, SE=√(p(1−p)/n) or √(pI(1−pI)/n) Difference of means (independent): SE=√(s_x²/n_x + s_y²/n_y) Paired difference: SE=s_D/√n Difference of proportions: SE=√(pI(1−pI)/nI + pI(1−pI)/nI) 

## **7. Normal Distribution Functions in R** 

pnorm(q, mean, sd) → cumulative probability P(X ≤ q) 1 - pnorm(q, mean, sd) → P(X > q) qnorm(p, mean, sd) → quantile (percentile) 

## **8. UBStats Functions** 

distr.table.x() – frequency tables distr.plot.x() – histograms/bar plots distr.summary.x(stats='central') – mode, median, mean distr.summary.x(stats='dispersion') – range, IQR, sd, var distr.table.xy() – cross-tabulations distr.plot.xy() – bar plots for two variables 

