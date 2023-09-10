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

@app.get("/test")
def read_root(name):
    return {"message": str(name)}

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
    #excel = load_workbook(BytesIO(file))
    
    #return {"Testfile":excel.sheetnames}
    #return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
