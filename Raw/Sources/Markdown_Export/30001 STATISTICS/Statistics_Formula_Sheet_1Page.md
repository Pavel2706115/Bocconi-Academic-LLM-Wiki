## **STATISTICS FORMULA SHEET – Bocconi University (Course 30001)** 

------------------------------------------------------------ 

## **1. DESCRIPTIVE STATISTICS** 

Mean xI=Σx_i/n; Weighted: Σx_k p_k; Median Me=(x_(n/2)+x_(n/2+1))/2; Mode=most frequent. Range=Max−Min; IQR=Q3−Q1; Variance s²=Σ(x_i−xI)²/(n−1); SD s=√s²; CV=s/xI. Covariance s_xy=Σ(x_i−xI)(y_i−I)/(n−1); Correlation r=s_xy/(s_x s_y). 

## **2. PROBABILITY** 

P(A∪B)=P(A)+P(B)−P(A∩B); P(A|B)=P(A∩B)/P(B); Indep.: P(A∩B)=P(A)P(B). E[X]=Σx_iP(X=x_i); Var(X)=E[X²]−(E[X])²; SD(X)=√Var(X). 

## **3. RANDOM VARIABLES** 

− − − Bernoulli(p): P(X=x)=p^x(1 p)^{1 x}, E[X]=p, Var(X)=p(1 p). Normal(µ,σ²): f(x)=1/(√(2πσ²)) e^{−(x−µ)²/(2σ²)}, Z=(X−µ)/σ, E[X]=µ, Var(X)=σ². Linear transform: Y=a+bX → E[Y]=a+bE[X], Var(Y)=b²Var(X). 

## **4. SAMPLING DISTRIBUTIONS** 

E[xI]=µ, Var(xI)=σ²/n, SE=σ/√n; E[pI]=p, Var(pI)=p(1−p)/n, SE=√(p(1−p)/n). 

## **5. POINT ESTIMATION** 

Unbiased: E[θI]=θ; Bias=E[θI]−θ; Efficiency→smaller Var(θI). Mean estimator xI → SE=σ/√n or s/√n. Proportion estimator pI=x/n → SE=√(p(1−p)/n) or √(pI(1−pI)/n). Difference of means (indep): SE=√(s_x²/n_x + s_y²/n_y); pooled: s_p²=[(n_x−1)s_x²+(n_y−1)s_y²]/(n_x+n_y−2); SE=s_p√(1/n_x+1/n_y). Paired means: D_i=X_i−Y_i, SE=s_D/√n. Difference of proportions: SE=√(pI(1−pI)/nI + pI(1−pI)/nI). 

## **6. NORMAL DISTRIBUTION FUNCTIONS (R)** 

pnorm(q,mean,sd)=P(X≤q); 1−pnorm(q)=P(X>q); qnorm(p,mean,sd)=percentile. 

## **7. UBSTATS FUNCTIONS** 

distr.table.x() freq tables; distr.plot.x() graphs; distr.summary.x(stats="central"/"dispersion") → mode, median, mean, range, IQR, sd, var. distr.table.xy(), distr.plot.xy() → two-variable tables/plots. 

------------------------------------------------------------ 

All symbols: µ(pop. mean), σ²(pop. var), s²(sample var), p(pop. proportion), pI(sample prop.), SE(standard error). 

