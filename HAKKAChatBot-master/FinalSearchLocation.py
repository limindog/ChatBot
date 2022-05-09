from bs4 import BeautifulSoup
import json
import requests
data={"CourseName": "",
"CourseNo": "",
"CourseNotes": "",
"CourseTeacher": "",
"Dimension": "",
"ForeignLanguage": 0,
"Language": "zh",
"OnleyNTUST": 0,
"OnlyGeneral": 0,
"OnlyMaster": 0,
"Semester": "1081"}
headers = {'Content-Type': 'application/json'}
url="https://querycourse.ntust.edu.tw/QueryCourse/api/courses"
def SearchLocation(Query):
    returnText=""
    data["CourseName"]=Query
    r=requests.post(url,data=json.dumps(data),headers=headers)
    result=json.loads(r.text)
    if len(result)<1:
        return "沒找到相關關鍵字 484打錯ㄌ"
    for i in result:
        if i["CourseNo"][0]=="3":
            continue
        returnText+=str(i["CourseName"])+" "+str(i["CourseTeacher"])+" "+str(i["Node"])+" "+str(i["ClassRoomNo"])+"\n\n"

    return returnText
