#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
import argparse,math

parser = argparse.ArgumentParser(description = "description goes here")
parser.add_argument("-n", type=int, help = "Write Natural Number. This option is required", required=True)
parser.add_argument("-f", type=str, help = "Write file name. This option is required", required=True)

args = parser.parse_args()
natural_number = args.n
file_name = open(args.f)
count = 0
for row in file_name:
    count += 1
print(count)

file_name2 = open(args.f)

count = math.ceil(count/natural_number)
n = 0
count2 = 1
text = "new_file"
buffer = ""

for row in file_name2:
    if n == 0:
        buffer = text +str(count2) + ".txt"
        file = open(buffer,'w')
        count2 += 1
        n += 1;
        file.write(row)
    elif n < count:
        file.write(row)
        n += 1
        if n == count:
            n=0
            file.close()
