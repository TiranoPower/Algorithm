def solution(d, budget):
    d.sort()
    # print(d) 오름차순
    while budget < sum(d) : # 9 < 15 = [1,2,3,4] 9 < 10 = [1,2,3]
        d.pop()
        
    return(len(d))
    
    