
import nltk

MySentence = "In our society, owning programming skills is increasingly important. This applies not only to those working in the IT sector, but also to those working in fields such as science, art, education, and business management. Learning to program is indeed important not only because it allows to develop applications to support business activities, but above all because it allows to focus on the most effective approach to problem solving, combining technical aspects with logic and creativity.\nThis text aims to enable even those who have never approached programming before to write code in Python, starting from the fundamental elements of syntax and progressing to the understanding how to expand Python to adapt to specific studying or working needs. The text addresses key concepts such as data types, variables, conditional expressions, loops, custom functions, exception handling, classes and objects, the Standard Library modules and third-party modules."

MySList = nltk.tokenize.sent_tokenize(MySentence)
MyWList = nltk.tokenize.word_tokenize(MySentence)


for MyS in MySList:
    print(MyS + '\n')
    
print(MyWList)


