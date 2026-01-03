'''
Created on 03-Jan-2026

@author: Vivek
'''
import openpyxl

filename = r"C:\Users\admin\Documents\Ot11SP_DDT.xlsx"
my_workbook = openpyxl.load_workbook(filename)

active_sheet = my_workbook["Sheet1"] # loads the sheet by sheet name

cell_value = active_sheet.cell(2, 1).value
print(cell_value)




