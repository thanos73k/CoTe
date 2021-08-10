num=int(input())
save=[]
dp=[1]*num

for _ in range(num):
    save.append(int(input()))

for i in range(num):
    for j in range(i):
        if save[i] > save[j]:
            dp[i] = max(dp[i], dp[j]+1)


lis = max(dp)
print(num-lis)
