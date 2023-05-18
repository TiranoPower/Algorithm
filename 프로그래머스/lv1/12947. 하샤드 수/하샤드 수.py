def solution(x):
    
    digits = list(str(x))
    
    # print(digits) # [1, 2]...
    
    digit_sum = sum(map(int, digits))
    
    # print(digit_sum) # 3 ...
    
    if x % digit_sum == 0 :
        return True
    
    else : 
        return False
        