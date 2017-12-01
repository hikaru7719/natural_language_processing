#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
#確認にはheadコマンドを用いよ．
#head -n 5 "col3.txt"
import argparse

parser = argparse.ArgumentParser(description = "description goes here")
parser.add_argument("-n", type=int, help = "Write Natural Number. This option is required", required=True)
parser.add_argument("-f", type=str, help = "Write file name. This option is required", required=True)

args = parser.parse_args()
natural_number = args.n
file_name = open(args.f)
count = 1
for row in file_name:
    if count <= natural_number:
        print("{0}:{1}".format(count,row))
    count += 1
