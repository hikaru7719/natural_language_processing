#各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
file = open("hightemp.txt")
map = {}
for row in file:
    split = row.split('\t')
    if split[0] in map:
        map[split[0]] += 1
    else:
        map[split[0]] = 1
list = sorted(map.items(), key=lambda x: -x[1])
number = 1
for row in list:
    print("{0}:{1}".format(str(number),row[0]))
    number += 1
