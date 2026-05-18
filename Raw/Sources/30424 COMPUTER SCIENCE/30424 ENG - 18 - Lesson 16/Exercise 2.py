def counter():
    total = 0
    try:    
        x = int(input('Enter a number: '))
        for i in range (1,x+1):
            if i%3==0 and i%7==0 and i%5 != 0:
                total = total + 1

        return total
    except ValueError:
        print('Wrong argument type')
