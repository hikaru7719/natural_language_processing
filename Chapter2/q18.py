#各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
#確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
file = open('hightemp.txt')
list = []
for row in file:
    row = row.strip("\n")
    split = row.split("\t")
    list.append(split)
list.sort(key=lambda x:x[2])
for row in list:
    print("\t".join(row))
