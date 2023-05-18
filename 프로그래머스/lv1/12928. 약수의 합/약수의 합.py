def solution(n):
    answer = 0
    
    for i in range (1, n+1) : # n까지
        if n % i == 0 : # 나머지가 0 이되는 것들을
            answer += i # 더한다
    return answer