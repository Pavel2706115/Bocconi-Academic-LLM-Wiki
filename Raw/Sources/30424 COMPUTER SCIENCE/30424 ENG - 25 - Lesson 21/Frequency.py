import nltk

MySample = "Coding with Python in 2025 at Bocconi is awesome! Let's do it together!"
MySentence = "In our society, owning programming skills is increasingly important. This applies not only to those working in the IT sector, but also to those working in fields such as science, art, education, and business management. Learning to program is indeed important not only because it allows to develop applications to support business activities, but above all because it allows to focus on the most effective approach to problem solving, combining technical aspects with logic and creativity.\nThis text aims to enable even those who have never approached programming before to write code in Python, starting from the fundamental elements of syntax and progressing to the understanding how to expand Python to adapt to specific studying or working needs. The text addresses key concepts such as data types, variables, conditional expressions, loops, custom functions, exception handling, classes and objects, the Standard Library modules and third-party modules."



def PrintDict(MyDictionary):
    print('\n'+'-'*20)
    print('Item\tFreq.'.expandtabs(15))
    print('-'*20)
    for k,v in MyDictionary.items():
        Output = str(k)+'\t'+str(v)
        print(Output.expandtabs(15))

'''NOTE: in the funtion 'PrintDict(MyDictionary)'
   the string method '.expandtabs(value)' is used
   to define a custom size of the Tabulation (that
   by default is 8 positions, and here is 15) '''





def CharFreq01(MySentence):
    MySortLowSen = sorted(MySentence.lower())
    OutDict = {}
    for c in MySortLowSen:
        OutDict[c] = MySortLowSen.count(c)
    return OutDict





def CharFreq02(MySentence):
    MySortLowSen = sorted(MySentence.lower())

###---------- To complete ----------###






def WordFreq01(MySentence):
    MyLowSen = MySentence.lower()
    MyWords = MyLowSen.split()
    MyWords.sort()

###---------- To complete ----------###






def WordFreq02(MySentence):
    MyLowSen = MySentence.lower()
    MyWords = MyLowSen.split()
    MyWords.sort()
    return nltk.FreqDist(MyWords)





### --- Functions calls --- ###

PrintDict(CharFreq01(MySample))

PrintDict(WordFreq02(MySentence))





### --- EXTRA --- ###

def MostFreq(MySen):
    for k,v in WordFreq02(MySen).items():
        if v == max(WordFreq02(MySen).values()):
            print('The most frequent word is "'+k+'" which is present', v, 'times')

MostFreq(MySentence)
