n = int(input())
dp = [[0] for _ in range(91)]

for i in range(1,3):
   dp[i] = 1


for i in range(3,n+1):
   dp[i] = dp[i-2] + dp[i-1]

print(dp[n])
