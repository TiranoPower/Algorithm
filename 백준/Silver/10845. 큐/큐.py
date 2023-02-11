import sys

input = sys.stdin.readline

Que = []
n = int(input())

for i in range(n):
    command = input().split()

    if command[0] == 'push' : Que.append(command[1])

    elif command[0] == 'pop' :
        if Que : print(Que.pop((0)))
        
        else: print(-1)

    elif command[0] == 'size' : print(len(Que))

    elif command[0] == 'empty' :
        if len(Que) == 0: print(1)

        else : print(0)

    elif command[0] == 'front':
        if len(Que) == 0 :  print(-1)

        else : print(Que[0])

    elif command[0] == 'back' :
        if len(Que) == 0 : print(-1)

        else : print(Que[-1])

    
