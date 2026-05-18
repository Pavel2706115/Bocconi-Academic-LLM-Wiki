print("Let's play the game 'Guess the number'!")
print('Please, think of a number between 0 and 255')
input("(then hit ENTER when you are ready to start)\n...\n")

for x in range(256):
    a = input('Is ' + str(x) + ' your number?\nenter "Yes" if it is correct, "No" otherwise:\n>>> ')
    if a.upper() in ['YES', 'Y']:
        break
        
print('Great! Your number is', x, 'and it took me', x+1, 'attempts to guess it!')
