def solution(s):
    answer = ''
    new_list = s.split(' ')
    #print(new_list) 
    for i in new_list:
       # print(i)
        for j in range(len(i)) :
            if j % 2 == 0 : # 짝수면
                answer += i[j].upper()
            else :
                answer += i[j].lower()
        answer += ' '
    return answer[0:-1]