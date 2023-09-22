from Excel.ExcelEngine import *
from jsonengine import *
import os
from database.DB_Engine import *
from io import *

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
    
def OnDB_C(cred,collection_name,target):
    db = Database(cred)
    db.get_db()
    db.get_collection(collection_name)
    id = 1
    for i in target:
        db.create_doc(i,str(id))
        id += 1
    db.close_db()
    

def OnExcel(file,db_collection=None):
    ExcelOP = Excel(BytesIO(file))
    #ExcelOP = Excel(file)
    ExcelOP.openfile()
    rows = ExcelOP.getrows() #for input to database from excel
    OnJson("data.json",rows)
    ExcelOP.closefile()
    if db_collection is not None:
        OnDB_C("D:/testbase_back-end/backend/database/serviceAccountKey.json",db_collection,rows)
    return rows

# path = "C:/Users/icanfly37/Desktop/excel_tester/หลักสูตร.xlsx"
# print(OnExcel(path))