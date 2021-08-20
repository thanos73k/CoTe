goal, city= map(int, input().split())
info=[]
INF=987654321
dp=[0] + [INF]* 2000

for _ in range(city):
    tmp =list( map(int,input().split()))
    info.append(tmp)


for cost, people in info:
    for i in range(people, goal + people):
        dp[i]= min(dp[i],dp[i-people]+cost)

print(min(dp[goal:]))

