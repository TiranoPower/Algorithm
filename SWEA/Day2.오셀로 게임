T = int(input())
for test_case in range(1, T+1):
  N,M = map(int, input().split()) # 한 변의 길이 : N
                                 # 돌을 놓는 횟수 : M
  array = [[0] * N for _ in range(N)] #  N의 길이까지 다 0으로 초기화
  
  direction  = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)] # 8가지 방향의 정의

  middle =  N//2 # 첫 시작 정의
  array[middle][middle] = 2 # 초기값 흰돌 정의(1)
  array[middle-1][middle-1] =  2  # 초기값 흰돌 정의(2)

  array[middle][middle-1] = 1 # 초기값 검은돌 정의(1)
  array[middle-1][middle] = 1 # 초기값 검은돌 정의(2)

  for _ in range(M) : # 오목돌 놓을때까지
    y, x, color = map(int, input().split()) # 문제 지문에 반대로 되있으므로 반대로 정의
    y -= 1  # 1부터 시작하므로 배열을 만들기 위하여 -1
    x -= 1  # 1부터 시작하므로 배열을 만들기 위하여 -1

    if not array[x][y] : # 입력값을 반대로 정의했으므로 if문 돌아감
      array[x][y] = color # 입력값 color로 지정
      for i in range(8) :  
        dx, dy = direction[i] # 방향 정의
        nx, ny = x + dx, y + dy # x좌표와 y 좌표에 방향을 더함
        reverse = []

        while True:
           if nx < 0 or N - 1 < nx or ny < 0 or N -1 < ny:
             reverse = [] # 질문
             break
           if array[nx][ny] == 0: # 빈칸을 만난 경우 초기화
             reverse = []
             break
           if array[nx][ny] == color:  ## 같은 색을 만났으므로
              break
           else:
              reverse.append((nx, ny))
           nx += dx
           ny += dy

        for rx, ry in reverse: # 바꾼값의 색 지정
           array[rx][ry] = color  

  W, B = 0, 0
  for i in range(N):
      for j in range(N):
        if array[i][j] == 1:
           W += 1
        elif array[i][j] == 2:
           B += 1

  print('#{} {} {}'.format(test_case, W, B))
    
    
    
    
    
    
    

  
   
