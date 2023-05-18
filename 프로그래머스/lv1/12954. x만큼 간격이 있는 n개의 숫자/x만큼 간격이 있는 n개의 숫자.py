def solution(x, n):
    answer = [] # 결과를 담을 배열
    current = x # 현재 값
    
    for i in range(n) : # n개까지
        answer.append(current) # 현재 값 추가
        current += x # 현재값에서 덧셈
    
    return answer