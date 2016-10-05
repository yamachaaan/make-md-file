#!/bin/sh

read YYYY
read wXX
cd ~/blog.yamachaaan.net/blog/draft/$YYYY/
touch "$YYYY-$wXX.md"
echo "---" > "$YYYY-$wXX.md"
echo "layout: post" >> "$YYYY-$wXX.md"
echo "pubdata: $DATE-23:59:59+09:00" >> "$YYYY-$wXX.md"
echo "title: '$YYYY-$wXX 今週のふりかえり'" >> "$YYYY-$wXX.md"
echo "tags: ['weekly report']" >> "$YYYY-$wXX.md"
echo "pagetype: posts" >> "$YYYY-$wXX.md"
echo "---" >> "$YYYY-$wXX.md"
echo "$YYYY-$wXXのふりかえり。">> "$YYYY-$wXX.md"
echo "## 今週のPost">> "$YYYY-$wXX.md"
echo "## 今週の振り返り">> "$YYYY-$wXX.md"
echo "## 今週のポモドーロ">> "$YYYY-$wXX.md"
echo "## KPT ">> "$YYYY-$wXX.md"
echo "### K">> "$YYYY-$wXX.md"
echo "### P">> "$YYYY-$wXX.md"
echo "### T">> "$YYYY-$wXX.md"
echo "## 今週の計画">> "$YYYY-$wXX.md"
vim ~/blog.yamachaaan.net/blog/draft/$YYYY/$YYYY-$wXX.md

