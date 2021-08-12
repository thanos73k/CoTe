size= int(input())
save=[]
dp = [1]*size

save=list(map(int,input().split()))

for i in range(size):
    for j in range(0,i):
        if save[i] > save[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))