import sys

n = int(input())

user = []

for i in range(n) :
    user.append(list(input().split()))

user.sort(key = lambda a :int(a[0]))  # []의 []값 [0]번째

for i in range(n) :
    print(user[i][0], user[i][1])