TC=int(input())
for _ in range(TC):
    n=int(input())
    graph=[list(map(int,input().split())) for _ in range(2)]

    dp=[[0]*n for _ in range(2)]
    for i in range(n):
        if i==0:
            dp[0][i]=graph[0][0]
            dp[1][i]=graph[1][0]
        elif i==1:
            dp[0][1]=dp[1][0]+graph[0][1]
            dp[1][1]=dp[0][0]+graph[1][1]
        else:
            dp[0][i]=max(graph[0][i]+dp[1][i-1], max(dp[0][i-2],dp[1][i-2])+graph[0][i])
            dp[1][i]=max(graph[1][i]+dp[0][i-1], max(dp[0][i-2],dp[1][i-2])+graph[1][i])   
    
    if dp[0][n-1]>dp[1][n-1]:
        print(dp[0][n-1])
    else:
        print(dp[1][n-1])