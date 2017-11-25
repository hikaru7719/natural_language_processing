#「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ
s = "パタトクカシーー"
answer = ""
i = 1
for num in range(len(s)-1):
    if num == i-1:
        answer += s[num]
        i += 2
print("{0}".format(answer))
