#12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
#確認にはpasteコマンドを用いよ．
#paste -d '\t' col1_test.txt col2_test.txt
col1 = open('col1.txt')
col2 = open('col2.txt')
col3 = open('col3.txt','w')
for row,row2 in zip(col1,col2):
    row = row.replace('\n','\t')
    col3.write(row+row2)
col1.close()
col2.close()
col3.close()
