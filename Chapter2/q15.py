#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
# tail -n 5 col3.txt
import argparse

parser = argparse.ArgumentParser(description = "description goes here")
parser.add_argument("-n", type=int, help = "Write Natural Number. This option is required", required=True)
parser.add_argument("-f", type=str, help = "Write file name. This option is required", required=True)

args = parser.parse_args()
natural_number = args.n
file_name = open(args.f)
count = 0
count2 = 1;
for row in file_name:
    count += 1
print(count)
file_name2 = open(args.f)
for row in file_name2:
    if count2 > (count - natural_number):
        print("{0}:{1}".format(count2,row))
    count2 += 1
