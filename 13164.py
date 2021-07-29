from queue import PriorityQueue

n,k =map(int,input().split())
save=list(map(int,input().split()))
diff=[]
sol=0

que = PriorityQueue()

for i in range(n-1):
    que.put(save[i+1]-save[i])

for i in range(n-k):
    sol+=que.get()


print(sol)