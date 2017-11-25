#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
#この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
text = "I am an NLPer"
def ngram(n,string):
    list_answer = []
    for num in range(0,len(string)-(n-1)):
        i = 0
        if isinstance(string,str):
            b=""
            while i < n:
                b = b +string[num +i]
                i += 1
        elif isinstance(string,list):
            b=[]
            while i < n:
                b.append(string[num +i])
                i += 1
        list_answer.append(b);
    return list_answer
list_char_bigram = ngram(2,text)
print("{0}".format(list_char_bigram))

list_strings = text.split()
list_word_bigram = ngram(2,list_strings)
print("{0}".format(list_word_bigram))
