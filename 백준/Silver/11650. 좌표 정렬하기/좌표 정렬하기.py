import sys 

n = int(input())

num = []

for i in range(n):
    [x,y] = map(int, input().split())

    num.append([x,y])

answer = sorted(num)

for j in range(n):
    print(answer[j][0], answer[j][1])