def solution(arr):
    answer = [] # 빈 배열
    # print(arr) 1 1 3 3 0 1 
    for i in arr : # 1 1 3 3 0 1  
        if answer[-1:] == [i] : continue
        answer.append(i)
    
    return answer