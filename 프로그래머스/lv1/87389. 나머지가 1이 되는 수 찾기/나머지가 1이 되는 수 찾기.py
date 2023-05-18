def solution(n):
    x = 2
    while True: # 계속
        if n % x == 1: # 나머지가 1이라면
            return x # x를 반환
        x += 1 # x를 더함, while true 계속 실행
