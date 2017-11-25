#"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
a = ""
list_strings = []
list_strring_length = []
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

for string in list_strings:
    list_strring_length.append(len(string))


print("{0}:{1}".format(list_strings,list_strring_length))
