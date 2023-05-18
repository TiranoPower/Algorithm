def solution(arr):
    if len(arr) <= 1 : # 길이 1이하면
        return [-1] # -1 반환
    
    
    min_value = min(arr) # 제일 작은수 찾는 함수
    
    arr.remove(min_value)

    return arr

# 복습 필요