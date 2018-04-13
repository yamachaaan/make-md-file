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
Content=""

# load yaml
def define():
    with open('config.yml','r') as yml:
        config = yaml.load(yml)
        global rootPath
        rootPath = config['Main']['rootPath']
        global header
        header = config['Main']['header']
        global Content
        Content = config['Content']['Quarter']

# get mmfType
def setmmfType():
    mmfType=[]
    Date = datetime.today()
    if Date.weekday() is 6:
        mmfType.append("week",0)
    if last_day.month is (1 or 3 or 5 or 7 or 8 or 10 or 12):
        if last_day.day is 31:
            print("Monthly")
        mmfType.append("month",1)
    elif last_day.month is (4 or 6 or 9 or 11):
        if last_day.day is 30:
            print("Monthly")
            mmfType.append("month",1)
    else:
        if last_day.day is (28 or 29):
            print("Monthly")
            mmfType.append("month",1)
    last_day = (Date + relativedelta(months=1)).replace(day=1) - timedelta(days=1)
    if last_day.month is (3 or 12):
        if last_day.day is 31:
            print("Quarter")
            mmfType.append("quote",2)
    if last_day.month is (6 or 9):
        if last_day.day is 30:
            print("Quarter")
            mmfType.append("quote",2)
    if last_day.month is 12:
        if last_day.day is 31:
            print("Year")
            mmfType.append("year",3)
    #return mmfType

# createFile
def createFile():
    global rootPath
    global header
    f = open(rootPath,'w')
    f.write(header)
    f.close()

# Main
if __name__ == '__main__':
    setmmfType()
    define()
    #createFile()
    print (rootPath)
    print (header)
    print (Content)
