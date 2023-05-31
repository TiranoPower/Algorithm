def solution(players, callings):
    idx = {i : player for i, player in enumerate(players)} # 등수 : 선수 딕셔너리
    p = {player : i for i, player in enumerate(players)} # 선수 : 등수 딕셔너리
    
    # print(idx)
    
    
    
    for i in callings :
        loc = p[i] # 현재 등수
        loc2 = loc - 1 # 앞 등수
        i2 = idx[loc2] # 앞 선수
        
    #print(loc) 
    #print(loc2)
    # print(i2)
    
        idx[loc] = i2 # 등수 : 선수 딕셔너리에서 현재 등수의 선수를 업
        idx[loc2] = i # 등수 : 선수 딕셔너리에서 현재 등수의 선수를 다운
    
        p[i] = loc2 # 선수 : 등수 딕셔너리에서 현재 선수의 등수를 현재 등수로 업
        p[i2] = loc # 선수 : 등수 딕셔너리에서 현재 선수의 등수를 현재 등수로 다운
        
    return list(idx.values())

# 복습 필요