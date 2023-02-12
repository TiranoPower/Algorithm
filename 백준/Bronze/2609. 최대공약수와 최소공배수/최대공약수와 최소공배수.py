def gcd(a,b) :
    while b :
        a, b = b, a % b ## 최대공약수
    
    return a 

def lcm(a, b) :
    return a * b // gcd(a,b)


a,b = map(int, input().split())

print(gcd(a,b))
print(lcm(a,b))