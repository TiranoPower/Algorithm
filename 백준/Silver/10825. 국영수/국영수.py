import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())

user = [list(input().split()) for i in range(n)]
    
user.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for j in user:
    output(str(j[0]) + "\n")
    