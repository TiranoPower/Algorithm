def solution(number):
    answer = 0
    l = len(number) # number의 길이
    
    for i in range(l): # 첫번째 숫자
        for j in range(i+1,l) : #두번째 숫자
            for k in range(j+1,l): # 세번째 숫자
                if number[i] + number[j] + number[k] == 0 : # 0이 되면
                    answer +=1 # answer에 count 더하기
    return answer 
    