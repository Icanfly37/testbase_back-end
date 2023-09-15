from typing import Annotated, Union
from fastapi import FastAPI, UploadFile,File
from fastapi.responses import FileResponse
from ExcelEngine import *
from openpyxl import *
from io import *

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/test")
def read_root():
    return {0: {"Test": {"message": "Hello, World!"}}}

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    ExcelOP = Excel(file)
    check = ExcelOP.openfile()
    sheets = ExcelOP.allsheets()
    rows = ExcelOP.getrows()
    ExcelOP.closefile()
    print(sheets)
    print(rows)
    return {"allsheet":sheets,"rows":rows}

@app.post("/uploadfile/")
def upload_file():
    excel_send = "D:/excel_test/ontester.xlsx"
    return FileResponse(excel_send, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
