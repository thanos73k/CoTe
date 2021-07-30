import heapq

size=int(input())
save=[]

for _ in range(size):
    save.append(list(map(int,input().split())))

save.sort(key=lambda x:(x[1]))
real=[]

for i in save:
    heapq.heappush(real,i[0])
    if(i[1]<len(real)):
        heapq.heappop(real)

print(sum(real))