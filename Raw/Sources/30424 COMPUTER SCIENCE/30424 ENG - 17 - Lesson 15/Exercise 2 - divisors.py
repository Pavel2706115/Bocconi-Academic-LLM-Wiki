ex = abs(int(input("Enter an integer: ")))

if ex == 0:
    print('Invalid number')

else:
    divisors = 0
    for i in range(1,ex+1):
        if ex%i==0:
            divisors = divisors +1
            print(i)
    
print("The nummber of divisors is", divisors)
