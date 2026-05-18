### LECTURE 20 SCRIPT ###
### TEST ON POPULATION PROPORTION
# Test on churn rate (slide 71)
phat = 29/150; phat
p0 = 0.22; n = 150;
SE0 = sqrt(p0*(1-p0)/n); SE0
zscore = (phat-p0)/SE0; zscore
pvalue = pnorm(zscore); pvalue

### TEST FOR DIFFERENCE BETWEEN PROPORTIONS
# A/B test on two banner (slide 83)
phatA = 456/2364
phatB = 611/2323
phat0 = (456+611)/(2364+2323)
se0 = sqrt(phat0*(1-phat0)/2364+
  phat0*(1-phat0)/2323); se0
zscore = (phatA-phatB)/se0
zscore
# pvalue
2*pnorm(zscore)

### TEST ON PROPORTIONS FROM RAW DATA ###

# Clients of a bank: test on proportion/s (slide 79)
# Test on the proportion of clients dissatisfied with fees
TEST.prop(x=FeesOK,success="No",p0=0.25,
          alternative="less",data=Bank)

# Test difference in the proportions of clients
# dissatisfied with fees among males and females (slide 86)
Fees.M = Bank$FeesOK[Bank$Sex=="M"]
Fees.F = Bank$FeesOK[Bank$Sex=="F"]

TEST.diffprop(x=Fees.M,y=Fees.F,success.x="No",pdiff0=0)