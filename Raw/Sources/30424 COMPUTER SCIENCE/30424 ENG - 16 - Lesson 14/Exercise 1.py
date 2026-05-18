num1 = int(input('Enter the first integer: '))
num2 = int(input('Enter the second integer (it should be higher than the first one): '))
sbor = num1 + num2
diff = num2 - num1
avg = sbor//2
if num1 == num2:
    print("You entered twice the same integer!")
elif num1 > num2:
    print("Second integer should be higher than the first one!")
else:
    print('The sum of the two ingers is: ',sbor, '\nThe difference of the two integers is: ',diff, '\nThe average of the two integers is: ',avg)
