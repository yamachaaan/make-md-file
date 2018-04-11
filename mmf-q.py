#encoding:utf-8
"""
Name:     mmf-q
Author:   yamachaaan
URL:      http://yamachaaan.net
Modified: 2018-04-09
"""

import os
from datetime import datetime,timedelta,date
from dateutil.relativedelta import relativedelta

mainPath = "/Users/yamachaaan/blog.yamachaaan.net/data/"
now = datetime.now().strftime("%Y-%m-%d")
MonthContent = []

def setQuarter(ymdPath):
    target = ymdPath
    result = 1
    if target == 3:
        result = 1
    elif target == 6:
        result = 2
    elif target ==9:
        result = 3
    else:
        result = 4
    return result

def setNextQuarter(target):
    result = 0
    if target == 1:
        result = 2
    elif target == 2:
        result = 3
    elif target == 3:
        result = 4
    else:
        result = 1
    return result

def createContents(ymdPath):
    quarterNo = setQuarter(ymdPath[1])
    MonthContent.append(ymdPath[0] + "-Q" + str(quarterNo) + " のふりかえり。  \n")
    MonthContent.append("### " + ymdPath[0] + "-Q" + str(quarterNo) + " の目標\n")
    MonthContent.append("\n")
    MonthContent.append("#### " + "プライベート\n")
    MonthContent.append("\n")
    MonthContent.append("#### " + "資格&免許\n")
    MonthContent.append("\n")
    MonthContent.append("#### " + "身体\n")
    MonthContent.append("\n")
    MonthContent.append("#### " + "お金\n")
    MonthContent.append("\n")
    MonthContent.append("#### " + "学習\n")
    MonthContent.append("\n")
    dt = datetime.now() + relativedelta(months=1)
    nextYear = dt.year
    if quarterNo == 4:
        nextYear = nextYear + 1
    MonthContent.append("### " + str(nextYear) + "-Q" + str(setNextQuarter(quarterNo)) + " の目標\n")
    MonthContent.append("\n")
    MonthContent.append("#### " + "プライベート\n")
    MonthContent.append("\n")
    MonthContent.append("#### " + "資格&免許\n")
    MonthContent.append("\n")
    MonthContent.append("#### " + "身体\n")
    MonthContent.append("\n")
    MonthContent.append("#### " + "お金\n")
    MonthContent.append("\n")
    MonthContent.append("#### " + "学習\n")
    MonthContent.append("\n")
    return MonthContent

def getDate(now):
    SplitYmd = now.split("-")
    return SplitYmd

def createfileName(now):
    fileName = now + "-diary.md"
    return fileName

def createFilePath(ymdPath,fileName):
    fileFullPath = mainPath + ymdPath[0] + "/" + ymdPath[1] + "/" + fileName
    return fileFullPath

def setTitle(ymdPath):
    title = ymdPath[0] + "-Q" + str(setQuarter(ymdPath[1])) + " ふりかえり"
    return title

def makeFile(fileFullPath,title,now,MonthContent):
    f = open(fileFullPath,'w')
    f.write("---\n")
    f.write("layout: post\n")
    f.write("pubdate: " + now + ":23:59:59+09;00\n")
    f.write("title: " + title + "\n")
    f.write("tags: ['review']\n")
    f.write("pagetype: posts\n")
    f.write("---\n")
    for i in MonthContent:
        f.write(i)
    f.close()

if __name__ == '__main__':
    ymdPath = getDate(now)
    createContents(ymdPath)
    fileName = createfileName(now)
    fileFullPath = createFilePath(ymdPath,fileName)
    title = setTitle(ymdPath)
    makeFile(fileFullPath,title,now,MonthContent)
