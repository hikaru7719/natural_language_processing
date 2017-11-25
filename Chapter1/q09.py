#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
#それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
#ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
#（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
#を与え，その実行結果を確認せよ．
import random

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(text)
list_split = text.split()
answer = []
for string in list_split:
    if len(string) <= 4:
        answer.append(string)
    else:
        toList = list(string)
        first = toList[0]
        last = toList[len(string)-1]
        toList.pop(0)
        toList.pop(len(string)-2)
        random.shuffle(toList)
        buffer = ""
        for char in toList:
            buffer += char
        ret = first + buffer + last
        answer.append(ret)

print(" ".join(answer))
