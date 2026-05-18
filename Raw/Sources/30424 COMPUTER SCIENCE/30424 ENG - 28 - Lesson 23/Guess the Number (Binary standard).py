n = int(input("Let's play the game 'Guess the number'!\n\
How many attempts do you want me to guess the number? "))
print('Ok, now think of a number between 0 and', (2**n)-1)
input("(then hit ENTER when you are ready to start)\n...")

x = 0

for i in range(n-1, -1, -1):
    x = x + 2**i
    a = input('Is the number less than ' + str(x) + '? (Yes/No): ')
    if a.lower() in ['yes', 'y']:
        x = x - 2**i
        
print('Your number is:', x)
