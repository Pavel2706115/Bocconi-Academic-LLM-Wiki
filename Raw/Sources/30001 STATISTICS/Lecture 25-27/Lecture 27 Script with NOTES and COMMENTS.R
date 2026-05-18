### LECTURE 27 SCRIPT ###

#### MUSIC DOWNLOAD [SLIDES: 55-61]
# Regression using all the numerical variables
m0 = lm(Sales ~ Ads.Exp+Radio+Popularity, data = Downloads)
summary(m0) # good model!
# 66.66% of the variability of Sales is explained by the
# independent variables.
# The model is overall significant as the p-value
# for the overall significance is < 2.2e-16 (numerically zero)
confint(m0) # confidence interval for the model parameters

# Assumptions are respected!!!!
plot(m0,which=1) # linearity OK! and homoschedasticity OK!
rstd = rstandard(m0)
distr.plot.x(rstd,plot.type="histogram") # normality super OK!

# Relation between residuals and categorical vars
distr.plot.xy(x=International,y=rstd,
              plot.type="boxplot",data=Downloads)
distr.plot.xy(x=Genre,y=rstd,plot.type="boxplot",
              data=Downloads)

# If we detect association between the residuals and
# other variables then..... we let them join the model! :)
# <3
# (as they might explain the residual variability)

m1 = lm(Sales ~ Ads.Exp+Radio+Popularity+
          International+Genre, data = Downloads)
summary(m1) # The R^2-adjusted as improved! Happy times!
# we always prefer model with higher adj-R2 :)!

# Interpretation of InternationalYES:
# If all the other variables are fixed
# an INTERNATIONAL SONG has AVERAGE/EXPECTED sales 41.114589
# higher than a NON INTERNATIONAL SONG

# Interpretation of GenrePop:
# If all the other variables are fixed
# a POP SONG has AVERAGE/EXPECTED sales 47.852953 higher
# than a ROCK SONG (base category)

# Also e.g.:
# If all the other variables are fixed
# a POP SONG has AVERAGE/EFFECTED sales
# (47.852953-27.751379) higher than a ELECTRONIC SONG

# Predicting Sales corresponding to different amounts of ads expenses:
#   (500, 1000, 1500)
# for a pop international artist with popularity 60 who will likely
# be played on radio 55 times a week.
# Define the point in correspondence to which we make the prediction:
xg = data.frame(Ads.Exp=c(500,1000,1500),Radio=55,Popularity=60,
                    International="Yes",Genre="pop")
# Point prediction for this point:
predict(m1,xg)
# Provide a confidence interval for the expected sales of songs
# from artists with the characteristics defined above
# (pop international artists with popularity 60 who will likely
# be played on radio 55 times a week)
predict(m1,xg,interval = "confidence", level = 0.95)
# Provide a confidence interval for the sales of a specific song
# of a specific artist with such characteristics
predict(m1,xg,interval = "predict", level = 0.95)

### HOUSE PRICES [SLIDES 62-66]
m = lm(Price ~ Bedrooms+HSize+LSize, data = House) 
summary(m) 
# Here the model is SUPER SIGNIFICANT!
# but..
# 1) the individual variables are not significant
# WEIRD!
# 2) the coefficient of BEDROOMS is negative!
# (i.e. for each additional bedroom, all the other variables fixed,
# the expected price of a house GOES DOWN!)
# WEIRD!
# These features often happen in case of MULTICOLLINEARITY!
# MULTICOLLINEARITY IS HIGH LINEAR DEPENDENCE BETWEEN
# THE INDEPENDENT VARIABLES

# Relationships between independent and dependent variables
distr.plot.xy(x=Bedrooms,y=Price,plot.type="scatter",
              fitline=T,data=House)
distr.plot.xy(x=HSize,y=Price,plot.type="scatter",
              fitline=T,data=House)
distr.plot.xy(x=LSize,y=Price,plot.type="scatter",
              fitline=T,data=House)

# Correlations among all the variables (all numerical)
# in dataframe House
cor(House) # the correlations between independent variables are HIGH!

# (EASY) SOLUTION: Focus only on one out of the three variables:
m  = lm(Price ~ HSize, data = House) 
summary(m) # HIGHER adj-R^2!!! WOWOWOW!

### HOTEL
m = lm(Margin ~ Number+Nearest+Office+Enrollment+Income+Distance, 
              data = Hotel)
summary(m) 

# Check the assumptions
plot(m,which=1)
distr.plot.x(m$residuals,plot.type="histogram")

# extra-sample forecasts
xg = data.frame(Number = 3815,Nearest=0.9,
                         Office=476,Income=35,
                         Distance=11.2,Enrollment=24.5)

predict(m,xg,interval = "confidence",level = 0.95)
predict(m,xg,interval = "prediction",level = 0.95)

# in-sample prediction
conf.pred = predict(m, Hotel,interval = "confidence",level = 0.95)
pred.pred = predict(m, Hotel,interval = "prediction",level = 0.95)

# observation 87:
Hotel[87,]
conf.pred[87,]
pred.pred[87,]

# other observations:
Hotel[c(2,54,42,95),]
conf.pred[c(2,54,42,95),]
pred.pred[c(2,54,42,95),]