from openpyxl import *
from io import *
from rows_and_cols import *

#excel = load_workbook(BytesIO(file))

class Excel():
    def __init__(self,path): # path are bytes not directory names
        self.path = BytesIO(path)
        self.error = 0
        self.rows = {}
        self.cols = {}
    def openfile(self):
        try:
            self.excel = load_workbook(self.path)
            return self.error
        except FileNotFoundError:
            return self.error
    def allsheets(self):
        return self.excel.sheetnames
    def getrows(self):
        sheet = self.excel[self.excel.sheetnames[0]]
        num_rows = sheet.max_row
        num_cols = sheet.max_column
        for i in range(1,num_rows+1):
            self.rows.update({"row "+str(i):each_row(sheet,i,num_rows,num_cols)})
        return self.rows
    def getcolumns(self):
        sheet = self.excel[self.excel.sheetnames[0]]
        num_rows = sheet.max_row
        num_cols = sheet.max_column
        for i in range(1, num_cols+1):
            self.cols.update({"col"+str(i):each_column(sheet,i,num_cols,num_rows)})
        return self.cols
    def closefile(self):
        self.excel.close()
        
#excel = load_workbook(BytesIO(file))