### CALLCENTER APPLICATION ###
# Univariate Analysis
distr.table.x(x=Reason,freq=c("counts","prop"),data=CallCenter)
distr.table.x(x=Satisf,freq=c("counts","prop"),data=CallCenter)

# Turn Satisf into a Factor
CallCenter$Satisf.F = factor(CallCenter$Satisf,
                            levels=c("Not at all","Slightly","Moderately",
                                     "Very","Completely"))
distr.table.x(x=Satisf.F,freq=c("counts","prop","cum"),data=CallCenter)

# Cross table
distr.table.xy(x=Reason,y=Satisf.F, freq=c("counts","prop"), 
               freq.type="joint",f.digits=3,data=CallCenter)
distr.plot.xy(x=Reason,y=Satisf.F, freq="prop", freq.type="joint",
              plot.type="bars", 
              color=c("red","orange","yellow","green","darkgreen"),
              data=CallCenter)

# Conditional frequency of: Satisf.F (y) | Reason (x) 
distr.table.xy(x=Reason,y=Satisf.F, freq="prop", freq.type="y|x",
               data=CallCenter)
distr.plot.xy(x=Reason,y=Satisf.F, freq="prop", freq.type="y|x",
              plot.type="bars", 
              color=c("red","orange","yellow","green","darkgreen"),
              data=CallCenter)