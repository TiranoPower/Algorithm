import sys

n = sys.stdin.readline().strip()
arr = []

for i in range(len(n)):
    arr.append(n[i:])
    
arr.sort()   

for i in  arr :
    print(i)

# 문자열 오름차순 : 알파벳순
# 숫자 오름차순 : 오름차순



