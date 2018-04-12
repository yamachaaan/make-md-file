#encoding:utf-8
"""
Name:     mmf-y
Author:   yamachaaan
URL:      http://yamachaaan.net
Modified: 2018-04-12
"""

import os
from datetime import datetime,timedelta,date
from dateutil.relativedelta import relativedelta

mainPath = "/Users/yamachaaan/blog.yamachaaan.net/data/"
now = datetime.now().strftime("%Y-%m-%d")
MonthContent = []

def createContents(ymdPath):
    quarterNo = setQuarter(ymdPath[1])
    MonthContent.append(ymdPath[0] + " のふりかえり。  \n")
    MonthContent.append("### " + ymdPath[0]  + " の目標\n")
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
    nextYear = dt.year + 1
    MonthContent.append("### " + str(nextYear) + " の目標\n")
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
    title = ymdPath[0] + " ふりかえり"
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
