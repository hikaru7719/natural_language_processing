# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
#という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
#取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
a = ""
list_strings = []
list_number = [1,5,6,7,8,9,15,16,19]
dic = {}
for char in str:
    if char == " ":
        if a != "":
            list_strings.append(a)
        a = ""
    elif char == ",":
        if a != "":
            list_strings.append(a)
        a =""
    elif char == ".":
        if a != "":
            list_strings.append(a)
        a = ""
    else:
        a += char
print(list_strings)

for num in  range(0,len(list_strings)-1):
    if num + 1 == list_number[0]:
        a = list_strings[num]
        dic[num+1] = a[0]
        list_number.pop(0)
    else:
        a = list_strings[num]
        dic[num+1] = a[0]+a[1]

for key,value in dic.items():
    print("{0}:{1}".format(key,value))
