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
    if len(id) == 1:
        sub_object_1={"S_ID" : "Subject_0"+id}
        sub_object_2={"C_ID" : "Course_0"+id}
    else:
        sub_object_1={"S_ID" : "Subject_"+id}
        sub_object_2={"C_ID" : "Course_"+id}
    for i in range(len(header)):
        #sub_object_1[header[i]] = slave[i]  
        if header[i] == "รหัสวิชา":
            if slave[i] is not None:
                if "-" in slave[i]:
                    target_year = slave[i].index("-")
                    catch_year = slave[i][target_year:][1:]
                    real_year = "25"+str(catch_year)
                    sub_object_1[header[i]] = slave[i][:target_year]
                    sub_object_1["ปีการศึกษา"] = real_year
                else:
                    sub_object_1[header[i]] = slave[i]
                    sub_object_1["ปีการศึกษา"] = None
            else:
                sub_object_1[header[i]] = slave[i]
                sub_object_1["ปีการศึกษา"] = None
        elif header[i] == "อาจารย์ผู้สอน":
            if slave[i] is not None:
                if "," in slave[i]:
                    staff = slave[i].split(",")
                elif "/" in slave[i]:
                    staff = slave[i].split("/")
                else:
                    staff = [slave[i]]
            else:
                staff = [slave[i]]
            sub_object_2["S_ID"] = sub_object_1["S_ID"]
            sub_object_2["P_ID"] = staff
        elif header[i] == "หมู่เรียน":
            if "," in slave[i]:
                sec = slave[i].split(",")
            elif "/" in slave[i]:
                sec = slave[i].split("/")
            else:
                sec = [slave[i]]
            for j in range(len(sec)): #O(2)
                if sec[j] == "บรรยาย":
                    sec[j] = "80x"
                elif sec[j] == "ปฏิบัติ":
                    sec[j] = "83x"
                else:
                    sec[j] = None
            sub_object_2["หมู่เรียน"] = sec
        elif header[i] == "ชั้นปี":
            if "," in slave[i]:
                year = slave[i].split(",")
            elif "/" in slave[i]:
                year = slave[i].split("/")
            else:
                year = [slave[i]]
            sub_object_2["ชั้นปีที่เปิดสอน"] = year
        elif header[i] == "วิชาพื้นฐาน":
            if slave[i] is not None:
                if "," in slave[i]:
                    pre = slave[i].split(",")
                elif "/" in slave[i]:
                    pre = slave[i].split("/")
                else:
                    pre = [slave[i]]
            else:
                pre = [slave[i]]
            sub_object_1[header[i]] = pre
        else:
            sub_object_1[header[i]] = slave[i]
        pack = [sub_object_1,sub_object_2]
    return pack