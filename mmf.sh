#!/bin/sh

read YYYY
read MM
cd ~/blog.yamachaaan.net/blog/data/$YYYY/$MM/
read DATE
touch "$DATE-diary.md"
echo "---" > "$DATE-diary.md"
echo "layout: post" >> "$DATE-diary.md"
echo "pubdata: $DATE-23:59:59+09:00" >> "$DATE-diary.md"
read TITLE
echo "title: '$TITLE'" >> "$DATE-diary.md"
read TAG
echo "tags: ['$TAG']" >> "$DATE-diary.md"
echo "pagetype: posts" >> "$DATE-diary.md"
echo "---" >> "$DATE-diary.md"
echo "## 日記¥n">> "$DATE-diary.md"
echo 
echo "## 作業メモ">> "$DATE-diary.md"
echo
echo "## 作ったもの">> "$DATE-diary.md"
echo 
echo "## KPT">> "$DATE-diary.md"
echo "### K">> "$DATE-diary.md"
echo "- ">>  "$DATE-diary.md"
echo "### P">> "$DATE-diary.md"
echo "- ">> "$DATE-diary.md"
echo "### T">> "$DATE-diary.md"
echo "- ">> "$DATE-diary.md"
vim ~/blog.yamachaaan.net/blog/data/$YYYY/$MM/$DATE-diary.md

