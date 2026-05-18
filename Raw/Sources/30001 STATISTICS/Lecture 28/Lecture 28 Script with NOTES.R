# Lecture 28 Script
# (CHECK SLIDES FOR THE FINAL PLOTS)
# scatterplot of happiness against weekly hours of work
# coloured by sex variable
distr.plot.xy(weekly_h,happiness,data = happy,
              var.c = sex,
              plot.type = "scatter",fitline = TRUE)
# not linear relationship for sure!
# Nonetheless we try and fit a model and see what happens
m1 = lm(happiness ~ weekly_h, data = happy)
summary(m1)
# comments?
m2 = lm(happiness ~ weekly_h+sex, data = happy)
summary(m2)
# comments?

# QUADRATIC MODEL
# It is possible to include as independent variable
# a transformation of any of the independent variables!
# In particular here we add to the model:
# weelky_h2 = (weelky_h)^2
# The resulting model is called QUADRATIC because
# it includes a QUADRATIC TERM.
# The resulting regression function is not linear anymore,
# it is a quadratic function!
happy$weekly_h2 = happy$weekly_h^2
mquadratic = lm(happiness ~ weekly_h+weekly_h2+sex,
                data = happy)
summary(mquadratic)
# comments?
