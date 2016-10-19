#!/bin/sh
echo "何年?"
read YYYY
echo "何月?"
read MM
if [ ! -d ~/blog.yamachaaan.net/blog/data/$YYYY/$MM/ ]
then
    mkdir ~/blog.yamachaaan.net/blog/data/$YYYY/$MM/
else
cd ~/blog.yamachaaan.net/blog/data/$YYYY/$MM/
fi
cd ~/blog.yamachaaan.net/blog/data/$YYYY/$MM/
name=`date +%Y-%m-%d`
touch ~/blog.yamachaaan.net/blog/data/$YYYY/$MM/$name-diary.md
echo "---" > "$name-diary.md"
echo "layout: post" >> "$name-diary.md"
echo "pubdata: $name-23:59:59+09:00" >> "$name-diary.md"
echo "タイトルは?"
read TITLE
echo "title: '$TITLE'" >> "$name-diary.md"
echo "タグは？"
read TAG
echo "tags: ['$TAG']" >> "$name-diary.md"
echo "pagetype: posts" >> "$name-diary.md"
echo "---" >> "$name-diary.md"
echo "## 日記">> "$name-diary.md"
echo 
echo "## 作業メモ">> "$name-diary.md"
echo
echo "## 作ったもの">> "$name-diary.md"
echo 
echo "## KPT">> "$name-diary.md"
echo " ">> "$name-diary.md"
echo "### K">> "$name-diary.md"
echo " ">> "$name-diary.md"
echo "- ">>  "$name-diary.md"
echo "### P">> "$name-diary.md"
echo " ">> "$name-diary.md"
echo "- ">> "$name-diary.md"
echo "### T">> "$name-diary.md"
echo " ">> "$name-diary.md"
echo "- ">> "$name-diary.md"
echo " ">> "$name-diary.md"
echo "$name-diary.mdファイルを作成しました。"
vim ~/blog.yamachaaan.net/blog/data/$YYYY/$MM/$name-diary.md
