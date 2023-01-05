T = int(input()) # 테스트케이스의 횟수 입력

for i in range(1, T+1) :
    m = list(input()) # 복구해야 할 메모리의 값 입력
    answer = 0 # 변경횟수 초기값 설정
    flag = ['0'] * len(m) # 길이만큼 "0"로 flag 설정
    
    for j in range(len(m)) : # 이중 반복문
        if m[j] != flag[j] : # flag[j]와 m[j]이 다르면 k 반복문으로 
            for k in range(i, len(m)) :
                flag[k] = m[j]  # 길이만큼 m[j]의 값 복사 
            answer += 1 # 변경횟수를  1만큼 더함 

    print("#{} {}".format(i, answer)) # format : 각각의 테스트케이스에 대한 총 변경  출력
