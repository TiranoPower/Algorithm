import math

def solution(n):
    answer = 0
    
    sqrt_n = math.isqrt(n) # n의 제곱근 계산
    
    if sqrt_n * sqrt_n  == n : # n의 양의 정수 x의 제곱인지 판별
        answer = (sqrt_n + 1) ** 2 # (x+1)의 제곱근 계산
        
    else :
        answer = -1
    
    return answer

# 복습 필요