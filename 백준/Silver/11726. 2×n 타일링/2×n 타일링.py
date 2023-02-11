n = int(input())

x = [0] * 1001

x[1] = 1
x[2] = 2

for i in range(3, 1001):
    x[i] = (x[i-1] + x[i-2]) % 10007 
    
print(x[n])
    
    