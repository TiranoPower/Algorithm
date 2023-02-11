import sys

input = sys.stdin.readline
output = sys.stdout.write  # 문자열때만 사용

n,k = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

print(array[k-1])