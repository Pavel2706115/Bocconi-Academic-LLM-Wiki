


class Person():
    
    def __init__(self, nat, FirstName="", LastName=""):
        self.name = FirstName
        self.surname = LastName
        self.nationality = nat
        self.height = 0
        self.weight = 0.0
        
    def BMI(self):
        bmi_value = self.weight / (self.height/100)**2
        return bmi_value

    def __str__(self):
        t = (self.name + " " +
             self.surname + " (" +
             str(self.height) + " cm, " +
             str(self.weight) +
             " kg, has a Body Mass Index of " +
             str(round(self.BMI(), 1)) + ')') 
        return t
