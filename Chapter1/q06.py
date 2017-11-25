# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
#それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def bigram(n,string):
    list_answer = []
    for num in range(0,len(string)-(n-1)):
        i = 0
        buffer=""
        while i < n:
            buffer = buffer +string[num +i]
            i += 1
        list_answer.append(buffer);
    return list_answer

list_first = bigram(2,"paraparaparadise")
list_second = bigram(2,"paragraph")
print(list_first)
print(list_second)

print(set(list_first)&set(list_second))
print(set(list_first)|set(list_second))
print(set(list_first)-set(list_second))
if "se" in list_first:
    print("true")
else:
    print("false")

if "se" in list_second:
    print("true")
else:
    print("false")
