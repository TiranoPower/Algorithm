def solution(absolutes, signs):
    answer = 0
    
    for i in range (len(absolutes)) :
        if signs[i] : # signs[i]가 True이면
            answer += absolutes[i]  # 해당 인덱스의 absolutes 값 더함
#            print(answer) 
            
        else :  # signs[i]가 False면
            answer -= absolutes[i]  # 해당 인덱스의 absolutes 값을 뺌
        
    return answer


# 복습 필요