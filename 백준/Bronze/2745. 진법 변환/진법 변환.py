N, B  = input().split()
N = ''.join(reversed(N))
B = int(B)

result = 0

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for  i in range(len(N)-1,-1,-1):
    sum = number.index(N[i]) * (B**i)  ## index : 인덱스값 찾기
    result +=sum

print(result)

# 복습 필요 