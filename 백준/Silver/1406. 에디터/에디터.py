import sys


stack_1 = list(sys.stdin.readline().rstrip()) 
stack_2 = [] 

n = len(stack_1)
m = int(input()) 
                               
for i in range(m): 
    command = sys.stdin.readline().split()
    if command[0] == "L" and stack_1:  
        stack_2.append(stack_1.pop())  

    elif command[0] == "D" and stack_2:
        stack_1.append(stack_2.pop())

    elif command[0] == "B" and stack_1:
        stack_1.pop()

    elif command[0] == "P" :  # (1) [a, b, c, d] []  (2) [a,b,c,d,y] [x],
        stack_1.append(command[1]) 

print("".join(stack_1+list(reversed(stack_2))))

# list(reversed) => 이중리스트 되는거 아님, 통째로 외우기
# 문자열.join() 합치기
