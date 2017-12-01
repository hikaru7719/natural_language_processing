#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
#確認にはcutコマンドを用いよ．．
#cut -f 1  hightemp.txt > col1_test.txt
#cut -f 2  hightemp.txt > col2_test.txt
# coding:utf-8
file = open('hightemp.txt')
file2 = open('col1.txt','w')
file3 = open('col2.txt','w')

for row in file:
    col = row.split("\t")
    file2.write(col[0]+"\n")
    file3.write(col[1]+"\n")
file.close()
file2.close()
file3.close()
