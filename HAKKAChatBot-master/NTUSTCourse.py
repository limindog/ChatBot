#%%
import requests
import json
import re
import time
import random
from bs4 import BeautifulSoup

url="https://querycourse.ntust.edu.tw/QueryCourse/api/courses"
commondata={"CourseName": "",
"CourseNo": "",
"CourseNotes": "",
"CourseTeacher": "",
"Dimension": "",
"ForeignLanguage": 0,
"Language": "zh",
"OnleyNTUST": 0,
"OnlyGeneral": 1,
"OnlyMaster": 0,
"Semester": "1081"}
engdata={"CourseName": "",
"CourseNo": "",
"CourseNotes": "",
"CourseTeacher": "",
"Dimension": "",
"ForeignLanguage": 1,
"Language": "zh",
"OnleyNTUST": 0,
"OnlyGeneral": 0,
"OnlyMaster": 0,
"Semester": "1081"}
headers = {'Content-Type': 'application/json'}

def SearchCommon():
    time.sleep(1)
    ContentCourse=""
    r=requests.post(url,data=json.dumps(commondata),headers=headers)
    result=json.loads(r.text)
    
    
    for i in result:
            
            #QuickSearchCourseLocation[i['CourseNo']]=[i["CourseName"],i["Node"]]
            com=re.compile("[0-9]+")
            num=com.findall(i["Contents"])
            try:
                if int(num[0])>int(i["AllStudent"]):
                #i["CourseNo"],i["CourseName"],i["CourseTeacher"],i["Node"],i["AllStudent"],num[0]))
                    ContentCourse+=i["CourseNo"]+" "+i["CourseName"]+" "+i["Node"]+" 缺額:"+str(int(num[0])-int(i['ChooseStudent']))+"\n"
            except:
                pass
            
    r.close()
    return ContentCourse
def SearchEnglish():
    time.sleep(1)
    ContentCourse=""
    r=requests.post(url,data=json.dumps(engdata),headers=headers)
    result=json.loads(r.text)
    for i in result:
           #QuickSearchCourseLocation[i['CourseNo']]=[i["CourseName"],i["Node"]]
            com=re.compile("[0-9]+")
            num=com.findall(i["Contents"])
            if int(num[0])>int(i["AllStudent"]):
            #i["CourseNo"],i["CourseName"],i["CourseTeacher"],i["Node"],i["AllStudent"],num[0]))
                ContentCourse+=i["CourseNo"]+" "+i["CourseName"]+" "+i["Node"]+" 缺額:"+str(int(num[0])-int(i['ChooseStudent']))+"\n"
    r.close()
    return ContentCourse

def SearchBeauty():
    index=random.randint(1500,3031)
    url="https://www.ptt.cc/bbs/Beauty/index"+str(index)+".html"
    r=requests.get(url,cookies={'over18': '1'})
    bs=BeautifulSoup(r.text,"html.parser")
    final="看推的比較好><\n"
    href=""
    for ArticalDiv in bs.find_all("div",class_="r-ent"):
        href=ArticalDiv.find("a")
        result=str(href)
        if result !="None":
            if "公告" in href.text:
                continue
            num=ArticalDiv.find("span")
            try:
                if num["class"][1]=="f1" or num["class"][1]=="f3":
                    final+="推"+num.text+" "+href.text+"\n https://www.ptt.cc"+result[9:44]+"\n"
                else:
                    final+="噓"+num.text+" "+href.text+"\n https://www.ptt.cc"+result[9:44]+"\n"
            except:
                final+="0 "+href.text+"\n https://www.ptt.cc"+result[9:44]+"\n"
        
    r.close()
    return final
def CourseContent(CourseNum):
    time.sleep(1)
    url="https://querycourse.ntust.edu.tw/QueryCourse/api/coursedetials?semester=1081&course_no="+str(CourseNum)
    r=requests.get(url)
    result=json.loads(r.text)
    content=result[0]
    r.close()
    for i in content:
        if not isinstance(content[i],str):
            content[i]=str(content[i])
    content["CoreAbility"]=content["CoreAbility"].replace("■","")
    returnText="學期: "+content["Semester"]+"\n課程代號: "+content["CourseNo"]+"\n課程名稱: "+content["CourseName"]+"\n授課老師: "+content["CourseTeacher"]+"\n學分數: "+content["CreditPoint"]+"  必/選修: "
    returnText+=content["RequireOption"]+"  學年:"+content["AllYear"]+"\n先修課程:"+content["PreCourse"]+"\n教室位置:"+content["ClassRoomNo"]+"\n\n核心能力: "
    returnText+=content["CoreAbility"]+"\n課程內容: "+content["CourseContent"]+"\n\n教科書: "+content["CourseTextbook"]+"\n\n參考書目: "+content["CourseRefbook"]+"\n\n修課學生須知: "
    returnText+=content["CourseNote"]+"\n\n評分方式:"+content["CourseGrading"]+"\n\n備註: "+content["CourseRemark"]
    return returnText

def programmerStory():
    return """身為一名客家人，阿嬤帶給我的勤儉，我永遠不會忘記，
「乖孫，客家人不能喝溫水哦，因為小氣鬼只能喝涼水，要記得喔。」
，身為客家人的阿嬤勤儉是她唯一願意給我的東西。
-
還記得高中讀書時，一條菜脯一碗稀飯，這就是我的早餐，但貪心的我，常常多夾一條。
：「李俊賢你在周馬該啊（李俊賢你在衝三小），這樣晚餐沒東西吃耶。」
看向阿嬤手上的碗，半條菜脯還浮在稀的像水的飯上，我還不解阿嬤的作為。 
：「阿嬤，妳怎麼還留著半條菜脯，是吃不下嗎？」
：「掉ㄋㄧㄚˇ梅（幹你娘），阿嬤是要留到晚餐啦。」 
驚訝、頓悟、羞恥，各種情緒湧上心頭，原來阿嬤的客家精神，已經貫徹到這種地步，
至於為什麼是留到晚餐，因為客家人根本沒有午餐觀念，太浪費錢了，阿嬤的堅持，
讓我感到十足的羞恥，曾幾何時，我遺忘了自己身為客家人的驕傲，竟然敢把早餐吃完，羞愧的我，主動跪下請阿嬤原諒我。
：「李俊賢你給我站起來，男人膝下有黃金，萬一跪碎了，以後怎麼花？罰你喝溫水三杯。」 
：「阿嬤不要啦，你怎麼罰我都可以，就是不要溫水，我會考上台科大，拜託不要讓我喝溫水。」 
：「好，你最好做到，不然就讓你看看我的客家本色。」阿嬤拿起手中的藤條，揮了兩下，跟鄰居阿梅的掃把很像，應該是昨天幹來的。
-
聽完阿嬤的最後忠告，我拿起水壺，接下我慌張的眼淚，奪門而出，展開我的贖罪之旅-統測。 
「唐山過台灣，沒半點錢...」，熟悉的旋律重複在手機中，畢竟為了省手機空間，我的手機只有這首音樂，讀書累了就打開＂客家本色＂來警醒自己，
兢兢業業、刻苦耐勞、勤儉度日，經過了兩百多天，我終於考上台科大。
：「阿嬤，我考上台科大了，妳可以原諒我了嗎？」
：「好吧，就原諒你這一次，為了慶祝你考上台科大，阿嬤就炒客家小炒給你吃吧。」 
看著精美的空盤，我看到阿嬤用心準備的客家小炒，就知道阿嬤非常開心我考上好學校，
止不住的眼淚宣洩而出，兩百多天的壓力頓時釋放，拿起手中的涼水，看著好吃的客家小炒，我與阿嬤度過完美的晚餐時光。

#後記，考上台科的我，非常想念阿嬤的客家小炒，想起吃完後的空腹感，淚水不禁潸潸落下，
因此做出了客家小幫手，讓我不忘記客家人驕傲，也能懷念跟阿嬤的晚餐時光。
"""

QuickSearchCourseLocation={'ADG015301': ['造型藝術與創意美學', 'W10,W9'], 'ADG018301': ['建築基礎攝影', 'M10,M9'], 'ADG020301': ['建築十二問－名家論壇(一)', 'TA,TB,TC'], 'BAG004301': ['行銷管理', 'TA,TB,TC'], 'BAG005301': ['會計學', 'S2,S3,S4'], 'BAG006301': ['財務管理', 'S6,S7,S8'], 'BAG007301': ['數據分析', 'RA,RB,RC'], 'CEG321301': ['人文與科技實務講座', 'WA,WB,WC'], 'CEG323301': ['性別、科技、全球化', 'MA,MB'], 'CHG303301': ['科技與人生', 'F8,F9'], 'ECG003301': ['台灣電資產業論壇與工程倫理', 'RA,RB,RC'], 'FBG006301': ['品牌價值創新講座', 'TA,TB,TC'], 'GE1515301': ['國際文化交流實務', 'F3,F4'], 'GE1515302': ['國際文化交流實務', 'W3,W4'], 'GE3401301': ['憲法', 'M8,M9'], 'GE3401302': ['憲法', 'M6,M7'], 'GE3402301': ['政黨政治與民主發展', 'M6,M7'], 'GE3405301': ['社會科學概論', 'M8,M9'], 'GE3405304': ['社會科學概論', 'R8,R9'], 'GE3407301': ['國際現勢', 'T8,T9'], 'GE3604301': ['性別與法律', 'F6,F7'], 'GE3605302': ['智慧財產權法概要', 'F1,F2'], 'GE3606301': ['民法概要', 'R1,R2'], 'GE3642301': ['古典希臘的思想與文化', 'W1,W2,W3'], 'GE3700301': ['文學與人生', 'F6,F7'], 'GE3708301': ['台灣社會變遷', 'M6,M7'], 'GE3708302': ['台灣社會變遷', 'M8,M9'], 'GE3709301': ['歷史與文明的變遷', 'W1,W2'], 'GE3709302': ['歷史與文明的變遷', 'W3,W4'], 'GE3710301': ['近代東亞視覺與文化史', 'W6,W7'], 'GE3710302': ['近代東亞視覺與文化史', 'W8,W9'], 'GE3711301': ['華人歷史與文化', 'R6,R7'], 'GE3711302': ['華人歷史與文化', 'R8,R9'], 'GE3714301': ['中國與東亞文明史', 'F6,F7'], 'GE3714302': ['中國與東亞文明史', 'F8,F9'], 'GE3719301': ['人類文明起源史', 'T1,T2'], 'GE3719302': ['人類文明起源史', 'T6,T7'], 'GE3723301': ['藝術創作與心靈探索', 'W6,W7'], 'GE3723302': ['藝術創作與心靈探索', 'W8,W9'], 'GE3724301': ['近代中國史與文創運用', 'W6,W7'], 'GE3724302': ['近代中國史與文創運用', 'W8,W9'], 'GE3725301': ['消費者保護法', 'R6,R7'], 'GE3727301': ['臺灣庶民生活史', 'W6,W7'], 'GE3727302': ['臺灣庶民生活史', 'W8,W9'], 'GE3728301': ['音樂與文化', 'R2,R3,R4'], 'GE3728302': ['音樂與文化', 'R6,R7,R8'], 'GE3728304': ['音樂與文化', 'T6,T7,T8'], 'GE3729301': ['數位藝術設計', 'R6,R7'], 'GE3729302': ['數位藝術設計', 'R8,R9'], 'GE3900301': ['藝術賞析', 'T8,T9'], 'GE3900304': ['藝術賞析', 'R3,R4'], 'GE3901301': ['哲學與人生', 'T6,T7'], 'GE3901302': ['哲學與人生', 'R3,R4'], 'GE3901303': ['哲學與人生', 'R6,R7'], 'GE3903302': ['邏輯思考概論', 'T8,T9'], 
'GE3907301': ['管理概論', 'R1,R2'], 'GE3907302': ['管理概論', 'R3,R4'], 'GE3909302': ['醫學與生活', 'F6,F7'], 'GE3909303': ['醫學與生活', 'F1,F2'], 'GE3909305': ['醫學與生活', 'F8,F9'], 'GE3909306': ['醫學與生活', 'F3,F4'], 'GE3917301': ['藥物與健康', 'W6,W7'], 'GE3917302': ['藥物與健康', 'W8,W9'], 'GE3931301': ['普通心理學', 'R6,R7,R8'], 'GE3931302': ['普通心理學', 'F2,F3,F4'], 'HCG015301': ['骨骼肌肉評估和物理治療', 'F5,F6'], 'IBG006301': ['專利101：專利制度入門與基礎', 'F3,F4'], 'IBG007301': ['時事漫談智慧財產與科技法', 'T3,T4'], 'MBG204301': ['溝通與表達', 'F6,F7'], 'MBG204302': ['溝通與表達', 'F8,F9'], 'MEG302301': ['3D列印原理與應用實務', 'W6,W7'], 'MEG302302': ['3D列印原理與應用實務', 'W6,W7'], 'MIG001301': ['資訊科學導論', 'T6,T7,T8'], 'TCG003301': ['活力合唱（一）', 'R6,R7,R8'], 'TCG033301': ['文藝發展與流行音樂文化', 'MA,MB,MC'], 'TCG034301': ['文學與電影', 'RA,RB,RC'], 'TCG035301': ['心靈提升實作', 'S3,S4'], 'TCG036301': ['臨終關懷與生命教育', 'W6,W7'], 'TCG037301': ['親近經典智慧', 'W3,W4'], 'TCG039301': ['環境關懷與生態寫作', 'R3,R4'], 'TCG040301': ['人我關懷與心靈成長', 'R8,R9'], 'TCG045301': ['部落漫遊', 'W10,W9'], 'TCG046301': ['性別與社會福利', 'W3,W4'], 'TCG047301': ['養生醫學', 'W5'], 'TCG047302': ['養生醫學', 'W7'], 'TCG048301': ['雜誌編輯與學習', 'W10,W9'], 'TCG056301': ['國際禮儀', 'WA,WB'], 'TCG058301': ['工業4.0導論', 'F6,F7'], 'TCG062301': ['東南亞社會與文化', 'M3,M4'], 'TCG063301': ['口語表達', 'T8,T9'], 'TCG065301': ['經濟學：市場與趨勢', 'R6,R7'], 'TCG068301': ['領導與生活', 'M8,M9'], 'TCG072301': ['生死議題與臨終關懷', 'M6,M7'], 'TCG073301': ['群眾生活中的科技議題', 'RA,RB'], 'TCG074301': ['電信政策', 'RA,RB'], 'TCG075301': ['媒體與社會', 'M3,M4'], 'TCG078301': ['大數據與程式設計導論', 'M10,M9'], 'TCG079301': ['行動通訊與生活', 'F6,F7'], 'TCG080301': ['領導與溝通', 'T6,T7'], 'TCG082301': ['文化與社會', 'M8,M9'], 'TCG084301': ['愛情心理學', 'TA,TB'], 'TCG085301': ['從韓流文化看韓國社會', 'T8,T9'], 'TCG086301': ['園藝治療的實務運用', 'R8,R9'], 'TCG087301': ['愛情多樣性', 'RA,RB'], 'TCG088301': ['藝術電影賞析', 'R8,R9'], 'TCG093301': ['人際溝通與親密', 'WA,WB'], 'TCG094301': ['大數據分析概觀與實務研討', 'F8,F9'], 
'TCG095301': ['當代科技的健康效應', 'T8,T9'], 'TCG096301': ['歐洲文化與企業概論', 'W8,W9'], 'TCG097301': ['世界當代文化史與紀錄片田調研究', 'R10,R9'], 'TCG098301': ['細胞、分子與生命', 'W8,W9'], 'TCG099301': ['影像記事中的近代兩岸', 'T10,T9'], 'TCG100301': ['書法藝術', 'WA,WB'], 'FE1041701': ['實用華語班(第一級)', 'RA,RB,RC'], 'FE1041702': ['實用華語班(第一級)', 'WA,WB,WC'], 'FE1041703': ['實用華語班(第一級)', 'MA,MB,MC'], 'FE1042701': ['實用華語班(第二級)', 'TA,TB,TC'], 'FE1042702': ['實用華語班(第二級)', 'WA,WB,WC'], 'FE1043701': ['實用華語班(第三級)', 'RA,RB,RC'], 'FE1044701': ['實用華語班(第四級)',
'MA,MB,MC'], 'FE1045701': ['實用華語班(第五級)', 'TA,TB,TC'], 'FE1051701': ['進階華語班(第一級)', 'MA,MB,MC'], 'FE1062701': ['商務華語（一）', 'TA,TB,TC'], 'FE1071701': ['華語口語訓練', 'M10,M9'], 'FE1071702': ['華語口語訓練', 'T8,T9'], 'FE1071703': ['華語口語訓練', 'R8,R9'], 'FE1072701': ['初級新聞華語(一)', 'TA,TB,TC'], 'FE1081701': ['初級中文讀寫 (一)', 'RA,RB,RC'], 'FE1112701': ['英文實務', 'TA,TB'], 'FE1112702': ['英文實務', 'R8,R9'], 'FE1112703': ['英文實務', 'W10,WA'], 'FE1151701': ['文法與修辭', 'W1,W2'], 'FE1151702': ['文法與修辭', 'W3,W4'], 'FE1151703': ['文法與修辭', 'F8,F9'], 'FE1151704': ['文法與修辭', 'T3,T4'], 'FE1231701': ['初級英文寫作(一)', 'M3,M4'], 'FE1231702': ['初級英文寫作(一)', 'M10,MA'], 'FE1231703': ['初級英文寫作(一)', 'T6,T7'], 'FE1231704': ['初級英文寫作(一)', 'W8,W9'], 'FE1241701': ['中級英文寫作(一)', 'F3,F4'], 'FE1241702': ['中級英文寫作(一)', 'M8,M9'], 'FE1241703': ['中級英文寫作(一)', 'R8,R9'], 'FE1351701': ['英語演講(一)', 'T8,T9'], 'FE1471701': ['英文小說與電影', 'M8,M9'], 'FE1471702': ['英文小說與電影', 'T3,T4'], 'FE1571701': ['世界文化', 'M8,M9'], 'FE1571702': ['世界文化', 'F6,F7'], 'FE1571703': ['世界文化', 'T8,T9'], 'FE1571704': ['世界文化', 'W8,W9'], 'FE1581701': ['休閒英文', 'R3,R4'], 'FE1581702': ['休閒英文', 'T3,T4'], 'FE1591701': ['職場英文', 'M1,M2'], 'FE1591702': ['職場英文', 'M8,M9'], 'FE1591703': ['職場英文', 'W8,W9'], 'FE1591704': ['職場英文', 'F6,F7'], 'FE1621701': ['科技英文', 'T3,T4'], 'FE1621702': ['科技英文', 'T8,T9'], 'FE1621703': ['科技英文', 'R6,R7'], 'FE1721701': ['藝術英文', 'W8,W9'], 'FE1741701': ['商用英文書信', 'T8,T9'], 'FE1741702': ['商用英文書信', 'W8,W9'], 'FE1751701': ['商務英文溝通', 'T8,T9'], 'FE1751702': ['商務英文溝通', 'T10,TA'], 'FE1751703': ['商務英文溝通', 'W6,W7'], 'FE1771701': ['行銷英文', 'F6,F7'], 'FE1781701': ['觀光英文', 'F3,F4'], 'FE1781702': ['觀光英文', 'T6,T7'], 
'FE1781703': ['觀光英文', 'M8,M9'], 'FE1781704': ['觀光英文', 'M3,M4'], 'FE1791701': ['簡報英文', 'W6,W7'], 'FE1791702': ['簡報英文', 'M8,M9'], 'FE1791703': ['簡報英文', 'R8,R9'], 'FE1821701': ['新聞英文', 'W3,W4'], 'FE1821702': ['新聞英文', 'R6,R7'], 'FE1821703': ['新聞英文', 'R10,RA'], 'FE1851701': ['國際議題分析', 'M6,M7'], 'FE1851702': ['國際議題分析', 'R3,R4'], 'FE1871701': ['跨文化溝通理解', 'M8,M9'], 'FE1871702': ['跨文化溝通理解', 'W3,W4'], 'FE1871703': ['跨文化溝通理解', 'F3,F4'], 'FE1911701': ['餐旅英文', 'W6,W7'], 'FE1911702': ['餐旅英文', 'T8,T9'], 'FE1911703': ['餐旅英文', 'F3,F4'], 'FE1921701': ['進階英文閱讀', 'R3,R4'], 'FE1921702': ['進階英文閱讀', 'R8,R9'], 'FE1921703': ['進階英文閱讀', 'T8,T9'], 'FE1931701': ['進階英語溝通', 'M6,M7'], 'FE1931702': ['進階英語溝通', 'T6,T7'], 'FE1931703': ['進階英語溝通', 'W8,W9'], 'FE1951701': ['德語入門', 'W1,W2'], 'FE1961701':
['初級德語 (一)', 'W3,W4'], 'FE1962701': ['初級德語 (二)', 'W1,W2'], 'FE2021701': ['英語發音練習', 'M6,M7'], 'FE2021702': ['英語發音練習', 'R8,R9'], 'FE2031701': ['體育英文', 'R8,R9'], 'FE2031702': ['體育英文', 'T8,T9'], 'FE2031703': ['體育英文', 'F3,F4'], 'FE2051701': ['性別、性向與文化', 'W8,W9'], 'FE2061701': ['印尼語入門', 'T8,T9'], 'FE2062701': ['初級印尼語（一）', 'W8,W9'], 'FE2111701': ['越南語入門', 'W8,W9'], 'FE2131701': ['初級越南語 (一)', 'M8,M9'], 'FE2132701': ['初級越南語 (二)', 'M10,MA'], 'FE2141701': ['故事力：商用英語溝通', 'T8,T9'], 'FE2141702': ['故事力：商用英語溝通', 'F6,F7'], 'FE2151701': ['希臘羅馬神話：英文選讀', 'M10,MA'], 'FE2171701': ['日語入門', 'T8,T9'], 'FE2172701': ['初級日語（一）', 'R8,R9'], 'FL1006302': ['語言學概論(一)', 'T3,T4'], 'FL3323701': ['翻譯與習作', 'F3,F4'], 'FL3402302': ['英語語音學', 'T1,T2'], 'FL3800701': ['進階西班牙文(一)', 'F3,F4'], 'FL3805701': ['進階日文(一)', 'T6,T7'], 'FL3805702': ['進階日文(一)', 'R8,R9'], 'FL3813701': ['進階法文(一)', 'T8,T9'], 'FL3830701': ['商務日文', 'M8,M9'], 'FL3833701': ['初級日文(一)', 'M3,M4'], 'FL3833702': ['初級日文(一)', 'R6,R7'], 'FL3833703': ['初級日文(一)', 'R6,R7'], 'FL3833704': ['初級日文(一)', 'M6,M7'], 'FL3833705': ['初級日文(一)', 'R3,R4'], 'FL3833706': ['初級日文(一)', 'W3,W4'], 'FL3833707': ['初級日文(一)', 'W6,W7'], 'FL3841701': ['初級西班牙文(一)', 'F1,F2'], 'FL3841702': ['初級西班牙文(一)', 'F6,F7'], 'FL3846701': ['初級法文(一)', 'M6,M7'], 'FL3846702': ['初級法文(一)', 'M8,M9'], 'FL3848701': ['初級德文(一)', 'R1,R2']}
#從新網站早教室位置
def QuickSearchCourseLocationFunction(query):
    returnText=""
    location=""
    for i in QuickSearchCourseLocation:
        if query in QuickSearchCourseLocation[i][0]:
            url="https://querycourse.ntust.edu.tw/QueryCourse/api/coursedetials?semester=1081&course_no="+str(i)+"&language=zh"
            r=requests.get(url)
            result=json.loads(r.text)
            content= next(iter(result), '不存在')
            location=str(content["ClassRoomNo"])
            returnText+=QuickSearchCourseLocation[i][0]+" "+QuickSearchCourseLocation[i][1]+" "+location+"\n"
            r.close()
    if returnText=="":
        return "找不到此關鍵字，484打錯字ㄌ，也有可能客家小幫手被玩壞了。"
    else:
        return returnText
#從舊網站找教室位置
def QuickSearchCourseLocationFunctionOldWebsite(query):
    returnText=""
    loaction=""
    for i in QuickSearchCourseLocation:
        if query in QuickSearchCourseLocation[i][0]:
            url="http://info.ntust.edu.tw/faith/edua/app/qry_linkoutline.aspx?semester=1081&courseno="+str(i)
            r=requests.get(url)
            bs=BeautifulSoup(r.text,"html.parser")
            span=bs.find("span",id="lbl_timenode")
            location=span.find("font")
            classlocation=location.text.replace(" ","")
            returnText+=QuickSearchCourseLocation[i][0]+"\t"+QuickSearchCourseLocation[i][1]+"\t"+classlocation+"\n"
            r.close()
    if returnText=="":
        return "找不到此關鍵字，484打錯字ㄌ，也有可能客家小幫手被玩壞了。"
    else:
        return returnText
