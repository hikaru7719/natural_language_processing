#行数をカウントせよ．確認にはwcコマンドを用いよ．
#wcコマンドの結果は左から行数、単語数、バイト数
file = open('hightemp.txt')
count = 0
for row in file:
    count += 1
file.close()
print("{0}".format(count))
