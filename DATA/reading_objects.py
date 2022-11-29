from LIBRARY.config import Config
import xlrd

def read_locators():
    workbook = xlrd.open_workbook(Config.DATA_Path)
    worksheet = workbook.sheet_by_name("data")
    rows = worksheet.get_rows()
    # columns = worksheet.ncols
    # rows= worksheet.get_rows()     #generator object
    print(rows)
    header=next(rows)
    d={}
    for row in rows:
        d[row[0].value] = (row[1].value, row[2].value)
    return d
# print(read_locators())

