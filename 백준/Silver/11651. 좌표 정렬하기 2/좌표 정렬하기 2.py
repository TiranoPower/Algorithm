import sys


input = sys.stdin.readline

n = int(input())

num = []

for i in range(n):
    [x,y] = map(int, input().split())

    num.append([y,x])

answer = sorted(num)

for j in range(n):
    print(answer[j][1], answer[j][0])