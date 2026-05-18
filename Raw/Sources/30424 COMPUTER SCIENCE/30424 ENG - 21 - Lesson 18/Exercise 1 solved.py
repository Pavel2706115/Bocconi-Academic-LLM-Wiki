

def create(num):
    output = dict()
    for x in range(1,num + 1):
        output[x] = (x / 2)**3
    return output



def show(MyDictionary):
    print("Key\tValue")
    for K in MyDictionary:
        print(str(K) + " \t" + str(MyDictionary[K]))







