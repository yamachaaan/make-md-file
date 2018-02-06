#encoding:utf-8
"""
Name:     mmf-w
Author:   yamachaaan
URL:      http://yamachaaan.net
Modified: 2018-01-18
"""

import os
from datetime import datetime,timedelta,date
import linecache

now = datetime.now()
strDate = now.isoformat()
datepath = now.strftime("%Y/%m")
filename = now.strftime("%Y-%m-%d") + "-diary"
mainPath = "/Users/yamachaaan/blog.yamachaaan.net/data/"
#mainPath = "/users/yamachaaan/mmf/"
dayList = [0 for Cnt in range(6)]
postList = [0 for Cnt in range(6)]
weekNo = date(now.year,now.month,now.day).isocalendar()

def makeFile():
    if (os.path.isdir(mainPath + datepath)):
        pass
    else:
        os.makedirs(mainPath + datepath)
    os.chdir(mainPath + datepath)

def setweekDay():
    for dayCnt in range(7):
        d = now-timedelta(dayCnt)
        dayList.insert(dayCnt,d.strftime("%Y-%m-%d"))

def getPostTitle(tmp):
    pathList = tmp.split("-")
    targetFilePath = mainPath + pathList[0] + "/" + pathList[1] + "/" + tmp + "-diary.md"
    PostTitle = linecache.getline(targetFilePath, int(4))
    return PostTitle

def createContents():
    f = open(filename + '.md','a')
    f.write("---\n")
    f.write("layout: post\n")
    f.write("pubdata: " + strDate + "-23:59:59+09:00\n")
    f.write("title: " + str(now.year) + "-W" + str(weekNo[1]) + " ふりかえり" +"\n")
    f.write("tags: ['review']\n")
    f.write("pagetype: posts\n")
    f.write("---\n")
    f.write(str(now.year) + "年-W" + str(weekNo[1]) + "をふりかえる。")
    f.write("  \n")
    f.write("### 目標")
    f.write("  \n")
    f.write("### 記事")
    f.write("  \n")
    for Cnt in range(7):
        tmp = str((now - timedelta(Cnt)).strftime("%Y-%m-%d"))
        urlList = tmp.split("-")
        surl = "/" + urlList[0] + "/" + urlList[1] + "/" + urlList[2] + "/"
        seturl = "http://blog.yamachaaan.net" + surl + "diary.html"
        f.write("- [" + tmp + " " + getPostTitle(tmp) + "](" + seturl + ")\n")

    f.write("### つくったもの")
    f.write("  \n")
    f.write("### よんだもの")
    f.write("  \n")
    f.write("### みたもの")
    f.write("  \n")
    f.write("### " + str(now.year) +"年-W" + str(weekNo[1] + 1) + "の目標")
    f.write("  \n")
    f.close()

if __name__ == '__main__':
    makeFile()
    setweekDay()
    createContents()
