

import openpyxl

_1stSemester = ('Economics', 'Mathematics', 'Accounting', 'History', 'Law')


MyFile = input('Which name do you want to give to your file? ')
MySheet = input('How do you want to name the existing worksheet? ')

MyWB = openpyxl.Workbook()
MyWB.active.title = MySheet

MyWB.active['A1'] = 'Course'
MyWB.active['B1'] = 'Score'

Row = 2

for MyCourse in _1stSemester:
    MyGrade = input('Insert the score of ' + MyCourse + ': ')
    MyWB.active['A'+str(Row)] = MyCourse
    MyWB.active['B'+str(Row)] = int(MyGrade)
    Row = Row + 1

MyWB.active['A'+str(Row+1)] = 'Average'
MyWB.active['B'+str(Row+1)] = '=AVERAGE(B2:B' + str(Row-1) +')'

MyWB.save(MyFile+'.xlsx')

print('\nThe creation of the file ' + MyFile + '.xlsx has been completed.\nThank you!')

