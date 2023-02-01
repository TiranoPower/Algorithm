import math

n = int(input())

arr = [0,0,1,1]  # 0 1 2 3

for i in range(4, n+1):  # 4부터
    three, two, one = math.inf, math.inf, arr[i-1]
     
    if i % 3 == 0:
        three = arr[i // 3]
    
    if i % 2 == 0:
        two = arr[i // 2]
     
    value = 1 + min(three, two, one)
    arr.append(value)
    
print(arr[n])
        