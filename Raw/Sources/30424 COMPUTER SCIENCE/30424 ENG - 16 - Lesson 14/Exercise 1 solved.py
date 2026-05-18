num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number higher than the first one: "))

if num1 == num2:
    print("Please, enter two different numbers!")
elif num1 < num2:
    print("The sum is:", num1+num2)
    print("The difference is:", num2-num1)
    print("The average is:", (num1+num2)/2)
else:
    print("The second number must be higher than the first one!")
    
