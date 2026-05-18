def FirstLast(s):
    '''You should write a sentence for an argument of the function.'''
    myfirst = s[0]
    mylast = s[-1]
    p = "First character: " + myfirst.upper() + ", last character: " + mylast.upper()
    return p

def FirstLast2(s,ind1=0,ind2=1):
    '''You should write a sentence for an argument of the function.'''
    cut = s[ind1:ind2+1]
    
    p = "Cut part is:" + cut.upper()
    return p

def FirstLast3(s):
    '''You should write a sentence for an argument of the function.'''
    mylist = s.split()
    myfirst = mylist[0]
    mylast = mylist[-1]
    
    p = "First word is " + myfirst.upper() + " Last word is " + mylast.upper()
    return p
