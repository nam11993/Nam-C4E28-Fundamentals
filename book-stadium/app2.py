from xlrd import open_workbook

class Arm(object):
    def __init__(self, id, name, address, time, contact, description):
        self.id = id
        self.name = name
        self.address = address
        self.time = time
        self.contact = contact
        self.description = description

    def __str__(self):
        return("Arm object:\n"
               "  Arm_id = {0}\n"
               "  Name = {1}\n"
               "  Address = {2}\n"
               "  Time = {3}\n"
               "  Contact = {4} \n"
               "  Description = {5}"
               .format(self.id, self.name, self.address,
                       self.time, self.contact, self.description))

wb = open_workbook('data_sanbong.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []

    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        item = Arm(*values)
        items.append(item)

for item in items:
    print (item)
    print("Accessing one single value (eg. DSPName): {0}".format(item.name))
    print