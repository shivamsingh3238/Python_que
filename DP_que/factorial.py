def recursion(x):
    if x==0:
        return 1
    if (dp[x]!= -1):
        return dp[x]
    
    return(dp[x] = x * recursion(x-1))



n=int(input())
dp=[0]*n
result=recursion(n)
print(dp)
