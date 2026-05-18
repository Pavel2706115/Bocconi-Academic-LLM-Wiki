### LECTURE 10 SCRIPT ###
# FOR THIS LECTURE REFER TO THE SLIDES!
# ALL THE DATA EXPLORATION IS VERY EXHAUSTIVELY EXPLAINED THERE! :)

### CASE 3 ### (confounding variable)
head(Ability_Performance) # dataset
# Manager: rating of the consultant given by the manager
# Performance: rating based on the time it took to complete the last task
# (the shorter the time, the better the performance) 
# QUESTION: are manager's rating reliable?
distr.plot.xy(Manager,Performance,plot.type="scatter",
              data = Ability_Performance, fitline=TRUE)
# there is a negative linear association WEIRD!
cor(Ability_Performance$Manager,
    Ability_Performance$Performance)
# POSSIBLE EXPLANATION: there is a CONFOUNDING
# VARIABLE. A possible example is DIFFICULTY OF THE TASKS
# the consultant is asked to perform.
# The higher the manager score, the more
# difficult tasks the consultant is given.
# The more difficult the task, the longer
# it takes to carry over it.

### CASE 4 ### (absolute and relative metrics)
head(Burglary.US) # dataset
# County: some US counties
# Burglary_Arrest: the number of arrests for burglary
# Employed and Unemployed: number of Employed and Unemployed people
# QUESTION: is there an association between employment and burglary?
distr.plot.xy(x=Employed,y=Burglary_Arrests,
              plot.type = "scatter",
              fitline = TRUE,
              data=Burglary.US)
cor(Burglary.US$Employed,Burglary.US$Burglary_Arrests)
# The correlation seems positive, but there's an outlier
# that might be very impactful! We remove it:
Burglary.Reg = Burglary.US[Burglary.US$Employed<2000000,]
distr.plot.xy(x=Employed,y=Burglary_Arrests,
              plot.type = "scatter",
              fitline = TRUE,
              data=Burglary.Reg)
cor(Burglary.Reg$Employed,Burglary.Reg$Burglary_Arrests)
# The relationship is positive...
# ...but...
# WAIT!
# Of course in a state with higher population, we will have more
# Employed and more Arrests! It's just because there's more people in the state!
# So let's look instead at relative measures!
# we divide the two variables by the total population of the corresponding state
Burglary.US$Pop = Burglary.US$Unemployed+Burglary.US$Employed
Burglary.US$Burglary_Pop = Burglary.US$Burglary_Arrests/Burglary.US$Pop
Burglary.US$Employed_Pop = Burglary.US$Employed/Burglary.US$Pop
distr.plot.xy(x=Employed_Pop,y=Burglary_Pop,plot.type = "scatter",
              fitline = TRUE,data=Burglary.US)
cor(Burglary.US$Employed_Pop,Burglary.US$Burglary_Pop)
# The higher the percentage/rate of employed population,
# the lower the rate of Arrests for Burglary!
# Now it makes sense!
# See Slides :)

### CASE 5 ### (causation, confounding variables)
head(Police_Crime) # dataset
# State: US State
# Region: ...
# Police: per capita expenditures on police personnel
# Assault, Rape, Murder, ViolentCrime: reported violent crimes,
# related to population
# UrbanPop: level of urbanization (%)
# QUESTION: is there an association between police expenditure
# and number of crimes?
distr.plot.xy(Police,Assault,plot.type = "scatter",
              data = Police_Crime,fitline=TRUE)
cor(Police_Crime$Police,
    Police_Crime$Assault,use = "complete.obs")
# Explanation 1: maybe there is a causal relationship
# but in reverse!
# The higher the crimes, the more the police
# expenditure is increased.
# Explanation 2: UrbanPop is a confounding variable
distr.plot.xy(UrbanPop,Police,plot.type = "scatter",
              data = Police_Crime,fitline=TRUE)
cor(Police_Crime$UrbanPop,
    Police_Crime$Police,use = "complete.obs")
distr.plot.xy(UrbanPop,Assault,plot.type = "scatter",
              data = Police_Crime,fitline=TRUE)
cor(Police_Crime$UrbanPop,
    Police_Crime$Assault,use = "complete.obs")
distr.plot.xy(Region,UrbanPop,plot.type = "box",
              data = Police_Crime)

### CASE 7 ### (confounding variables)
head(Managers_Salary) # dataset
# Salary: in US dollars
# Gender: gender
# Education: education level
# Experience: years of work experience
# QUESTION: is the equal pay for equal work policy respected by the company
# with respect to gender in particular?
distr.plot.xy(Gender,Salary,plot.type = "box",
              data = Managers_Salary)
# there is association between gender and salary
# POSSIBILITY 1: confounding variable is experience
distr.plot.xy(Experience,Salary,plot.type = "scatter",
              data = Managers_Salary)
distr.plot.xy(Gender,Experience,plot.type = "box",
              data = Managers_Salary)
distr.plot.xy(Experience,Salary,plot.type = "scatter",
              data = Managers_Salary,var.c=Gender)
# this is plausible!

# POSSIBILITY 2: confounding variable is education
Managers_Salary$Education = factor(Managers_Salary$Education,
 levels = c("College","Bachelor","Graduate","Post-Graduate"))
distr.plot.xy(Gender,Education,plot.type = "bars",
              freq.type = "y|x",data = Managers_Salary)
distr.plot.xy(Education,Salary,plot.type = "box",
              data = Managers_Salary)
# there does not seem to be a VERY STRONG association
# between education and salary
# hence it cannot be a confounding variable.