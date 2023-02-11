import sys


input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
dic = {}


for i in range(n) :  # 카드 5장
    card = int(input())  # 5
    if card in dic:  # {2 : 1, 2 : 3} 
        dic[card] += 1
    else :
        dic[card] = 1

result = sorted(dic.items(), key = lambda x : (-x[1], x[0]))  ## 딕셔너리는 sorted함수


print(result[0][0])
