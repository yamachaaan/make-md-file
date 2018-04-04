#encoding:utf-8
"""
Name:     mmf-m
Author:   yamachaaan
URL:      http://yamachaaan.net
Modified: 2018-02-07
"""

import os
from datetime import datetime,timedelta,date

mainPath = "/Users/yamachaaan/blog.yamachaaan.net/data/"
now = datetime.now().strftime("%Y-%m-%d")
MonthContent = []

def createContents(ymdPath,MonthContent):
    MonthContent.append(ymdPath[0] + "-" + ymdPath[1] + " のふりかえり。  \n")
    MonthContent.append("### " + ymdPath[0] + "-" + ymdPath[1] + " の目標\n")
    MonthContent.append("\n")
    MonthContent.append("### 週のふりかえり\n")
    MonthContent.append("\n")
    MonthContent.append("### つくったもの\n")
    MonthContent.append("\n")
    MonthContent.append("### よんだもの\n")
    MonthContent.append("\n")
    MonthContent.append("### みたもの\n")
    MonthContent.append("\n")
    MonthContent.append("### " + ymdPath[0] + "-" + ymdPath[1] + " の目標\n")
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
    title = ymdPath[0] + "-" + ymdPath[1] + " ふりかえり"
    return title

def makeFile(fileFullPath,title,now,MonthContent):
    f = open(fileFullPath,'w')
    f.write("---\n")
    f.write("layout: post\n")
    f.write("pubdate: " + now + ":23:59:59+09;00\n")
    f.write("title: " + title + "\n")
    f.write("tags: ['diary']\n")
    f.write("pagetype: posts\n")
    f.write("---\n")
    for i in MonthContent:
        f.write(MonthContent[i])
    f.close()

if __name__ == '__main__':
    ymdPath = getDate(now)
    createContents(ymdPath,MonthContent)
    fileName = createfileName(now)
    fileFullPath = createFilePath(ymdPath,fileName)
    title = setTitle(ymdPath)
    makeFile(fileFullPath,title,now,MonthContent)
