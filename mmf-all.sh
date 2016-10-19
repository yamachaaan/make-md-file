#! bin/bash

# 変数定義
daily="日記"
weekly="週報"
monthly="月報"
quarter="四半期"
year="年報"

# 入力
echo "何書くの？"
read type

# 判定
if [ $type = $daily ]; then
    echo "日記を書くよ"
    source ~/mmf/mmf-d.sh
elif [ $type = $weekly ] ; then
    echo "週報を書くよ"
    source ~/mmf/mmf-w.sh
elif [ $type = $monthly ] ; then
    echo "今月のふりかえりを書くよ"
    source ~/mmf/mmf-m.sh
elif [ $type = $quarter ] ; then
    echo "ハーフのふりかえりを書くよ"
    source ~/mmf/mmf-h.sh
else 
    echo "今年のふりかえりを書くよ"
    source ~/mmf/mmf-y.sh
fi

