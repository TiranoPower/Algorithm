def solution(arr, divisor):
    
    result = []
    
    
    for num in arr :
        if num % divisor == 0 : # divisor 가 num을 나눴을때 나머지가 0이면 
            result.append(num) # result에 담기
            
    #   print(num)
    #   print(result)
    
    if len(result) == 0 :
        return [-1]
    
    else :
        return sorted(result) # 오름차순
    

        
        
    



# 복습 필요