n, k =map(int, input().split())

save=[]
dp=[0]*(k+1)

for _ in range(n):
    save.append(int(input()))

for value in save:
    for i in range(value, k + 1):
        if i-value==0:
            dp[i]+=1

        if dp[i-value]!=0:
            dp[i] += dp[i-value]

print(dp[k])