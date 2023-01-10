for tc in range(1, 11) : # 1부터 10까지의 테스트 케이스
  N, arr = input().split() # 문자열 개수, 문자열 값
  arr = list(arr) # 리스트로 설정
  
  s = 0 #
  while s < len(arr) : # 처음부터 끝까지 반복 수행
    if s and arr[s] == arr[s-1] : # 앞과 뒤의 문자열 비교
      del arr[s], arr[s-1]  # 같으면 앞과 뒤의 문자열 삭제
      s -= 1  # 앞으로 감
    else :  # 아니면 뒤로 감
     s += 1

  print(f'#{tc} {"".join(arr)}') # 테스트케이스 및 합친 문자열의 결과값 출력

