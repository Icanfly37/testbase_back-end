from openpyxl.cell import MergedCell
from openpyxl import *

def each_column(sheet,col_target,max_col,max_row):
    box = []
    for i in range(1,max_row+1):
        a = sheet.cell(row = i, column =col_target)
        if not isinstance(a,MergedCell):
            if col_target <= max_col:
                if isinstance(a.value,str):
                    a.value.replace("\t","")
                    box.append(a.value)
                else:
                    box.append(a.value)
    return box
    
def each_row(sheet,row_target,max_rows,max_col):
    box = []
    for i in range(1,max_col+1):
        a = sheet.cell(row = row_target, column = i)
        if not isinstance(a,MergedCell):
            if row_target <= max_rows:
                if isinstance(a.value,str):
                    a.value.replace("\t","")
                    box.append(a.value)
                else:
                    box.append(a.value)
    return box

def sub_object_send(id,header,slave):
    sub_object={}
    for i in range(len(header)):
            sub_object[header[i]] = slave[i]
    return sub_object