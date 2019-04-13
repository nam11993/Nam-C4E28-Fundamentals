from xlrd import open_workbook

wb = open_workbook('data_stadium.xlsx')
for s in wb.sheets():
    #print 'Sheet:',s.name
    values = []
    for row in range(s.nrows):
        col_value = []
        for col in range(s.ncols):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append(value)
        values.append(col_value)
# print (values)

data = {}
# a = values[0]
# b = values[1]
# for j in b:
#     for i in a:
#         data[(i)] = (j)
#         print(data)
# # print(b)

for a in values:
    for i in a:
        