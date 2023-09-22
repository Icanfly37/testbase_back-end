from Excel.ExcelEngine import *
from jsonengine import *
import os

def get_Current_Path(file_target):
    current_directory = os.getcwd()
    port_path = current_directory.replace("\\", "/")
    real_path = port_path+file_target
    #real_path = file_path.replace("\\", "/")
    return real_path

def OnJson(path,target):
    jsoner = IsJson(path)
    jsoner.get_json_file("w")
    jsoner.write_json_file(target)
    jsoner.closefile("w")

def OnExcel(file):
    ExcelOP = Excel(file)
    ExcelOP.openfile()
    rows = ExcelOP.getrows() #for input to database from excel
    ExcelOP.closefile()
    OnJson(get_Current_Path("data.json"),rows)
    return rows