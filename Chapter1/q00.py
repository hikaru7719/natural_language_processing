#文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
s = "stressed"
b = ""
for num in range(1,len(s)):
    a = num * -1
    b = b + s[a]
print("{0}".format(b));
