#!/bin/sh

echo "何年?"
read YYYY
if [ ! -d ~/blog.yamachaaan.net/blog/draft/$YYYY/ ]
then
    mkdir ~/blog.yamachaaan.net/blog/draft/$YYYY/
else
cd ~/blog.yamachaaan.net/blog/draft/$YYYY/
fi
cd ~/blog.yamachaaan.net/blog/draft/$YYYY/
name=`date +%Y-w%V`
cd ~/blog.yamachaaan.net/blog/draft/$YYYY/
touch "$name.md"
echo "---" > "$name.md"
echo "layout: post" >> "$name.md"
date=`date +%Y-%m-%d`
echo "pubdata: $date-23:59:59+09:00" >> "$name.md"
echo "title: '$name 今週のふりかえり'" >> "$name.md"
echo "tags: ['weekly report']" >> "$name.md"
echo "pagetype: posts" >> "$name.md"
echo "---" >> "$name.md"
echo "$nameのふりかえり。">> "$name.md"
echo "## 今週のPost">> "$name.md"
echo "## 今週の振り返り">> "$name.md"
echo "## 今週のポモドーロ">> "$name.md"
echo "## KPT ">> "$name.md"
echo "### K">> "$name.md"
echo "### P">> "$name.md"
echo "### T">> "$name.md"
echo "## 今週の計画">> "$name.md"
vim ~/blog.yamachaaan.net/blog/draft/$YYYY/$name.md

