import sys

n = sys.stdin.readline().strip()

alpha = [0] * 26

for j in n :
    alpha[ord(j)-97] += 1

print(*alpha)