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



class Student(Person):

    def __init__(self, IDnum, nat, FirstName="", LastName=""):
        Person.__init__(self, nat, FirstName, LastName)
        self.ID_number = IDnum

    def __str__(self):
        t = (self.name + " " +
             self.surname + " - " +
             "student ID " +
             self.ID_number)
        return t

    def welcome(self):
        w = ("Hello, my name is " +
             self.name)
        return w




# The following lines can also be entered one by one, directly in the Shell 
        
MySister = Person('english', 'Mary', 'White')
MySister.height = 183
MySister.weight = 70.6
print(MySister)


MyCousin = Person('french', 'Juliette', 'Marmorat')
MyCousin.height = 172
MyCousin.weight = 56.1
print(MyCousin)


MyFriend = Person('mexican', 'Juan Esteban', 'Gonzales')
MyFriend.height = 169
MyFriend.weight = 71.4
print(MyFriend)



MyClassMate = Student('123456', 'italian', 'Mario', 'Rossi')
MyClassMate.height = 169
MyClassMate.weight = 71.4
print(MyClassMate)
print("The Body Mass Index of", MyClassMate.name, "is", format(MyClassMate.BMI(), ".1f"))
print(MyClassMate.welcome())


