
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

MyThought = 'We are all here to learn Python so to pass Computer science exam'
MyList = word_tokenize(MyThought.lower())
MyENstop = stopwords.words('english')
KW_List = []

for W in MyList:
    if W not in MyENstop:
        KW_List.append(W)

print(KW_List)
        
