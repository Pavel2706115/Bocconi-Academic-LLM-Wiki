
# To avoid having to specify the Path,
# make sure that all the files used (.py, .xlsx, .txt)
# are all saved in the same folder


filename = 'Lesson20.txt'

myfile = open(filename, 'r')

stringRows = myfile.readlines()

KeysList = stringRows[0].split('\t')

col_num = len(KeysList)

myDct = {}
for i in range(col_num):
    myKey = KeysList[i]
    myDct[myKey] = []


mainlist = []
for i in range(col_num):
    mainlist.append([])

for row in stringRows[1:]:   
    singleValues = row.split('\t')
    index = 0
    for valueslist in mainlist:
        valueslist.append(singleValues[index])
        index = index + 1

index = 0
for k in myDct.keys():
    myDct[k] = mainlist[index]
    index = index + 1


print("Filled dictionary:", myDct)





