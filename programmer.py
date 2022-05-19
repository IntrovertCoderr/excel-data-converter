# Reading an excel file using Python
import xlrd
# importing for regular expression
import re

# Give the location of the file
loc = ("../Programmer report.xls")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

arr =[]
# For row 0 and column 0
for x in range(0,160):
    arr.append((sheet.cell_value(x, 5)))

print (arr)


