T = int(input())

for i in range(1, T+1) :
    m = list(input())

    answer = 0
    flag = ['0'] * len(m) # 길이만큼 "0" 출력
    for j in range(len(m)) : 
        if m[j] != flag[j] : # flag[j]와 m[j]이 다르면 k 반복문으로 
            for k in range(i, len(m)) :
                flag[k] = m[j]  # 길이만큼 m[j]의 값 복사 
            answer += 1 # 변경횟수값 1만큼 더함 

    print("#{} {}".format(i, answer)) # format : 각각의 i 및 answer 값 출력
