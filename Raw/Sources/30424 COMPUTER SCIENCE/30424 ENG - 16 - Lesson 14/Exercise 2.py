a = float(input("Enter the first number, corresponding to the first side of a triangle: "))
b = float(input("Enter the second number, corresponding to the second side of a triangle: "))
c = float(input("Enter the third number, corresponding to the third side of a triangle: "))
sum1 = a+b
sum2 = a+c
sum3 = b+c

if a>0 and b>0 and c>0 and a<sum3 and b<sum2 and c<sum1:
    if a==b and b==c:
        print("With these measures, it is an equilateral triangle")
    elif a != b and b!=c:
        print("With these measures, it is a scalene triangle")
    else:
        print("With these measures, it is an isosceles triagnle")

else:
    print("These measures cannot represent the sides of a triangle!")
