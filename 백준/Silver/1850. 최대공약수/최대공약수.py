def gcd(a,b) :
    while b :
        a, b = b, a % b ## 최대공약수
    
    return a 

A,B = map(int, input().split())

print('1' * gcd(A,B))