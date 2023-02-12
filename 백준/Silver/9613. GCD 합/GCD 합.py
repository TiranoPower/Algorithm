from itertools import combinations

def gcd(x, y):	# 최대공약수 계산 함수
    while y:
        x, y = y, (x % y)
    return x

n = int(input())
lists = []
result = 0
for _ in range(n):
    lists = list(map(int, input().split()))	# 조합 만들 숫자들 받기
    lists = lists[::-1]	# 내림차순 정렬
    del lists[len(lists) - 1]	# 마지막 요소 필요 없으니 제거
    ncr = combinations(lists, 2)	# 조합 생성
    
    for i in ncr:
        result += gcd(i[0], i[1])	# 조합을 통해 최대공약수들 result에 더하기
    print(result)	# 프린트 해 두고
    result = 0	# 초기화