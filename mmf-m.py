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

def createContens():
    return "hoge"

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

def makeFile(fileFullPath,title,now):
    print(fileFullPath)
    f = open(fileFullPath,'w')
    f.write("---\n")
    f.write("layout: post\n")
    f.write("pubdate: " + now + ":23:59:59+09;00\n")
    f.write("title: " + title + "\n")
    f.write("tags: ['diary']\n")
    f.write("pagetype: posts\n")
    f.write("---\n")
    f.write(createContens())
    f.close()

if __name__ == '__main__':
    ymdPath = getDate(now)
    fileName = createfileName(now)
    fileFullPath = createFilePath(ymdPath,fileName)
    title = setTitle(ymdPath)
    makeFile(fileFullPath,title,now)
