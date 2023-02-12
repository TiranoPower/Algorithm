def gcd(a,b):
     while b:
        a,b = b, a % b

     return a

def lcm(a,b):
    
    return a * b // gcd(a,b)

T = int(input())


for i in range(T):
    n,k = map(int, input().split())
    print(lcm(n,k))