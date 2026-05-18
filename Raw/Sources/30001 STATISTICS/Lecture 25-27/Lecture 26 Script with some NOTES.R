### LECTURE 26 SCRIPT ###
# Bank's customers profitability
# Regression of Profit on Wealth
# SLIDE [43-54] but read also theory in slides and summary

# model estimation
distr.plot.xy(Wealth,Profit,plot.type = "scatter",data = Bank.Invest)
m = lm(Profit ~ Wealth, data = Bank.Invest)
summary(m)

# model validation
plot(m,which=1)
distr.plot.x(m$residuals,plot.type="histogram")

# Relation between residuals and strategy
distr.plot.xy(x=Strategy,y=Profit,plot.type="boxplot",
              data=Bank.Invest)
distr.plot.xy(x=Strategy,y=m$residuals,plot.type="boxplot",
              data=Bank.Invest)
distr.plot.xy(Wealth,Profit,plot.type = "scatter",
              #var.c = Strategy,
              data = Bank.Invest, fitline = TRUE)
# Adding a categorical variable (set of dummy vars) to the model
m  = lm(Profit ~ Wealth + Strategy, data = Bank.Invest)
summary(m)