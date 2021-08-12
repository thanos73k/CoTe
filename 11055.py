size= int(input())
save=[]
save=list(map(int,input().split()))
dp = [save[0]]+[0]*(size-1)

for i in range(size):
    for j in range(0,i):
        if save[i] > save[j]:
            dp[i]=max(dp[i],dp[j]+save[i])

    if dp[i]==0:
        dp[i] = save[i]
print(max(dp))