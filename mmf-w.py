#encoding:utf-8
"""
Name:     mmf-w
Author:   yamachaaan
URL:      http://yamachaaan.net
Modified: 2018-01-18
"""

import os
import datetime

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
datepath = now.strftime("%Y/%m")
filename = date + "-diary"
mainPath = "/Users/yamachaaan/blog.yamachaaan.net/data/"

def makeFile():
    if (os.path.isdir(mainPath + datepath)):
        pass
    else:
        os.makedirs(mainPath + datepath)
    os.chdir(mainPath + datepath)

def createContents():
    year = now.strftime("%Y")
    month = now.strftime("%-m")
    day = now.strftime("%-d")
    list = datetime.date(int(year),int(month),int(day)).isocalendar()
    f = open(filename + '.md','a')
    f.write("---\n")
    f.write("layout: post\n")
    f.write("pubdata: " + date + "-23:59:59+09:00\n")
    f.write("title: \n")
    f.write("tags: ['review']\n")
    f.write("pagetype: posts\n")
    f.write("---\n")
    f.write(now.strftime("%Y") + "年-W") + list[1]
    f.write("  \n")
    f.write("### 目標")
    f.write("  \n")
    f.write("### 記事")
    f.write("  \n")
    f.close()

if __name__ == '__main__':
    makeFile()
    createContents()

