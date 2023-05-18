def solution(n):
    digits = list(str(n))  # n을 문자열로 반환 후 각 자릿수를 리스트에 저장
    
    # print(digits) [1,1,8,3,7,2]
    digits.sort(reverse = True) # 내림차순으로 정렬
    
    # print(digits) [8,7,3,2,1,1]
    
    sorted_n = ''.join(digits) # 결합
    
    # print(sorted_n) # 873211(str형)
    
    return (int(sorted_n))
    
    
    