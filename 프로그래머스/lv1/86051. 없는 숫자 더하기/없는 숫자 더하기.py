def solution(numbers):
    answer = 0
    
    check = [False] * 10 # 0부터 9까지 check
    
    for num in numbers : # numbers 배열 순회
        check[num] = True # 숫자 체크
        
       #  print(check[num]) 
        
    for i in range(10) :
        if not check[i] :
            answer += i
        
    return answer

# 복습 필요
        
        
        
