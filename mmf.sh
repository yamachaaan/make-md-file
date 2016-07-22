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
vim ~/blog.yamachaaan.net/blog/data/$YYYY/$MM/$DATE-diary.md

