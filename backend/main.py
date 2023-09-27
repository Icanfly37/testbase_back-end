from typing import Annotated, Union
from fastapi import FastAPI, UploadFile,File
from fastapi.responses import FileResponse
from pydantic import BaseModel
from Excel.ExcelEngine import *
from openpyxl import *
from io import *
from jsonengine import *
import os
from work import *

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

#senddata
@app.post("/test")
def read_root():
    return {0: {"Test": {"message": "Hello, World!"}}}

#stub/driver
@app.post("/test_send")
def read_root():
    send = OnJson(get_Current_Path("data.json"),"r")
    #jsoner = IsJson(get_Current_Path("data.json"))
    #jsoner.get_json_file("r")
    #send = jsoner.read_json_file()
    #jsoner.closefile("r")
    #print(send)
    return {"getjson": send}

#getdata
@app.post("/items/")
async def create_item(data: dict):
    print(data)
    #print(item.description)
    return {"message": "Data received and processed successfully"}

#getExcelFile
@app.post("/downloadfiles/")
async def create_file(file: Annotated[bytes, File()]):
    rows = OnExcel(file)
    #OnJson(get_Current_Path("/backend/data.json"),rows)
    #OnJson("data.json",rows)
    return {"rows":rows}

#sendExcelFile
@app.post("/uploadfile/")
def upload_file():
    excel_send = "D:/excel_test/ontester.xlsx"
    return FileResponse(excel_send, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
