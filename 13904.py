import heapq

size=int(input())
save=[]

for _ in range(size):
    save.append(list(map(int,input().split())))

save.sort(key=lambda x: (x[0]))

real=[]

for i in save:
    heapq.heappush(real,i[1])

    if(len(real)>i[0]):
        heapq.heappop(real)

print(sum(real))

