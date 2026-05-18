from nltk.corpus import wordnet



def explain(MyWord):
    MySyn = wordnet.synsets(MyWord)
    i = 1
    for Syn in MySyn:
        print(str(i)+'.',Syn.definition())
        i = i+1
        



