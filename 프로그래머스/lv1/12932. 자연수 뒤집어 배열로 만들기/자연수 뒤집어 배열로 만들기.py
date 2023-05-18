def solution(n):
    answer = []
    
    while n > 0 : # 0보다 클때까지
        answer.append(n % 10)  # 나머지를 추가
        n //= 10 # 남은 몫으로 계산 
        
    
    return answer

# 복습 필요