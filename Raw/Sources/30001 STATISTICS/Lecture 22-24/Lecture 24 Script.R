# Lecture 24 Script

# Example from notes
# x: age
# y: chat time
# Given data:
sumx = 3790; sumy = 77677
sx2 = 88.06; sy2 = 30237.98
rxy = 0.79; n = 96
xbar = sumx/n; ybar = sumy/n

# 1) Model estimation
sxy = rxy*sqrt(sx2*sy2)
b1 = sxy/sx2; b1
b0 = ybar - b1*xbar; b0

# 2) R^2 Calculation
R2 = rxy^2; R2

# 4) Confidence interval for beta_1
SSE = (1-R2)*(n-1)*sy2
sepsilon2 = SSE/(n-2) 
se = sqrt(sepsilon2/((n-1)*sx2)) # estimate of the standard error of betahat_1
t.025 = qt(0.975,n-2)
ME = se*t.025
c(b1-ME,b1+ME)

# 5) Test H0: beta1 = 0 against H1: beta_1 ⧣ 0
# REJECTION REGION with alpha = 0.01
qt(c(0.005,0.995),n-2)
# R.01 = {t-score<-2.63 or t-score>2.63}
tscore = b1/se; tscore
# tscore = 12.49 hence.. REJECT!
pvalue = 2*(1-pt(tscore,n-2)); pvalue # -> REJECT FOR SURE!!!!! COME ON!

# 6) Construct a confidence interval for the expected chat time of
# customers of age = 35
xg = 35
yhat = b0+b1*xg; yhat
se = sqrt(sepsilon2*(1/n+(xg-xbar)^2/((n-1)*sx2)))
ME = se*qt(0.975,n-2)
CI = c(yhat-ME,yhat+ME); CI

# 7) Construct the prediction interval for the chat time of a specific
# 35 year old customer
xg = 35
yhat = b0+b1*xg; yhat
se = sqrt(sepsilon2*(1+1/n+(xg-xbar)^2/((n-1)*sx2))) # only add +1 in brackets
ME = se*qt(0.975,n-2)
PI = c(yhat-ME,yhat+ME); PI # prediction interval is wider!