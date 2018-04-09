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
    elif target == 4:
        result = 2
    elif target ==9:
        result = 3
    else:
        result = 4
    return result

def createContents(ymdPath):
    MonthContent.append(ymdPath[0] + "-Q" + str(setQuarter(ymdPath[1])) + " のふりかえり。  \n")
    MonthContent.append("### " + ymdPath[0] + "-Q" + str(setQuarter(ymdPath[1])) + " の目標\n")
    MonthContent.append("\n")
    dt = datetime.now() + relativedelta(months=1)
    nextYear = dt.year
    nextMonth = dt.month
    nextMonth = '{0:02d}'.format(nextMonth)
    MonthContent.append("### " + str(nextYear) + "-Q" + str(setQuarter(ymdPath[1]) + 1) + " の目標\n")
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
