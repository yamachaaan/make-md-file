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

def createPath():
    now = datetime.now().strftime("%Y-%m-%d")
    fileName = now + "-diary.html"
    ymdPath = fileName.split("-")
    fileFullPath = mainPath + ymdPath[0] + "/" + ymdPath[1] + "/" + ymdPath[2] + "/" + fileName
    print(fileFullPath)
    print(ymdPath[1])

# def setTitle():
# 
# def makeFile():
# 
# def createContnts():

if __name__ == '__main__':
    createPath()
    #setTitle()
    #makeFile()
    #createContnts()
