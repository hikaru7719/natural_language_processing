#タブ1文字につきスペース1文字に置換せよ．
#確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
#sed -e "s/\t/ /g" hightemp.txt
# coding: utf-8
file = open("hightemp.txt")
for line in file:
    print(line.replace('\t',' '),end="")
file.close()
