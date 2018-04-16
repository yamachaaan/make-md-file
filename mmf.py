#encoding:utf-8
"""
Name:     mmf
Author:   yamachaaan
URL:      http://yamachaaan.net
Modified: 2018-04-13
"""

"""
import Library
"""
import yaml
import os
import linecache
import re
from datetime import datetime,timedelta,date
from dateutil.relativedelta import relativedelta

"""
initial variable
"""
rootPath=""
FileFullPath=""
header=""
weekContent=[]
monthContent=[]
quoteContent=[]
yearContent=[]
mmfType=[]

# load yaml
def define():
    with open('config.yml','r') as yml:
        config = yaml.load(yml)
        global rootPath
        rootPath = config['Main']['rootPath']
        global header
        header = config['Main']['header']
        global weekContent
        global monthContent
        global quoteContent
        global yearContent
        weekContent = (config['Content']['Weekly'])
        monthContent = (config['Content']['Monthly'])
        quoteContent = (config['Content']['Quarter'])
        yearContent = (config['Content']['Year'])

def setmmfType():
    mmfType=[]
    Date = datetime.today()
    last_day = (Date + relativedelta(months=1)).replace(day=1) - timedelta(days=1)
    if Date.weekday() is 6:
        mmfType.insert(1,"week")
    if last_day.month is (1 or 3 or 5 or 7 or 8 or 10 or 12):
        if Date.day is 31:
            mmfType.insert(2,"month")
    elif last_day.month is (4 or 6 or 9 or 11):
        if Date.day is 30:
            mmfType.insert(2,"month")
    else: # 2月
        if Date.day is (28 or 29):
            mmfType.insert(2,"month")
    if last_day.month is (3 or 12):
        if Date.day is 31:
            mmfType.insert(3,"quote")
    if last_day.month is (6 or 9):
        if Date.day is 30:
            mmfType.insert(3,"quote")
    if last_day.month is 12:
        if Date.day is 31:
            mmfType.insert(4,"year")
    return mmfType

def setPostDate():
    global header
    Date = datetime.today().strftime("%Y-%m-%d")
    header[2] = "pubdate: " + Date + "-23:59:59+09:00\n"

def setReview():
    global weekContent
    global monthContent
    global quoteContent
    global yearContent
    global mmfType
    now = datetime.today()
    if ("week" in mmfType) is True:
        weekNo = date(now.year,now.month,now.day).isocalendar()
        weekContent[0] = (str(now.year) + "-W" + str(weekNo[1]) + " をふりかえる。  \n")
        weekContent.append("### " + str(now.year) + "-W" + str(weekNo[1] + 1) + " の目標\n")
    if ("month" in mmfType) is True:
        MonthContent[0] = (str(now.year) + "-" + str(now.month) + " をふりかえる。  \n")
        MonthContent.append("### " + str(now.year) + "-" + str(now.month + 1) + " の目標\n")
    if ("quote" in mmfType) is True:
        if now.month % 3 == 0:
            quoteContent[0] = (str(now.year) + "-Q" + str(month / 3) + " をふりかえる。  \n")
            if month/3 == 4:
                quoteContent.append("### " + str(now.year + 1) + "-Q" + str(1) + " の目標\n")
            else:
                quoteContent.append("### " + str(now.year) + "-Q" + str(month / 3) + " の目標\n")
    if ("year" in mmfType) is True:
        yearContent[0] = (str(now.year) + " をふりかえる。  \n")
        yearContent.append("### " + str(now.year + 1) + " の目標\n")

def getPostTitle(tmp):
    global rootPath
    pathList = tmp.split("-")
    targetFilePath = rootPath + pathList[0] + "/" + pathList[1] + "/" + tmp + "-diary.md"
    PostTitle = linecache.getline(targetFilePath, int(4)).replace('\n','')
    return re.sub('[title: ]','',PostTitle)
# createFile
def createFile():
    global rootPath
    global FileFullPath
    global header
    global weekContent
    global monthContent
    global quoteContent
    global yearContent
    global reviewFirst
    global reviewNext
    now = datetime.today().strftime("%Y-%m-%d")
    date = now.split("-")
    FilePath = "data/" + date[0] + "/" + date[1] + "/"
    FileName = str(now) + "-diary.md"
    if (os.path.isdir(rootPath + FilePath)):
        pass
    else:
        os.makedirs(rootPath + FilePath)
    os.chdir(rootPath+ FilePath)
    FileFullPath = rootPath + FilePath + FileName
    f = open(FileFullPath,'w')
    for headerCont in header:
        f.write(headerCont)
    #if ("week" in mmfType) is True:
    if ("week" in mmfType) is True:
        cnt = 0
        for weekCont in weekContent:
            cnt += 1
            if cnt == 3:
                for Cnt in range(1,8):
                    tmp = str((datetime.now() - timedelta(Cnt)).strftime("%Y-%m-%d"))
                    urlList = tmp.split("-")
                    surl = "/" + urlList[0] + "/" + urlList[1] + "/" + urlList[2] + "/"
                    seturl = "http://blog.yamachaaan.net" + surl + "diary.html"
                    f.write("- [" + tmp + " " + getPostTitle(tmp) + "](" + seturl + ")\n")
            f.write(weekCont)
    if ("month" in mmfType) is True:
        for monthCont in monthContent:
            f.write(monthCont)
    if ("quote" in mmfType) is True:
        for quoteCont in quoteContent:
            f.write(quoteCont)
    if ("year" in mmfType) is True:
        for yearCont in yearContent:
            f.write(yearCont)
    f.close()

# Main
if __name__ == '__main__':
    define()
    mmfType = setmmfType()
    setPostDate()
    setReview()
    createFile()
