t = int(input()) ## 테스트케이스 초기화

zero  = ['C', 'E', 'F', 'G', 'H', 'I','J','K','L','M','N','S','T','U','V','W','X','Y','Z'] # 구멍 안난 횟수의 'zero' 리스트 저장 
one = ['A','D','O','P','Q','R'] # one의 구멍 1개 난 횟수의  'one' 리스트 저장 

for tc in range (1, t+1) : # 테스트케이스 1부터 입력한 값까지
  str1, str2 = input().split()  # 비교할 문자열 두개 입력
  arr1 = [] ## 첫번째의 리스트 초기화
  arr2 = [] ## 두번째의 리스트 초기화

  for i in str1: 
   arr1.append(i) # 입력한 문자열 첫번째 리스트에 추가

  for j in str2:
     arr2.append(j)  # 입력한 문자열 두번째 리스트에 추가

  for k in range(len(arr1)):  # 첫번째 리스트 끝까지
    if arr1[k] not in zero:  # 만약 zero 리스트에 일치되는 값이 없다면 '1'값 저장
      arr1[k] = 1        
    else : 
         arr1[k] = 0  # 있다면 '0'값 저장

  for a in range(len(arr2)): # 두번째 리스트 끝까지
    if arr2[a] not in zero :  # 만약 zero 리스트에 일치되는 값이 없다면 '1'값 저장
      arr2[a] = 1
    else : 
      arr2[a] = 0 # 있다면 '0'값 저장
       
  if arr1 != arr2:
      print("#{} DIFF".format(tc))   # 만약 첫번째 리스트와 두번째 리스트의 값이 다르면 'DIFF' 출력
  else : 
      print("#{} SAME".format(tc))   # 아니면 'SAME' 출력
  
