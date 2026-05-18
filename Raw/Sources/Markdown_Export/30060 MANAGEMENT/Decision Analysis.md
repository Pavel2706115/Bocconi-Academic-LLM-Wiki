# **DECISION ANALYSIS** 
[[DECISION ANALYSIS]] 

## AGENDA 

1. WHY WE NEED A SCIENTIFIC APPROACH TO DECISION-MAKING 

2. BASICS ON PROBABILITIES AND DISTRIBUTION 

3. MEAN AND STANDARD DEVIATION 

4. CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

5. PREDICTING OF EVENTS 

6. MAKING DECISIONS 

7. APPLICATION: SOUTHWEST AIRLINES 

1.0 

**WHY WE NEED A SCIENTIFIC APPROACH TO DECISION-MAKING** 
WHY WE NEED A SCIENTIFIC APPROACH TO DECISION-MAKING 

"In just a few short weeks on the job, I had already realized that because every tough decision came down to a probability, then certainty was an impossibility — which could leave me encumbered by the sense that I could never get it quite right. So rather than let myself get paralyzed in the quest for a perfect solution, or succumb to the temptation to just go with my gut every time, I created a sound decision-making process — one where I really listened to the experts, followed the facts, considered my goals and weighed all of that against my principles. Then, no matter how things turned out, I would at least know I had done my level best with the information in front of me.” BARACK OBAMA 
WHY WE NEED A SCIENTIFIC APPROACH TO DECISION-MAKING 

## Poll time! 

How many subscribers did Disney Plus secure in its first year of existence? 

A) 10 millions B) 20 millions C) 40 millions D) 70 millions 

In November 2019, Disney launched its new Disney+ streaming service. 

When journalists asked Reed Hastings (the boss of Netflix) how he thought Disney+ was going to perform in its first year, Hastings said it would secure 20 million subscribers “at best” . 

At the time, Netflix had about 160 million subscribers. Its streaming service was launched in 2007. 
WHY WE NEED A SCIENTIFIC APPROACH TO DECISION-MAKING 

## Poll time! 

How many total ChotuKool units did Godrej sell in the first two years? 

A) 15,000 B) 300,000 C) 2,500,000 D) 12,000,000 

In 2008, Indian household appliances manufacturer Godrej introduced ChotuKool , a low-cost refrigerator targeted at the hundreds of millions of Indians who could not afford a regular refrigerator or did not have stable access to electricity. The COO (chief operating officer) of Godrej said that they were expecting to sell “ probably millions ” of units in the first three years. 
WHY WE NEED A SCIENTIFIC APPROACH TO DECISION-MAKING 
WHY WE NEED A SCIENTIFIC APPROACH TO DECISION-MAKING 

## February 2019 

BMW and Daimler announced that they would invest $1 billion in Free Now , their car-sharing joint venture. 

Free Now included Share Now, the division centered on short-term car rentals, that already had 4m customers in more than 30 cities under the BMW brand DriveNow and Daimler’s Car2go. 

The plan was to extend Free Now’s services to another 90 cities and grow tenfold in the next three years. 
WHY WE NEED A SCIENTIFIC APPROACH TO DECISION-MAKING 

## December 2019 

BMW and Daimler announced that Free Now would leave the United States and Canada due the “volatile state of the global mobility landscape” and the “rising infrastructure complexities facing North American transportation”. 

The business also said it would leave Brussels, London and Florence due to “low adoption rates”. 

DriveNow and Car2Go, which had already pulled out of more than a dozen locations, will continue to operate in 18 European cities, including seven in Germany. 
WHY WE NEED A SCIENTIFIC APPROACH TO DECISION-MAKING 
WHY WE NEED A SCIENTIFIC APPROACH TO DECISION-MAKING 

Uncertainty rules also in our daily lifes 

Think about weather forecast: which one is more informative? 

**----- Start of picture text -----**<br>
MON TUE WED THU FRI<br>MON TUE WED THU FRI<br>Chance of<br>Chance of  rainfall:  Chance of  Chance of  Chance of<br>rainfall: 20% 40% rainfall: 90% rainfall: 70% rainfall: 80%<br>**----- End of picture text -----**<br>
WHY WE NEED A SCIENTIFIC APPROACH TO DECISION-MAKING 

## 3 main goals 

In this class we will learn how to make predictions using probability and updating our beliefs to make better decisions 

## **BE LESS CERTAIN** 

Overconfidence depends on culture, personality, expertise, … 

**LEARN TO MAKE PREDICTIONS** 

Question how often an outcome typically happen 

**THINK PROBABILISTICALLY** Have a theory to envision probability of events 

2.0 

**BASICS ON PROBABILITIES AND DISTRIBUTIONS** 
BASICS ON PROBABILITIES AND DISTRIBUTIONS 

Let’s introduce probability 

**https://www.khanacademy.org/math/cc-seventhgrade-math/cc-7th-probability-statistics/cc-7th-basicprob/v/basic-probability** 
BASICS ON PROBABILITIES AND DISTRIBUTIONS 

A random variable is a variable that can take on some values (x1, x2, ..xn). Each value is assigned a probability (p1, p2, .. pn) 

Random variable Possible values Random events Probability **0 0.5 X = 1 0.5** 
BASICS ON PROBABILITIES AND DISTRIBUTIONS 

## Random variables - values 

## **CONTINUOUS** 

Variables that take on a value in a range 

**QUALITATIVE / CATEGORICAL** 

Variables that do not come from measuring or counting 

**DICHOTOMOUS / BINARY** 

Variables that can take on only two values 
BASICS ON PROBABILITIES AND DISTRIBUTIONS 

## We define **PROBABILITIES** 

Probabilities indicate the likelihood of the occurrence of a random event Probabilities are a sequence of numbers [0,1] that have to sum up to 1 
BASICS ON PROBABILITIES AND DISTRIBUTIONS 

||||
|---|---|---|
|Values|Probabilities|Cumulative<br>Probabilities|
|10|0.20|0.20|
|20|0.10|0.30|
|30|0.20|0.50|
|40|0.20|0.70|
|50|0.10|0.80|
|60|0.05|0.85|
|70|0.10|0.95|
|80|0.05|1.00|
||||

**A random variable X can take on a certain value based on the assigned probability** 

i.e. the probability of getting a value of  X =10 is 0.2 or 20% 
BASICS ON PROBABILITIES AND DISTRIBUTIONS 

||||
|---|---|---|
|Values|Probabilities|Cumulative<br>Probabilities|
|10|0.125|0.125|
|20|0.125|0.250|
|30|0.125|0.375|
|40<br>50|0.125<br>0.125|0.500<br>0.625|
|60|0.125|0.750|
|70|0.125|0.875|
|80|0.125|1.000|
||||

**UNIFORM DISTRIBUTION Each value has the same probability X has an equal likelihood of being any of these 8 outcomes.** 

i.e. the variable can take on 8 different values (10, 20, 30, .., 80) but the probability of each value is always 12.5% 
BASICS ON PROBABILITIES AND DISTRIBUTIONS 

## Graphical representation: rolling a die has a uniform distribution 

**----- Start of picture text -----**<br>
0.15<br>0.10<br>0.05<br>0<br>1 2 3 4 5 6<br>outcome<br>probability<br>**----- End of picture text -----**<br>
# How informative is the uniform distribution? 
BASICS ON PROBABILITIES AND DISTRIBUTIONS 

||||
|---|---|---|
|Values|Probabilities|Cumulative<br>Probabilities|
|10|0.02|0.02|
|20|0.08|0.10|
|30|0.15|0.25|
|40|0.25|0.50|
|50|0.25|0.75|
|60|0.15|0.90|
|70|0.08|0.98|
|80|0.02|1.00|
||||

**NORMAL DISTRIBUTION In a normal distribution, the outcomes tend to distribute around a central value** 

i.e. in the table: Which values are more likely? And which ones are less likely? 
Can you think of examples where you may observe a normal distribution? 
BASICS ON PROBABILITIES AND DISTRIBUTIONS 

**----- Start of picture text -----**<br>
Grade distribution<br>**----- End of picture text -----**<br>
BASICS ON PROBABILITIES AND DISTRIBUTIONS 

||||
|---|---|---|
|Values|Probabilities|Cumulative<br>Probabilities|
|10|0.02|0.02|
|20|0.03|0.05|
|30|0.05|0.10|
|40|0.05|0.15|
|50|0.10|0.25|
|60|0.15|0.40|
|70|0.40|0.80|
|80|0.20|1.00|
||||

**NORMAL DISTRIBUTION Left skewed** : The values of the observations cluster more around the right side of the distribution 
BASICS ON PROBABILITIES AND DISTRIBUTIONS 
BASICS ON PROBABILITIES AND DISTRIBUTIONS 

||||
|---|---|---|
|Values|Probabilities|Cumulative<br>Probabilities|
|10|0.20|0.20|
|20|0.40|0.60|
|30|0.15|0.75|
|40|0.10|0.85|
|50|0.05|0.90|
|60|0.05|0.95|
|70|0.03|0.98|
|80|0.02|1.00|
||||

**NORMAL DISTRIBUTION Right skewed** : values cluster more around the left side of the distribution 
BASICS ON PROBABILITIES AND DISTRIBUTIONS 

3.0 

**MEAN AND STANDARD DEVIATION** 
MEAN AND STANDARD DEVIATION 

## Summary Statistics (or moments) 

**PROBABILITY DISTRIBUTIONS HAVE SUMMARY STATISTICS, OR MOMENTS** 

**SUMMARY STATISTICS ARE USED TO DESCRIBE DATA OR THE SAMPLE** 

**THE TWO MOST IMPORTANT STATISTICS ARE** 

- Mean 

- Standard deviation 

- (= square root of the variance) 
# Do you think Bocconi’s students are tall or short? 
MEAN AND STANDARD DEVIATION 

## Mean 

## **Probably you have no clue!** 

Mean =175 cm 

Height of 15,000 students at Bocconi 

But if I tell you that the mean of the height of Bocconi students is 175 cm, then what would you answer? 

And if now I tell you that the mean of the height of the students at Politecnico is 180 cm, then what would you answer? 

**ONE NUMBER CAN TELL YOU A LOT ABOUT MANY NUMBERS** 
MEAN AND STANDARD DEVIATION 

## Variance (or standard deviation) 

**The mean tells you where the center of the distribution is positioned** 

Means do not tell you whether the values of the observations are concentrated around it, or dispersed away from it 

Mean =175 cm 

Height of 15,000 students at Bocconi 

Small variance : most of the Bocconi students’ heights are around 175 cm High variance: many Bocconi students are either very short (155 cm) or very tall (195 cm) 
MEAN AND STANDARD DEVIATION 
MEAN AND STANDARD DEVIATION 
MEAN AND STANDARD DEVIATION 

|MEAN AND STANDARD DEVIATION|MEAN AND STANDARD DEVIATION|MEAN AND STANDARD DEVIATION|
|---|---|---|
||||
|Values<br>Probabilities<br>Cumulative<br>Probabilities|**Mean formula:**μ = σ𝑖=𝟏<br>𝑛<br>𝑝𝑖𝑥𝑖**,**<br>Where xiis the value of an observation, and<br>piis the probability of whether that value<br>occurs.<br>The mean of the distribution in the table is:<br>10*0.20 + 20*0.10 + 30*0.20 + 40*0.20<br>50*0.10 + 60*0.05 + 70*0.10 + 80*0.05 =**37**|+|
|10<br>0.20<br>0.20|||
|20<br>0.10<br>0.30|||
|30<br>0.20<br>0.50|||
|40<br>0.20<br>0.70|||
|50<br>0.10<br>0.80|||
|60<br>0.05<br>0.85|||
|70<br>0.10<br>0.95|||
|80<br>0.05<br>1.00|||

The mean of the distribution in the table is: 10*0.20 + 20*0.10 + 30*0.20 + 40*0.20 + 50*0.10 + 60*0.05 + 70*0.10 + 80*0.05 = **37** 
MEAN AND STANDARD DEVIATION 

||39<br>**Variance formula:**<br>𝜎2 = σ𝑖=𝟏<br>𝑛<br>𝑝𝑖<br>𝑥𝑖−𝜇2**,**<br>Where xiis the value of an observation, and piis<br>the probability of whether that value occurs<br>The variance of the distribution in the table is:<br>(10 – 37)2*0.20 + (20 – 37)2*0.10 +<br>(30 – 37)2*0.20 + (40 – 37)2*0.20 +<br>(50 – 37)2*0.10 + (60 – 37)2*0.05 +<br>(70 – 37)2*0.10 + (80 – 37)2*0.05 =**431**<br>**Standard deviation =**<br>𝑽𝒂𝒓𝒊𝒂𝒏𝒄𝒆<br>What’s the value of the standard deviation of the<br>distribution?|
|---|---|
|||
|Values<br>Probabilities<br>Cumulative<br>Probabilities|**Variance formula:**<br>𝜎2 = σ𝑖=𝟏<br>𝑛<br>𝑝𝑖<br>𝑥𝑖−𝜇2**,**<br>Where xiis the value of an observation, and piis<br>the probability of whether that value occurs<br>The variance of the distribution in the table is:<br>(10 – 37)2*0.20 + (20 – 37)2*0.10 +<br>(30 – 37)2*0.20 + (40 – 37)2*0.20 +<br>(50 – 37)2*0.10 + (60 – 37)2*0.05 +<br>(70 – 37)2*0.10 + (80 – 37)2*0.05 =**431**<br>**Standard deviation =**<br>𝑽𝒂𝒓𝒊𝒂𝒏𝒄𝒆<br>What’s the value of the standard deviation of the<br>distribution?|
|10<br>0.20<br>0.20||
|20<br>0.10<br>0.30||
|30<br>0.20<br>0.50||
|40<br>0.20<br>0.70||
|50<br>0.10<br>0.80||
|60<br>0.05<br>0.85||
|70<br>0.10<br>0.95||
|80<br>0.05<br>1.00||

What’s the value of the standard deviation of the distribution? 
MEAN AND STANDARD DEVIATION 

## Poll time! 

What type of variable is “Family_firm”? A) Qualitative B) Continuous C) Dichotomous 

||||||||||
|---|---|---|---|---|---|---|---|---|
||Year|ID|Family_firm|ROE|ROA||Turnover|Sector|
||2019|1|1|12.10|10.60|58,155.96||Manufacturing|
||2019|2|0|9.80|6.74|316,792.54||Fashion|
||2019|3|0|5.42|3.15|22,631.89||Transport andlogistics|
||2019|4|0|2.44|1.85|136,295.32||Metalproducts|
||2019|5|0|6.37|2.66|51,651.85||Transport andlogistics|
||2019|6|1|16.59|5.86|48,288.88||Wholesale|
||2019|7|1|30.41|7.26|152,355,00||Manufacturing|
||2019|8|1|9.94|5.22|36,519.24||Fashion|
||2019|9|0|9.40|4.71|194,447.17||Wholesale|
||2019|10|0|-12.81|-4.35|338,855.24||Metal products|
||||||||||
MEAN AND STANDARD DEVIATION 

## Poll time! 

What type of variable is “Turnover”? A) Qualitative B) Continuous C) Dichotomous 

||||||||||
|---|---|---|---|---|---|---|---|---|
||Year|ID|Family_firm|ROE|ROA||Turnover|Sector|
||2019|1|1|12.10|10.60|58,155.96||Manufacturing|
||2019|2|0|9.80|6.74|316,792.54||Fashion|
||2019|3|0|5.42|3.15|22,631.89||Transport andlogistics|
||2019|4|0|2.44|1.85|136,295.32||Metalproducts|
||2019|5|0|6.37|2.66|51,651.85||Transport andlogistics|
||2019|6|1|16.59|5.86|48,288.88||Wholesale|
||2019|7|1|30.41|7.26|152,355,00||Manufacturing|
||2019|8|1|9.94|5.22|36,519.24||Fashion|
||2019|9|0|9.40|4.71|194,447.17||Wholesale|
||2019|10|0|-12.81|-4.35|338,855.24||Metal products|
||||||||||
MEAN AND STANDARD DEVIATION 

## Poll time! 

What type of variable is “Sector”? 

A) Qualitative B) Continuous C) Binary 

||||||||||
|---|---|---|---|---|---|---|---|---|
||Year|ID|Family_firm|ROE|ROA||Turnover|Sector|
||2019|1|1|12.10|10.60|58,155.96||Manufacturing|
||2019|2|0|9.80|6.74|316,792.54||Fashion|
||2019|3|0|5.42|3.15|22,631.89||Transport andlogistics|
||2019|4|0|2.44|1.85|136,295.32||Metalproducts|
||2019|5|0|6.37|2.66|51,651.85||Transport andlogistics|
||2019|6|1|16.59|5.86|48,288.88||Wholesale|
||2019|7|1|30.41|7.26|152,355,00||Manufacturing|
||2019|8|1|9.94|5.22|36,519.24||Fashion|
||2019|9|0|9.40|4.71|194,447.17||Wholesale|
||2019|10|0|-12.81|-4.35|338,855.24||Metal products|
||||||||||
MEAN AND STANDARD DEVIATION 

## Poll time! 

What type of variable is “ROE”? 

A) Qualitative B) Continuous C) Dichotomous 

||||||||||
|---|---|---|---|---|---|---|---|---|
||Year|ID|Family_firm|ROE|ROA||Turnover|Sector|
||2019|1|1|12.10|10.60|58,155.96||Manufacturing|
||2019|2|0|9.80|6.74|316,792.54||Fashion|
||2019|3|0|5.42|3.15|22,631.89||Transport andlogistics|
||2019|4|0|2.44|1.85|136,295.32||Metalproducts|
||2019|5|0|6.37|2.66|51,651.85||Transport andlogistics|
||2019|6|1|16.59|5.86|48,288.88||Wholesale|
||2019|7|1|30.41|7.26|152,355,00||Manufacturing|
||2019|8|1|9.94|5.22|36,519.24||Fashion|
||2019|9|0|9.40|4.71|194,447.17||Wholesale|
||2019|10|0|-12.81|-4.35|338,855.24||Metal products|
||||||||||
MEAN AND STANDARD DEVIATION 

## Poll time! 

How do you expect turnover to be distributed? A) Normally distributed B) Left skewed C) Right skewed 

||||||||||
|---|---|---|---|---|---|---|---|---|
||Year|ID|Family_firm|ROE|ROA||Turnover|Sector|
||2019|1|1|12.10|10.60|58,155.96||Manufacturing|
||2019|2|0|9.80|6.74|316,792.54||Fashion|
||2019|3|0|5.42|3.15|22,631.89||Transport andlogistics|
||2019|4|0|2.44|1.85|136,295.32||Metalproducts|
||2019|5|0|6.37|2.66|51,651.85||Transport andlogistics|
||2019|6|1|16.59|5.86|48,288.88||Wholesale|
||2019|7|1|30.41|7.26|152,355,00||Manufacturing|
||2019|8|1|9.94|5.22|36,519.24||Fashion|
||2019|9|0|9.40|4.71|194,447.17||Wholesale|
||2019|10|0|-12.81|-4.35|338,855.24||Metal products|
||||||||||

4.0 

# **CONDITIONAL PROBABILITY AND JOINT PROBABILITY** 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

## What is **conditional probability?** 

The probability of an event (situation, characteristic, condition, …) occurring given that another event has already taken place 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

## Conditional probability is everywhere 

- If you want to know the probability that your friend has Covid, it is useful to know whether she is vaccinated! 

- If you want to know the probability that Messi goes back to Barcelona FC the next season, it is useful to know whether the team can afford to pay him 

- If you want to know the probability that customers will buy your new product, it is useful to know what a sample of them think of the test version. 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

## Should Share Now be in Barcelona? 

Madrid is currently the only city in Spain in which Share Now operates. 

You are an intern at Share Now and your boss **assess** asks you to **the business case of entering Barcelona** . 

That is, they want to know how **probable** it is that Share Now could turn a profit in that city. Your boss told you that they want the average subscriber to drive at least 20 hours per year. What **variables** do you think the probability of turning a profit could depend on? 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

## Should Share Now being in Barcelona? 

Consider **per-capita income** . 

Is it make more likely that Share Now will turn a profit in the city? 

- Maybe yes (high-income people do not like to waste time in the traffic and are ready to pay for rental of small cars) 

- Maybe not (high-income people like to own their car) 

- Maybe it has not impact (not a variable or different effects that balance each other) 

You usually need to **check data** to know whether an event (like profit) depend on something else (like per-capita income). 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

Expected Probability in Brief You have just met a person. 

You have to guess how many letters she has in her name. 

What would you say? 

Would you change your answer if I tell you she is from Korea? 
Who is more likely to have short last names - Italians or Koreans? 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

||Area of origin|
|---|---|
||Italy<br>Asia Others MARGINAL|
|# letters<br>in last<br>name<br>(X)|2<br>0<br>2<br>0<br>2|
||3<br>1<br>5<br>0<br>6|
||4<br>3<br>1<br>0<br>4|
||5<br>9<br>2<br>2<br>13|
||<br>6<br>8<br>2<br>4<br>14|
||<br>7<br>21<br>0<br>5<br>26|
||8<br>9<br>0<br>2<br>11|
||9<br>7<br>0<br>2<br>9|
||10<br>4<br>0<br>0<br>4|
||11<br>1<br>0<br>0<br>1|
||14<br>0<br>0<br>2<br>2|
||23<br>0<br>0<br>1<br>1|
||MARGINAL<br>63<br>12<br>18<br>93|

The frequency table to the left reports the number of letters of the last name of 93 student ~~s~~ based on whether originate from Ital Asia or somewhere else ~~y,~~ 

**The number of letters in the last name is our random variable X** 

- This type of table is called a “ **contingency table** ”: it shows the values of X contingent on another variable. 

- The totals of rows and columns are **marginal frequencies** (that is, the “last” row/column). 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

||Area of origin|
|---|---|
||Italy<br>Asia Others MARGINAL|
|# letters<br>in last<br>name<br>(X)|2<br>0<br>2<br>0<br>2|
||3<br>1<br>5<br>0<br>6|
||4<br>3<br>1<br>0<br>4|
||5<br>9<br>2<br>2<br>13|
||<br>6<br>8<br>2<br>4<br>14|
||<br>7<br>21<br>0<br>5<br>26|
||8<br>9<br>0<br>2<br>11|
||9<br>7<br>0<br>2<br>9|
||10<br>4<br>0<br>0<br>4|
||11<br>1<br>0<br>0<br>1|
||14<br>0<br>0<br>2<br>2|
||23<br>0<br>0<br>1<br>1|
||MARGINAL<br>63<br>12<br>18<br>93|

## Conditional probability: P(X|Y) 

What is the probability of a student with 5 letters in his or her last name? E.g. 13/93 = 13.9% 

What is the probability of a student with 5 letters in his or her last name given that the student is Italian? E.g. P(X=5|Italy) = 9/63 = 14.3% 

**The conditioning event is often called a condition, clue, data point or signal (being Italian)** 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

## What is **Conditional Expectation?** 

The expected value of a random variable, given that another event has already taken place 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

||Area of origin|
|---|---|
||Italy<br>Asia Others MARGINAL|
|# letters<br>in last<br>name<br>(X)|2<br>0<br>2<br>0<br>2|
||3<br>1<br>5<br>0<br>6|
||4<br>3<br>1<br>0<br>4|
||5<br>9<br>2<br>2<br>13|
||<br>6<br>8<br>2<br>4<br>14|
||<br>7<br>21<br>0<br>5<br>26|
||8<br>9<br>0<br>2<br>11|
||9<br>7<br>0<br>2<br>9|
||10<br>4<br>0<br>0<br>4|
||11<br>1<br>0<br>0<br>1|
||14<br>0<br>0<br>2<br>2|
||23<br>0<br>0<br>1<br>1|
||MARGINAL<br>63<br>12<br>18<br>93|

Conditional expectation: E(X|Y) = σ𝑛𝑖=𝟏 𝑝(𝑥𝑖| Y ) 𝑥𝑖 That is, you multiply all the values by their respective conditional probabilities, contingent on Y, and then you add them up. E(X | Italy) =  2*  0/63 + 3*  1/63 + 4* 3/63 + 5* 9/63 + 6*  8/63 + 7* 21/63 + 8*  9/63 + 9* 7/63 + 10*  4/63 + 11* 1/63 + 14*  0/63 + 23* 0/63 = 7 

E( X | Italy) = 7 = # of letters the last name will have on average given the student is Italian. 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

## What is **Joint probability?** 

The probability that two events take place together at the same time 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

||Area of origin|
|---|---|
||Italy<br>Asia Others MARGINAL|
|# letters<br>in last<br>name<br>(X)|2<br>0<br>2<br>0<br>2|
||3<br>1<br>5<br>0<br>6|
||4<br>3<br>1<br>0<br>4|
||5<br>9<br>2<br>2<br>13|
||<br>6<br>8<br>2<br>4<br>14|
||<br>7<br>21<br>0<br>5<br>26|
||8<br>9<br>0<br>2<br>11|
||9<br>7<br>0<br>2<br>9|
||10<br>4<br>0<br>0<br>4|
||11<br>1<br>0<br>0<br>1|
||14<br>0<br>0<br>2<br>2|
||23<br>0<br>0<br>1<br>1|
||MARGINAL<br>63<br>12<br>18<br>93|

Joint probability: P(X,Y) = P(X|Y)*P(Y) 

That is, the probability that **Y happens** times the probability that **X happens once we know that Y happened** 

E.g. 

P(X=5, Italy) = P(X=5 | Italy) * P (Italy) = = 9/63*63/93 = 14.3% * 67.7% = **9.7%** = probability that the student is Italian **AND** the last name has 5 words 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

Notice the difference between conditional and joint probabilities 

**CONDITIONAL PROBABILITY JOINT PROBABILITY P(X|Y) P(X,Y)= P(X|Y)*P(Y)** P(X=5|Italy) = 9/63 = 14.3% P(X=5, Italy) = 9/63*63/93 = 9.7% 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

## Let’s practice 

A TLC company is investigating its retention of customers. It selected a sample of 2,185 customers who signed the contract five years ago. Some of them remained (they still have the contract), others left to other providers. 

The company believes that the **age group** of customers could have an impact on the retention rate. 

||Gen Z (up to 24)|Millennials (25-<br>40)|Gen X (41-56)|Boomers and<br>older(57+)|TOTAL|
|---|---|---|---|---|---|
|Remained|200|115|180|210|705|
|Left|120|160|530|670|1,480|
|TOTAL|320|275|710|880|2,185|
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

## Let’s practice 

## In this sample: 

- what is the probability of **retaining a customer** ? 

- what is the probability of **retaining a Gen Z customer** ? 

## • what is the probability of **being a Gen Z customer who remains** ? 

||Gen Z (up to 24)|Millennials (25-<br>40)|Gen X (41-56)|Boomers and<br>older(57+)|TOTAL|
|---|---|---|---|---|---|
|Remained|200|115|180|210|705|
|Left|120|160|530|670|1,480|
|TOTAL|320|275|710|880|2,185|
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

## Independence 

Do you remember per-capita income and Share Now in Barcelona? It is always possible that a variable is not relevant . 

- If the conditioning event , or signal, is independent from the event we are interested in, then it does not help predict it 

- In this case, the signal, is not informative 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

## What is the joint probability of rolling two 6’s? 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

Joint probability with independent events: rolling two dices 

**EVENT 1** 

**EVENT 2** 

**JOINT PROBABILITY OF EVENT 1 AND 2** 

probability of rolling 6 in the first roll = 1/6 

probability of rolling 6 in the second roll = 1/6 

probability of (EVENT 1) X probability of (EVENT 2) = 1/6 X 1/6 

Joint probability: P(X,Y) = P(X|Y)*P(Y) But, if X and Y are independent, P(X|Y) = P(X) So, in case of independence: Joint probability = P(X|Y)*P(Y) = P(X)*P(Y) 

In this case, X = probability of rolling 6 in the first round Y = probability of rolling 6 in the second round 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

||Area of origin|
|---|---|
||Italy<br>Asia Others MARGINAL|
|# letters<br>in last<br>name<br>(X)|2<br>0<br>2<br>0<br>2|
||3<br>1<br>5<br>0<br>6|
||4<br>3<br>1<br>0<br>4|
||5<br>9<br>2<br>2<br>13|
||<br>6<br>8<br>2<br>4<br>14|
||<br>7<br>21<br>0<br>5<br>26|
||8<br>9<br>0<br>2<br>11|
||9<br>7<br>0<br>2<br>9|
||10<br>4<br>0<br>0<br>4|
||11<br>1<br>0<br>0<br>1|
||14<br>0<br>0<br>2<br>2|
||23<br>0<br>0<br>1<br>1|
||MARGINAL<br>63<br>12<br>18<br>93|

Independence is a matter of degree! 

P(X=5 | Italy) = 9/63 = **14.3%** P(X=5) = 13/93 = **14.0%** 

Although the two events (five letters and being Italian) are not independent, the conditional probability (five letters when you are Italian) is very close to the marginal probability of having five 5 letters… 

So, being Italian is not a very informative signal. 
CONDITIONAL PROBABILITY AND JOINT PROBABILITY 

||Area of origin|
|---|---|
||Italy<br>Asia Others MARGINAL|
|# letters<br>in last<br>name<br>(X)|2<br>0<br>2<br>0<br>2|
||3<br>1<br>5<br>0<br>6|
||4<br>3<br>1<br>0<br>4|
||5<br>9<br>2<br>2<br>13|
||<br>6<br>8<br>2<br>4<br>14|
||<br>7<br>21<br>0<br>5<br>26|
||8<br>9<br>0<br>2<br>11|
||9<br>7<br>0<br>2<br>9|
||10<br>4<br>0<br>0<br>4|
||11<br>1<br>0<br>0<br>1|
||14<br>0<br>0<br>2<br>2|
||23<br>0<br>0<br>1<br>1|
||MARGINAL<br>63<br>12<br>18<br>93|

What about whether being Asian or Italia ~~n~~ predicts whether your last name has 3 letters? 

P(X=3 | Asia)= 5/12 = 41.7% P(X=3) = 6/93 = 6.4% 

P(X=3 | Italy) = 1/63 = 1.6% P(X=3) = 6/93 = 6.4% 

Which one is more informative? Remember: prediction can go either ways 
Optional: podcast episode on using scientific thinking in business decision making 

5.0 

**PREDICTION OF EVENTS** 
PREDICTION OF EVENTS 

Why is probability relevant to management? 

**PREDICT EVENTS** 

## **DECIDE ACTIONS** 
PREDICTION OF EVENTS 

## Why is the new robot failing? 

Your company has recently bought a new robot for the factory, which has shown signs of malfunction. The robot starts regularly but after a few hours, on certain days, it comes to a halt all of a sudden. 

After thinking about why this may be the case, you hypothesize that the robot fails . **when the temperature in the factory is low** So, you ask your engineers to have a look at the factory records and collect the temperatures of the days the robot failed. 
PREDICTION OF EVENTS 

## Poll time! 

Are the failures of the robot due to low temperature? 

A) Yes B) No 

The engineers came back with this graph, which tells you the number of accidents at different recorded temperatures. 

50 degrees F = 10 degrees C 75 degrees F = 23.9 degrees C 
PREDICTION OF EVENTS 

## Think again 

Your theory is an if-then statement. 

If the temperature in the factory is low, then the robot fails. 

How do you test this theory? 

By looking at **all the days** in which the temperature is low, and then checking whether the robot fails on those days. 

It’s like the theory: “If mum is happy, she gives me chocolate”. You want her to give you chocolate **every time** she is happy. 
PREDICTION OF EVENTS 

## You need more data 

The engineers gave you only the temperatures of **the days when the robot failed** . 

What about the **days without incidents** ? Maybe the temperature was low on those days too and nothing happened… 

You tell the engineers. 

They come up with a new graph with the temperatures of all the days in which the robot operated. 
PREDICTION OF EVENTS 

## The complete graph 

What’s your conclusion now? 
PREDICTION OF EVENTS 

## Table version 

||Days with<br>accidents|Days<br>without<br>accidents|Total|
|---|---|---|---|
|Low<br>temp<br>(< 65° F)|6|0|6|
|High<br>temp<br>(≥ 65° F)|4|17|21|
|Total|10|17|27|

The first graph showed you only the first column (days with incidents). You could calculate: P(Low temperature | accident) = = 6/10 = 60% 

But, to test your theory, what you need is the full table to test this probability: 

P(accident | Low temperature) = = 6/6 = 100% 
## It wasn’t actually a robot 

https://www.youtube.com/watch?v=yibNEcn-4yQ 
PREDICTION OF EVENTS 

## It wasn’t actually a robot 
PREDICTION OF EVENTS 

## Definition of **theory** 

- A series of logical steps linking antecedents to consequences 

- If P then Q, if Q then R, if R then S, ..., if V then Z ... You eventually show that if P then Z 
PREDICTION OF EVENTS 

## Why are theories important? 

- Theories tell you what data / factors to examine 

- The factors that affect your outcome improve your ability to make an accurate prediction 

- The data that you find provide signals for your conditional probabilities, i.e., for improving your predictions 

In practice: 

1. You theorize “if A, then B” 

2. You collect all the cases with A, and then you measure B in them 

3. You calculate P(B|A) 

4. If needed, you repeat with a theory about A, and so on 
We need to pay attention to the data we collect (representative, large sample) 
PREDICTION OF EVENTS 

## How to predict events 

## **You have a target event** 

**You want to predict whether it will occur** 

Example: are there at least 10 supporters of Inter Milan in this class? 
PREDICTION OF EVENTS 

Step 1 

# **We need a theory!** 
PREDICTION OF EVENTS 

Step 1 

What’s your theory? 

What theory do you have to evaluate whether or not there are at least 10 supporters of Inter Milan in the class? What factors would you use to build your theory? 

Maybe you look around and check how many male students there are in the class. Or, how many are from Milan. 
PREDICTION OF EVENTS 

Step 1 What’s your theory? 

Based on your theory, you envision a certain probability (e.g. 60%) that there can be at least 10 supporters of Inter Milan in the class. This is called prior probability. 

Prior probability is the predicted probability of an event before data is collected . It is the best assessment of the probability of an outcome based on the current knowledge 
PREDICTION OF EVENTS 

Step 2 

Revise your theory 

Now that you have a prior probability you decide whether to continue with this probability or to look for more information/signals. 

Signals are costly and you usually cannot collect too many of them. 

At least two ways to collect signals: 

1. Ask others (experts) 

2. Collect data (data analysis) 

How do you apply them to your research on Inter Milan supporters? 
PREDICTION OF EVENTS 

Step 2 

Revise your theory: 

Try to improve your prior probability by asking the classmates sitting close to you what they think the probability of having at least 10 students supporting Inter Milan is. 

- Ask others 
PREDICTION OF EVENTS 

Step 2 

Revise your theory: 

- Ask others 

- They say 80% ... In this case you may update your probability to a higher level than your prior of 60% (e.g. to 70%) 

- They say 40% ... in which case you update your probability to a lower level than your prior of 60%  (e.g. to 50% ) . 

- The new probability is a posterior probability 

Posterior probability is the revised probability of an event occurring after taking new information into account. 
PREDICTION OF EVENTS 

Step 2 

Revise your theory: 

Let’s collect data now. 

Take a sample of 20 students in the class and check how many of them are supporters of Inter Milan. 

   - If they are at least 2 (10%), update your posterior probability upward 

   - If not, update your posterior probability downward 

- Collect data 
PREDICTION OF EVENTS 

## Predict events 

**STEP 1 – THEORY** 

You look at the class (100 students) with a theory in mind. You set a prior . probability 

**STEP 2 – LOOK FOR MORE INFORMATION** 

Then you ask friends (experts and collect data). 

You update you prior probability (multiple times), generating posterior probabilities 

**STEP 3 – DEFINE YOUR EXPECTATIONS** 

You decide when to stop collecting data/signals and to finalize your probability , that is, a posterior probability that you cannot improve further 
PREDICTION OF EVENTS 

## Technically 

**P(Y) = 60%** 

**PRIOR PROBABILITY** 

Y = at least 10 students in the class support Inter Milan 

**P(Y|S) = PROBABILITY OF EVENT Y GIVEN THE OBSERVED SIGNAL S** 

S: what the data or your friends told you 

- If S = 80% → P(Y|S=80%) = 70% 

- If S = 40% → P(Y|S=40%) = 50% 
PREDICTION OF EVENTS 

## Technically 

There could be a series of priors, signals, posteriors, in which each posterior becomes the prior before the next signal 

s1 s2 s3 P(Y)              P(Y | s1) P(Y | s1,s2) P(Y | s1,s2,s3) 

For example: 

- P(Y) =60%, 

- Data tell you S1=40%, 

- You update P(Y | S1=40%) = 50% 

- New data collection tells you S2= 45% 

- • You update P(Y | S1=40%, S2=45%) = 48% 

- • And so on…. 
PREDICTION OF EVENTS 

**So… how many supporters of Inter Milan in this class?** 

6.0 

**MAKING DECISIONS** 
MAKING DECISIONS 

From predicting events to making decisions and estimating payoffs 

## **WHY DO WE NEED TO PREDICT EVENTS?** 

> An event is You want to associated with decide whether or the outcome of an not to take that action action 
MAKING DECISIONS 

From predicting events to making decisions and 

estimating payoffs 

## **WHY DO WE NEED TO PREDICT EVENTS?** 

Example 

Pay 1,000 € upfront, and you receive 100 € per student who support Inter Milan in this class (100 students). Therefore: 

- if at least 10 students support Inter you break-even (total cost = 1,000€; total income = 100€ X 10 students = 1,000€ ) 

- if there are less than 10 supporters, you lose money 

- if there are more than 10 supporters, you gain money 
# Should you pay 1,000€ upfront? How to approach the decision? 
MAKING DECISIONS 

## You are facing this situation 

Scenarios At least 10 Inter Less than 10 Inter Actions supporters supporters Pay 1,000 upfront PROFIT LOSS Not pay 1,000 upfront 0 0 

- Actions = actions you are going to take 

- Scenarios = states of the world you are going to face 
MAKING DECISIONS 

## You are facing this situation 

Scenarios At least 10 Inter Less than 10 Inter Actions supporters supporters Pay 1,000 upfront PROFIT LOSS Not pay 1,000 upfront 0 0 • Actions = actions you are going to take • Scenarios = states of the world you are going to face 

**----- Start of picture text -----**<br>
This is the set of options<br>that is available to you.<br>You decide on this.<br>**----- End of picture text -----**<br>
MAKING DECISIONS 

## You are facing this situation 

Scenarios At least 10 Inter Less than 10 Inter Actions supporters supporters Pay 1,000 upfront PROFIT LOSS Not pay 1,000 upfront 0 0 

- Actions = actions you are going to take 

- Scenarios = states of the world you are going to face 

control it. This is what you PREDICT. 
MAKING DECISIONS 

## You are facing this situation 

**----- Start of picture text -----**<br>
Scenarios At least 10 Inter  Less than 10 Inter<br>Actions supporters  supporters<br>Pay 1,000 upfront PROFIT LOSS<br>Not pay 1,000 upfront 0 0<br>**----- End of picture text -----**<br>

- Actions = actions you are going to take 

- • Scenarios = states of the world you are going to face 

**----- Start of picture text -----**<br>
These are the outcomes of each action-<br>scenario. This is what you are assessing<br>**----- End of picture text -----**<br>
MAKING DECISIONS 

## You are facing this situation 

Scenarios At least 10 Inter Less than 10 Inter Actions supporters supporters Pay 1,000 upfront PROFIT LOSS Not pay 1,000 upfront Neither profit or loss Neither profit or loss 

How to proceed? 

Intuitively, the HIGHER the probability that at least 10 students support Inter Milan, the more likely it is that you get a PROFIT. 

**----- Start of picture text -----**<br>
PREDICT = estimate the probability of the<br>different outcomes<br>**----- End of picture text -----**<br>
MAKING DECISIONS 

## How do you decide? 

Assume your probability is 52%. Do you pay 1,000 upfront? 

And if it is 55%? 

You have already worked on probability estimation. 

You have a final posterior probability. But assume you do not know the real value yet (whether there are at least 10 supporters) 

And if it is 60%? 

**----- Start of picture text -----**<br>
You need a criterion<br>**----- End of picture text -----**<br>
MAKING DECISIONS 

## Establish a criterion 

APPROACH 1 

Think of a threshold probability 

## APPROACH 2 

Assign values (profits and losses) 
MAKING DECISIONS 

## 1. Threshold 

You think of a **threshold** P* such that: 

- if your expected payoff P(Y|S) ≥ P*, then you go ahead with the action 

- if your expected payoff P(Y|S) < P*, then you don’t 

## **IMPORTANT** 

Decision-makers should select the threshold **before** they estimate their expected payoff or see the data. 

Doing it after often generates confirmatory biases (you choose the threshold you want) leading to bad decisions. 
MAKING DECISIONS 

_I recently went clothes shopping in Brooklyn with my friend Emma. Showing off a pretty dress, she tugs at the price tag on the back. “Hey, what does this say?” she asks me. “If it’s less than 80 bucks, I’ll buy it.” Now that’s some decision intelligence! Instead of first seeing the price and then talking herself into a decision she’s already made, she uses the data to drive it. With a well-practiced reflex, she weighs how much she likes the dress and her budget, then sets the decision boundary …_ https://hackernoon.com/data-inspired-5c78db3999b2 

Cassie Kazyrkov | Chied Data Scientist at Google 
MAKING DECISIONS 

2. Assign values 

Given the probability that you have estimated, you assign values to profits and losses in the action-scenario matrix. 

Two approaches. 

- **Value model** (you calculate monetary values of profits and losses that you could make in the different scenarios) 

- **Utility model** (you attribute «utilities» that represent how much you enjoy a positive outcome or how much you suffer a loss) 
MAKING DECISIONS 

## Assign values: Value model 

Scenarios At least 10 Inter Less than 10 Inter Actions supporters supporters Pay 1,000 upfront +500€ -500€ Not pay 1,000 upfront 0 0 

## You estimate that: 

- if there are at least 10 students supporting Inter, on average there are 15 students supporting Inter → revenue – cost = 15x100€ – 1000€ = 500€ 

- if there are fewer than 10 students supporting Inter, on average there are 5 students supporting Inter → revenue – cost = 5x100€ – 1000€ = -500€ 
# Compute the expected value. Is it greater than 0? 
MAKING DECISIONS 

## Assign values: Value model 

Scenarios At least 10 Inter Less than 10 Inter Actions supporters supporters Pay 1,000 upfront +500€ -500€ Not pay 1,000 upfront 0 0 

Expected value (Pay 1,000) = 500 * P(Y|S) – 500 * (1 – P(Y|S) Expected value (Not pay 1,000) = 0 * P(Y|S) + 0 * (1 – P(Y|S) = 0 + 0 = 0 Example: P(Y|S) = 55% 

Expected value (Pay 1,000) = (500 * 0.55) – (500 * (1 – 0.55)) = = (500 * 0.55) – (500 * 0.45) = = 275 – 225 = 50 

**----- Start of picture text -----**<br>
CRITERION: You choose<br>the action with the<br>greater expected value.<br>**----- End of picture text -----**<br>
MAKING DECISIONS 

## Assign values: Value model 

. The value model derives a threshold probability based on the expected outcomes 

Threshold in the value model : the minimum probability required to make the expected value ≥ 0. 

The Expected value is 500 * P(Y|S) – 500 * (1 – P(Y|S) We want: Expected value ≥ 0. 

It is then easy to see that this inequality is true if P(Y|S) ≥ ½ , which will then be your threshold (P* = 50%) 
MAKING DECISIONS 

## Assign values: Utility model 

Utilities : how much you enjoy a positive outcome or how much you suffer from experiencing a loss 

This depends on: 

- Monetary values (money is useful…) 

- Other aspects of the decision 

E.g. you may be very worried about losing money (risk aversion) and the loss of 500 € has a disutility of 400 

Or you are very excited if you run a successful project, and turn the profit of 500 €  has an utility of 800 

Then you calculate the Expected utility of the actions (same as expected value, but with utilities in place of monetary values). 
MAKING DECISIONS 

## Assign values: Utility model 

Scenarios At least 10 Inter Less than 10 Inter Actions supporters supporters Pay 1,000 upfront 800 -400 Not pay 1,000 upfront 0 0 

For instance, you set utility equal to 800 if the project succeeds; -400 if it does not. 

The expected utility is 800*P(Y|S) – 400*(1 – P(Y|S)). Threshold: Expected utility ≥ 0 when P(Y|S) > 1/3 or P* = 33% 
MAKING DECISIONS 

## Value model vs Utility model 

1. The utility model or the value model are formally equivalent. You can see the value model as a special case of the utility model in which your utility depends only on monetary value. 

2. The difference is that you base utility on what is important to you 
MAKING DECISIONS 

## Value model vs Utility model 

**----- Start of picture text -----**<br>
Utility<br>model<br>Value model<br>**----- End of picture text -----**<br>

Broad and rigorous approach to introduce - sense making in managerial decisions Traditional financial planning + probability 
MAKING DECISIONS 

## Wrap up: A framework for managerial decision-making 

**DEFINE ACTIONS AND SCENARIOS** 

**DEFINE A MAP OF ACTIONSCENARIO PAIRS** 

**ESTIMATE THE PROBABILITY** 

## **MAKE A DECISION** 

What are the possible courses of action? What can you control? What you cannot? 

What are the possible combinations? Assign the payoffs derived from pair. 

Have a theory, estimate your priors, and decide whether to revise them 

Based either on a predefined threshold or on monetary valu ~~es~~ /utility 
MAKING DECISIONS 

The framework can accommodate complex decisions Your scenario-action pairs can also have more actions and scenarios, such as the following: 

|<br>such as the following:|||||
|---|---|---|---|---|
||||||
|Scenarios<br>Actions|High<br>demand|Medium<br>demand|Low<br>demand|Very low<br>demand|
|Producegreen hats|profit|profit|profit|loss|
|Produce red hats<br>profit<br>profit<br>loss<br>loss|||||
|Produce blue hats<br>profit<br>profit<br>loss<br>loss|||||
|Do notproduce hats<br>0<br>0<br>0<br>0|||||

In this case you still estimate the probability of the different scenarios, find the highest expected value given these probabilities, and take the action associated with the highest expected value (which could be the default action) 

7.0 

**APPLICATION: SOUTHWEST AIRLINES** 
SOUTHWEST AIRLINES 

## Should Southwest introduce fees? 

We are in 2016. 

- Analysts are pressuring Southwest to introduce fees to increase revenue 

- Southwest’s CEO is worried that fees could undermine customer trust 

How would you apply our framework to this decision? 
SOUTHWEST AIRLINES 

## 1. **Actions** 

General recommendation: let’s keep the model as simple as possible , e.g. minimum number of actions, scenarios, numbers that are easy to calculate, basic theories, etc. There is always time to complicate it later if necessary! **WHAT ACTIONS ARE AVAILABLE TO SOUTHWEST AIRLINES?** 
SOUTHWEST AIRLINES 

1. Actions 

2. **Scenarios** 

Which scenarios are relevant to the actions we are considering? 

- They must be important for our decision 

- They should be out of our control (once we take the action) 

- - We have to be able to estimate  the probability that they happen 

- - They should produce payoffs (values/utilities) (depending on our actions) 

- **WHICH SCENARIOS SHOULD YOU CONSIDER?** 
SOUTHWEST AIRLINES 

1. Actions 

2. Scenarios 

3. **Decision model** 

Let’s choose a decision making framework. Three options: 

- Threshold 

- Value Model 

- Utility Model 

I ~~t’~~ s important that you choose a model you can actually use, given the information that you have. 

**WHICH DECISION MAKING FRAMEWORK DO YOU WANT TO USE?** 
SOUTHWEST AIRLINES 

1. Actions 2. Scenarios 3. Decision model 4. **Utilities** 

Scenarios Customer Customer trust not trust Actions im acted dama ed p g Introduce fees ? ? Not introduce ? ? fees The utility derived should be linked to the strategy that Southwest Airlines is pursuing. 

## **WHAT UTILITIES DO YOU WANT TO INPUT?** 
SOUTHWEST AIRLINES 

1. Actions 2. Scenarios 3. Decision model 4. **Utilities** 

Scenarios Customer Customer trust not trust Actions im acted dama ed p g Introduce fees 100 -300 Not introduce 0 0 fees 

We can assign utilities to reflect the serious damage on Southwest that results from implementing a strategy that damages customer trust 
SOUTHWEST AIRLINES 

1. Actions 2. Scenarios 3. Decision model 4. Utilities 5. **Threshold** 

Scenarios Customer Customer trust not trust Actions im acted dama ed p g Introduce fees 100 -300 Not introduce 0 0 fees 

We can now calculate how probable we want the event ”customer trust not impacted” to be, in order to introduce fees. 

## **WHAT IS THE THRESHOLD?** 
SOUTHWEST AIRLINES 

1. Actions 

2. Scenarios 

3. Decision model 

4. Utilities 5. Threshold 6. **Estimate probability** 

The threshold is 75% . We can now ask ourselves: 

**WHAT IS THE PROBABILITY THAT CUSTOMER TRUST IS NOT IMPACTED BY THE INCREASE IN FEES?** 
SOUTHWEST AIRLINES 

1. Actions 

2. Scenarios 

3. Decision model 

4. Utilities 

5. Threshold 6. Estimate probability - **Have a theory** 

Have a theory : What are the antecedents of customer trust, for an airline company? 

Theory : If an airline company is …, or does …, then customers trust it. 

For example, research shows that trust depends a lot on keeping promises. Is this relevant in this case? 

**WHAT IS YOUR PRIOR THAT CUSTOMER TRUST IS NOT IMPACTED BY THE INCREASE IN FEES?** 
SOUTHWEST AIRLINES 

1. Actions 

2. Scenarios 

3. Decision model 

4. Utilities 

5. Threshold 

6. Estimate probability - Have a theory 

- **Ask experts** 

Ask experts : Who could you speak to, or what data can you look for, to improve your prior? • Consultants 

- Equity analysts 

- Experienced Southwest’s managers 

- What the other airline companies have already done (WestJet, JetBlue) 

- • Loyal customers (surveys, focus groups) 

- 

- …. 

## **DO YOU WANT TO UPDATE YOUR PRIOR?** 
SOUTHWEST AIRLINES 

1. Actions 

2. Scenarios 

3. Decision model 

4. Utilities 5. Threshold 6. Estimate probability - Have a theory - Ask experts - **Collect data** 

Collect data : You could run an experiment on a route or few routes, as suggested by the J.P. Morgan’s analyst. Remember: signals can be costly. Which is the cost of the signal, in this case? 

## **AFTER THE EXPERIMENT (IF YOU RUN IT), YOU ARRIVE AT YOUR FINAL ESTIMATE** 

➢ You make your decision based on whether the final estimate is larger or smaller than the threshold 
SOUTHWEST AIRLINES 

## What did Southwest do? 

It has never changed its fee policy. It has never ran an experiment either. 
SOUTHWEST AIRLINES 

## How did Southwest do? 

**----- Start of picture text -----**<br>
US domestic flights % market share (2010-2019) Operating margin (2010-2019)<br>100.0 25.0%<br>90.0<br>20.8%<br>20.0%<br>80.0 39.8 36.5 36.6 37.0 37.5 19.2% 18.4%<br>51.5 51.7 49.3 46.7 45.2 17.5% 16.6%<br>70.0 15.0% 15.1% 14.8% 14.6%<br>13.6% 13.1% 13.9%13.2%<br>60.0 12.0% 11.9% 12.4%<br>50.0 20.4 20.6 20.7 20.4 19.5 10.0% 8.2% 10.1% 8.6% 9.6%9.3% 8.0% 9.9%<br>15.2 17.9 19.1 6.5% 6.4% 7.2% 7.2%5.8% 7.2%6.1% 6.1% 6.7%<br>40.0 16.9 17.4 5.0% 4.8%4.2%<br>16.5 16.3 16.2 16.8 3.6% 3.3%<br>30.0 16.5<br>14.9 15.2 16.0 0.0% 0.7% 0. 21 %<br>14.3 14.5<br>20.0 16.2 15.7 15.3 15.5 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019<br>10.1 10.1 10.0 13.4<br>10.0 10.4 10.2 -5.0% -4.9%<br>6.9 6.2 10.5 10.1 9.7 9.9 10.2 10.8 11.0 10.8<br>0.0<br>2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 -10.0%<br>United Airlines American Airlines Delta Air Lines American Airlines Delta Air Lines<br>Southwest Others United Airlines Southwest<br>**----- End of picture text -----**<br>

# **THANK YOU** 

