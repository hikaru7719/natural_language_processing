#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ
file = open("hightemp.txt")
set = set([])
for row in file:
    split = row.split('\t')
    set.add(split[0])
print(set)
