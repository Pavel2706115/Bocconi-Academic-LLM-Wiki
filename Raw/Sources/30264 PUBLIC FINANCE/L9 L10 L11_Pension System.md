---
course: Public Finance
course_code: "30264"
tags:
  - "source"
  - course_30264
Links:
Title: "Social Security (Pension System) Gruber - Chapter 13"
Reference: "Course Material"
Created: 2026-05-18
Processed: true
---

### Topic 1: Introduction and the European Context
- **Slide 1: Title Slide**
	- **Summary:** The title slide introduces the lecture on “Social Security (Pension System)” from the Public Finance course
- **Slide 2: Social Security spending in Europe**
	- **Graph Explanation:** A stacked bar chart showing Social Security spending as a percentage of GDP across various European countries. The bars are divided by function:
		- Old-age (blue)
		- Disability (orange)
		- Survivors (gray)
		- Unemployment (yellow)
	- **Key Points:** Italy spends a significant portion of its GDP on social security, predominantly driven by old-age and survivors' pensions, placing it among the highest spenders alongside France and Greece
- **Slide 3: Pension spending trends in Europe**
	- **Graph Explanation:** A line graph tracking pension spending as a percentage of GDP from 1995 to 2022 across multiple European countries
	- **Key Points:** Most countries show an upward trajectory in spending over time. Italy (red line) gas consistently remained one of the highest spenders throughout the observed decades
- **Slide 4: Lecture Outline**
	- **Summary:** Outlines the lecture's core themes:
		1. Why the government provides social security?
		2. The types of systems (PAYGO vs. fully funded)
		3. Risks like moral hazard
		4. Financial equilibrium
		5. Specific focus on the Italian reform case
### Topic 2: The Rationale and Types of Pension Systems
- **Slide 5: Why should the government provide social security?**
	- **Summary:** Explains the rationale for state intervention. The primary “adverse event” is getting too old to earn a sufficient income
	- **Key Points:** While private pension plans (where current savings are invested in bonds/stocks to fund future benefits) exist, they are prone to failure. Inflation and poor financial market performance can severely lower the “replacement ratio” (the ratio of benefits to pre-retirement earnings). Additionally, individuals often underestimate their future needs, making private markets inefficient for this social risk
- **Slide 6 & 7: Types of pension systems & Public Systems**
	- **Summary:** Defines two primary structures of pension systems
	- **Key Points:** 
		- **Fully Funded:** <mark style="background:rgba(240, 200, 0, 0.2)">Workers' contributions are actively invested in capital markets to fund their own future pensions</mark>
		- **Pays-As-You-Go (PAYGO):** <mark style="background:rgba(240, 200, 0, 0.2)">An unfunded scheme based on an intergenerational pact. The taxes collected from active workers today go directly to pay for today's retirees, with the expectation/intergenerational promise that the next generation will do the same for them</mark>
- **Slide 8 & 9: Diagrams of Funding Systems**
	- **Summary:** Visual diagrams illustrating the flow of money. In PAYGO, funds move diagonally from workers at time $t$ to retirees at time $t$. In Fully Funded systems, funds stay with the cohort, moving from workers into a “Fund,” which pays out to that same cohort when they become retirees at time $t+1$.
### Topic 3: Comparing Systems: Financing and Returns
- **Slides 10, 11, & 13: Comparison Overview**
	- **Summary:** Transition slides establishing the three dimensions used to compare systems:
		- Financing method
		- Rate of return
		- Method for calculating benefits
- **Slide 12: Financing Method**
	- **Summary:** Details the core mathematical difference in financing
	- **Key Points:** <mark style="background:rgba(240, 200, 0, 0.2)">In PAYGO</mark>, $C_t$ =>$P_t$ <mark style="background:rgba(240, 200, 0, 0.2)">(contributions at time t fund pensions at time t)</mark>. <mark style="background:rgba(240, 200, 0, 0.2)">In a Fully Funded system</mark>, $P_t = C_{t-1} \times (1+i)$, <mark style="background:rgba(240, 200, 0, 0.2)">meaning pensions equal past contributions multiplied by the capital market's interest rate</mark> ($i$)
- **Slide 14-16: Pension systems' returns**
	- **Summary:** Explains how "implicit returns" are calculated in PAYGO versus actual returns in Fully Funded systems
	- **Key Points:** 
		- The implicit return of PAYGO is driven by population growth ($n$) and productivity/wage growth ($m$). The rate is approximately $n+m$
		- The return for a Fully Funded system is simply the market interest rate ($i$)
		- PAYGO offers a better return than a Fully Funded system only if population and wage growth combined exceed the interest rate ($(n+m)>i$)
- **Slides 17 & 18: PAYGO system return rate (Example & Conclusion)**
	- **Summary:** A numerical table and its implications, assuming 5% population/wage growth and a 10% tax
	- **Key Points:** PAYGO allows a state to pay seniors immediately. However, it creates a “First Generation Effect” (the very first retirees get an infinite return because they never paid in) and a potential “Last Generation Effect” (if the system collapses, the final workers get a -100% return)
### Topic 4: PAYGO Computation Methods
- **Slide 20-22: Earnings-based PAYGO system**
	- **Summary:** Explains how pensions are calculated based on past salaries
	- **Key Points:** 
		- <mark style="background:rgba(240, 200, 0, 0.2)">Earnings-based: a company promising to pay you 70% of your final salary for the rest of your life, regardless of how long you live</mark>
		- The formula is $P = \beta \times W_p \times L$ <mark style="background:rgba(240, 200, 0, 0.2)">(Pension equals a coefficient of return times pensionable earnings, times years worked). Pensionable earnings</mark> ($W_p$) <mark style="background:rgba(240, 200, 0, 0.2)">can be calculated generously (using just the last salary before retirement) or strictly (using a lifetime average)</mark>
- **Slide 23-25: Contribution-based PAYGO**
	- **Summary:** Explains a system that mimics a funded system but remains unfunded
	- **Key Points:** 
		- <mark style="background:rgba(240, 200, 0, 0.2)">Contribution-based: A piggy bank that lets you get back exactly what you put in, and if you are going to live a very long time, you have to stretch those same savings out into much smaller monthly portions</mark>
		- The pension is determined by the total contributions paid ($C$) divided by the expected years of life at retirement ($e(L)$). This introduces a “transformation coefficient” ($\frac{1}{e(L)}$) which automatically lowers the yearly pension payout as life expectancy increases, passing the burden of an aging population directly to the retirees
- **Slide 26: Fully funded pension system: computation method**
	- **Summary:** Under a fully funded approach, the accumulated capital ($C$) grows via the actual market interest rate ($i$) and is then paid out based on life expectancy
- **Slide 27: Summary Table**
	- **Summary:** A matrix comparing the three systems (PAYGO Earnings-based, PAYGO Contribution-based, and Fully-funded) across their financing sources, total pension bill drivers, and individual pension calculators
### Topic 5: Poverty, Justifications, and Moral Hazard
- **Slide 28: Justifications for State Intervention**
	- **Summary:** Re-evaluates why the state is involved: 
		- A**dverse selection in private markets** (individuals know their life expectancy better than insurers)
		- **Paternalism** (governments fear people won't save enough)
- **Slide 29 & 30: Living standards of the elderly (US & Italy)**
	- **Graph Explanation:** Two line charts (one for the US, and one for Italy) plotting Social Security spending against elderly poverty rate 
	- **Key Points:** Both countries show a striking, inverse correlation over time. As social security spending increased, the poverty rate among the elderly fell significantly, confirming the system's success in stabilizing consumption
- **Slide 31 & 32: The impact of the pension system on retirement age**
	- **Summary:** Introduces the problem of moral hazard in pension system
	- **Key Points:** Systems often apply an “implicit tax” on labor. If you work an extra year you pay another year of taxes AND forfeit a year of pension payouts. If the resulting bump in future pension levels is not actuarially fair, it heavily incentivizes workers to retire at the earliest possible dates
- **Slide 33 & 34: Moral Hazard Evidence (US & Italy)**
	- **Graph Explanation:** Line graphs mapping Social Security Spending against the Labor Force Participation (LFP) rate of elderly
	- **Key Points:** As spending on pension grew rapidly in the 1960s-1970s, labor force participation plummeted, proving that workers react to the incentives of the system
- **Slide 35: Strike in Retirement Hazard at EEA**
	- **Graph Explanation:** A line graph plotting the exit rate of male workers against age
	- **Key Points:** There are massive spikes in retirement exactly at age 62 (Early Entitlement Age) and 65 (Full Retirement Age), proving people time their retirement directly to system rules
- **Slide 36 & 37: Implicit Taxes and Implications**
	- **Graph Explanation:** A scatter plot showing an incredibly strong correlation ($R^2 = 0.82$) between a country's "Disincentive to work" and the percentage of “Nonworking Elderly”
	- **Key Points:** Countries like Italy and Belgium have high disincentive and high non-work rates, while Japan has low disincentive and high elderly work rates. Adjusting systems to fairly reward late retirement can mitigate this costly moral hazard
### Topic 6: Social Security Reforms and Equilibrium
- **Slide 38 & 39: Financial Imbalance and Demographics**
	- **Summary:** PAYGO systems face a major crisis
	- **Key Points / Graph:** The imbalance is driven by rising life expectancy, falling births, and lower wage growth. The graph shows the US ratio of older adults to working age people will more than triple (from 13 per 100 in 1950 to 42 per 100 in 2060)
- **Slide 40 & 41: Financial equilibrium in a PAYGO system**
	- **Summary:** Outlines the mathematical balance required to sustain the system: $P \cdot N_r = \alpha \cdot N_w \cdot w$ (Total Pensions = Total Contributions)
	- **Key Points:** Because the number of retirees ($N_r$) is increasing, policymakers are forced to reform by either raising taxes ($\alpha$), lowering average pension ($P$), or raising the retirement age (which shifts people from the $N_r$ pool to the $N_w$ pool)
- **Slide 42 & 43: Incremental vs Fundamental Reforms**
	- **Summary:** Discusses solutions
	- **Key Points:** Incremental reforms involve tweaking the math (raising taxes, lowering benefits, raising the age). Fundamental reforms involve privatization. While privatization puts capital in individuals' hands and respects consumer sovereignty, it triggers a massive transition problem: how do we pay for the current generation of retirees if current workers are putting their money into private accounts?
### Topic 7: The Italian Pension System Care
- **Slides 44, 45, & 46: Demographics in Italy**
	- **Graph Explanation:**
		- Slide 45 shows Italy's “Elderly dependence index” steeply climbing from 10% in 1940 to over 60% by 2060
		- Slide 46 shows a population pyramid bar chart comparing 2000 vs 2050, visibly demonstrating the severe aging of the population structure
	- **Key Points:** Italy's system has been under severe pressure since the 1990s due to this aging trajectory
- **Slide 47: Timeline of Italian Reforms**
	- **Summary:** Marks the major reforms:
		- 1992 -> AMATO
		- 1995 -> DINI
		- 2011 -> FORNERO
- **Slide 48: The Amato Reform (1992)**
	- **Summary:** An incremental reform
	- **Key Points:** Kept the earnings-related method but switched the calculations base from the last 5 years of salary to the *entire* working life average, significantly lowering payouts. It raised retirement ages and indexed pensions only to inflation, ceasing indexation to wage growth
- **Slide 49: The Dini Reform (1995)**
	- **Summary:** A major structural reform
	- **Key Points:** Shifted Italy from an earnings-based PAYGO to a *contribution-based* PAYGO system. It introduced conversion coefficients tied to life expectancy, meaning longer-living populations, would automatically receive lower yearly pensions, discouraging early retirement. However, it applied only to new workers (1996 and forward)(pro-rata for others), delaying its fiscal impact
- **Slide 50: In between Dini and Fornero**
	- **Summary:** Outlines stopgap measures by Prodi (1998, 2007) and Maroni (2004) attempting to tweak seniority rules and quota systems to restrict early retirement
- **Slide 51: The Fornero Reform (2011)**
	- **Summary:** A drastic tightening of the system due to the financial crisis
	- **Key Points:** Forced the contribution-based calculation on *everyone* starting in 2012 (pro-rata). It raised the statutory retirement age rapidly toward 67 by 2020 and linked future age requirements automatically to life expectancy. It heavily penalized early retirement
- **Slide 52 & 53: Flexibility and the Future**
	- **Summary / Graph:** Because Fornero was so strict, subsequent governments introduced flexibility loopholes (like Quota 103 or Opzione Donna) for those willing to accept penalties. Slide 53's graph models Italy's public pension spending, showing it spiking near 17% in 2040 before the demographic wave passes, and it declines to 13.7% by 2070
## Related Notes
- [[Public Finance Public Policy 6th Edition (Jonathan Gruber) (z-library.sk, 1lib.sk, z-lib.sk)]]
- [[L18 L19_Taxes on savings]]
- [[Frederic S. Mishkin_ Stanley Eakins - Financial Markets and Institutions-Pearson (2018)]]