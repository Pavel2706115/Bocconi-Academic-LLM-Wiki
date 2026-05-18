

# To avoid having to specify the Path,
# make sure that both files .py and .xlsx
# are saved in the same folder

import pandas


myDF = pandas.read_excel('Lesson20.xlsx', 'Invoices')

myDct = myDF.to_dict('list')


print("Filled dictionary:", myDct)



