#encoding:utf-8
"""
Name:     mmf-d
Author:   yamachaaan
URL:      http://yamachaaan.net
Modified: 2017-04-16
"""

import os
import datetime

now = datetime.datetime.now()

date = now.strftime("%Y-%m-%d")
datepath = now.strftime("%Y/%m")
filename = date + "-diary"
mainpath = "/home/yamachaaan/blog.yamachaaan.net/data/"

if (os.path.isdir(mainpath + datepath)):
    pass
else :
    os.makedirs(mainpath + datepath)
os.chdir(mainpath + datepath)

f = open(filename + '.md','a')
f.write("---\n")
f.write("layout: post\n")
f.write("pubdata: " + date + "-23:59:59+09:00\n")
f.write("title: \n")
f.write("tags: ['diary']\n")
f.write("pagetype: posts\n")
f.write("---\n")
f.close()
