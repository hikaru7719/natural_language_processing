#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
p = "パトカー"
t = "タクシー"
answer = ""
for num in range(len(p)):
    answer +=  p[num] + t[num]

print("{0}".format(answer))
