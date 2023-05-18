def solution(s):
    length = len(s) # 단어의 길이 구하기
    
    mid = length // 2 # 가운데 인덱스 계산
    
    #print(mid)
    
    if length % 2 == 0 : #단어의길이가 짝수면
        return s[mid-1:mid+1]
    
    else : # 홀수면
        return s[mid]
    


# 복습 필요