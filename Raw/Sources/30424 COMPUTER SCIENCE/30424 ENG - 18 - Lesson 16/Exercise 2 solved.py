


def divisors(num):
    div = 0
    for n in range(1, num+1):        
        if n % 3 == 0 and n % 7 == 0 and not n % 5 == 0:
            div = div + 1
    return div




# Function with errors handled with try...except
def divisors2(num):
    div = 0
    try:
        for n in range(1, num+1):        
            if n % 3 == 0 and n % 7 == 0 and not n % 5 == 0:
                div = div + 1
        return div
    except:
        return 'Wrong argument type'



# Function with errors handled with if-else
def divisors3(num):
    div = 0
    if type(num) == str or type(num) == float:
        return 'Wrong argument type'
    else:
        for n in range(1, num+1):        
            if n % 3 == 0 and n % 7 == 0 and not n % 5 == 0:
                div = div + 1
        return div


