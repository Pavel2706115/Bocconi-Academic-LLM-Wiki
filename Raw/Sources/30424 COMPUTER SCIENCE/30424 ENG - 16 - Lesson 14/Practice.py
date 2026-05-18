#Double alternative decision-making structure
'''
x = input('Enter the password: ')
if x == '5ecure':
    print('Password accepted.')
else:
    print('Sorry, the password is wrong.')
'''

#Chained conditionals
'''
x = int(input('Enter the value of x: '))
if x > 0:
    print('x is positive')
else:
    if x < 0:
        print ('x is negative')
    else:
        print ('x is 0')

x = int(input('How tall are you (in cm)? '))
y = int(input('How tall is the person on your right (in cm)? '))
if x > y:
    print('You are taller than the person on your right!')
else:
    if x<y:
        print('You are shorter than the person on your right!')
    else:
        print('What a coincidence: you are tall exactly like the person on your right!')
'''

#The el-if statement
'''
#First variant:
x = int(input('Test score: '))
if 91<x<100:
    print('The grade is A')
elif 81<x<91:
    print('The grade is B')
elif 71<x<81:
    print('The grade is C')
elif 61<x<71:
    print('The grade is D')
else:
    print('The grade is F')

#Second variant:
score = int(input('Enter the score: '))
if score >= 91:
    grade = 'A'
elif score >= 81:
    grade = 'B'
elif score >= 71:
    grade = 'C'
elif score >= 61:
    grade = 'D'
else:
    grade = 'F'

print('The grade is', grade)
'''
