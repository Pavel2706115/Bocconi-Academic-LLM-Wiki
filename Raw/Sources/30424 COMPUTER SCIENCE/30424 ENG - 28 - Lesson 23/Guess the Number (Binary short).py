n = int(input("Let's play the game 'Guess the number'!\n\
How many attempts do you give me to guess the number? "))
print('Ok, now think of a number between 0 and', (2**n)-1)
input("(then hit ENTER when you are ready to start)\n...\n")

x = 0

for i in range(n-1, -1, -1):
    x = x + 2**i
    a = input('Is ' + str(x) + ' your number?\nenter "Yes" if it is correct\nenter "L" if ' + str(x) + ' is too Low\nenter "H" if ' + str(x) + ' is too High:\n>>> ')
    if a.upper() in ['YES', 'Y']:
        break
    elif a.upper() == 'H':
        x = x - 2**i
        
print('Great! Your number is', x, 'and it took me', n-i, 'attempts to guess it!')
