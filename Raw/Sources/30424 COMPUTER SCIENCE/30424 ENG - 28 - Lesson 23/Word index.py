
import time



def position_index(MyWord):

    WordsSet = open('MyWords.txt')
    MyList = WordsSet.readlines()
    for i in range(len(MyList)):
        MyList[i] = MyList[i][:-1]
    
    start_time = time.perf_counter()
    
#############################################
    index = MyList.index(MyWord)
#############################################

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(' '+str(index)+'\t|', format((elapsed_time)*1000, '.9f')+'\t| .index method of lists')





def position_trav(MyWord):

    WordsSet = open('MyWords.txt')
    MyList = WordsSet.readlines()
    for i in range(len(MyList)):
        MyList[i] = MyList[i][:-1]
    
    start_time = time.perf_counter()
    
#############################################
    for word in MyList:
        if word == MyWord:
            index = MyList.index(MyWord)
#############################################

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(' '+str(index)+'\t|', format((elapsed_time)*1000, '.9f')+'\t| Traversing elements in a list')





def position_indexing_for(MyWord):

    WordsSet = open('MyWords.txt')
    MyList = WordsSet.readlines()
    for i in range(len(MyList)):
        MyList[i] = MyList[i][:-1]
    
    start_time = time.perf_counter()

#############################################
    for i in range(len(MyList)):
        if MyList[i] == MyWord:
            index = i
#############################################

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(' '+str(index)+'\t|', format((elapsed_time)*1000, '.9f')+'\t| Indexing with a "for" loop')





def position_indexing_while(MyWord):

    WordsSet = open('MyWords.txt')
    MyList = WordsSet.readlines()
    for i in range(len(MyList)):
        MyList[i] = MyList[i][:-1]
    
    start_time = time.perf_counter()

#############################################
    i = 0
    while i <= (len(MyList)-1):
        if MyList[i] == MyWord:
            index = i
            break
        i = i + 1
#############################################

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(' '+str(i)+'\t|', format((elapsed_time)*1000, '.9f')+'\t| Indexing with a "while" loop')


    


def position_binary(MyWord):

    WordsSet = open('MyWords.txt')
    MyList = WordsSet.readlines()
    for i in range(len(MyList)):
        MyList[i] = MyList[i][:-1]
    
    start_time = time.perf_counter()

#############################################
    pos_min = 0
    pos_max = len(MyList)-1
    i = 0

    while MyList[i] != MyWord:
        i = (pos_max + pos_min)//2
        if MyList[i] == MyWord:
            break
        elif MyList[i] > MyWord:
            pos_max = i
        elif MyList[i] < MyWord:
            pos_min = i+1
#############################################

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(' '+str(i)+'\t|', format((elapsed_time)*1000, '.9f')+'\t| Binary search')






def test():

    MyTest = input('Enter the word of which you want to know the position: ')

    print('-'*60)
    print(' index\t| milliseconds\t| Approach used')
    print('-'*60)

    try:
        position_index(MyTest)
        position_trav(MyTest)
        position_indexing_for(MyTest)
        position_indexing_while(MyTest)
        position_binary(MyTest)

    except:
        print(">>>   Sorry! I don't know '"+MyTest+"'   <<<")

    print('-'*60)
