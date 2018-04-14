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
from datetime import datetime,timedelta,date
from dateutil.relativedelta import relativedelta

"""
initial variable
"""
rootPath=""
header=""
Content=[]
mmfType=[]

# load yaml
def define():
    with open('config.yml','r') as yml:
        config = yaml.load(yml)
        global rootPath
        rootPath = config['Main']['rootPath']
        global header
        header = config['Main']['header']
        global Content
        Content.append(config['Content']['Weekly'])
        Content.append(config['Content']['Monthly'])
        Content.append(config['Content']['Quarter'])
        Content.append(config['Content']['Year'])

# get mmfType
def setmmfType():
    mmfType=[]
    Date = datetime.today()
    last_day = (Date + relativedelta(months=1)).replace(day=1) - timedelta(days=1)
    if Date.weekday() is 6:
        mmfType.insert(1,"week")
    if last_day.month is (1 or 3 or 5 or 7 or 8 or 10 or 12):
        if Date.day is 31:
            mmfType.insert(2,"month")
        else:
            mmfType.insert(0,"day")
    elif last_day.month is (4 or 6 or 9 or 11):
        if Date.day is 30:
            mmfType.insert(2,"month")
        else:
            mmfType.insert(0,"day")
    else: # 2月
        if Date.day is (28 or 29):
            mmfType.insert(2,"month")
        else:
            mmfType.insert(0,"day")
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

# createFile
def createFile():
    global rootPath
    global header
    now = datetime.today().strftime("%Y-%m-%d")
    date = now.split("-")
    FilePath = "data/" + date[0] + "/" + date[1] + "/"
    FileName = str(now) + "-diary.md"
    if (os.path.isdir(rootPath + FilePath)):
        pass
    else:
        os.makedirs(rootPath + FilePath)
    os.chdir(rootPath+ FilePath)
    tmpPath = rootPath + FilePath + FileName
    f = open(rootPath + FilePath + FileName,'w')
    f.write(header)
    if ("week" in mmfType) is True:
        f.write(Content[0])
    if ("month" in mmfType) is True:
        f.write(Content[1])
    if ("quote" in mmfType) is True:
        f.write(Content[2])
    if ("year" in mmfType) is True:
        f.write(Content[3])
    f.close()

# Main
if __name__ == '__main__':
    define()
    mmfType = setmmfType()
    createFile()
