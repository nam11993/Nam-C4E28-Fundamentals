import xlrd

wb = xlrd.open_workbook("data_stadium.xlsx")
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(2, 1)) #row, #column ==> value of cell
print(sheet.row_values(1)) # value of row
print(sheet.nrows) # number of rows
print(sheet.ncols) # number of row

