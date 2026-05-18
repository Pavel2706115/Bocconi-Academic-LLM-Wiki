
a = float(input('Insert first side length: '))
b = float(input('Insert second side length: '))
c = float(input('Insert third side length: '))

if a > 0 and b > 0 and c > 0 and \
   a < (b + c) and b < (a + c) and c < (a + b):
        
    if a == b == c :
        print("With these measures, it is an equilateral triangle")
    elif a != b and a != c and b != c :
        print("With these measures, it is a scalene triangle") 
    else :
        print("With these measures, it is an isosceles triangle")       

else :
    print("These measures cannot represent the sides of a triangle!")


