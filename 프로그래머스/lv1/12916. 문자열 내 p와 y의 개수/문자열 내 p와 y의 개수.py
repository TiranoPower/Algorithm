def solution(s):
    
    s = s.lower() # 소문자로 만들기
    count_p = s.count('p') # p 개수 새기
    count_y = s.count('y') # y 개수 세기
    
    return count_p == count_y # 개수가 같으면 true, 틀리면 false


# 복습필요 