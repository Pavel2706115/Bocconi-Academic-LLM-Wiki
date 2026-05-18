import webbrowser

MyQuery = ''
MyKW = input('Type the keyword you want to search: ')

while MyKW != '':
    MyQuery = MyQuery + MyKW + '+'
    MyKW = input('Do you want to enter another keyword?\n\
    (Type the new keyword or hit Enter key to launch the search): ')

webbrowser.open('https://www.google.com/search?q='+MyQuery)
