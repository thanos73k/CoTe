from queue import PriorityQueue

n=int(input())
k=int(input())

lst=list(map(int,input().split()))

que=PriorityQueue()
sol=0

tmp=set(lst)
lst=list(tmp)
lst.sort()

for i in range(len(lst)-1):
    que.put(lst[i+1]-lst[i])

for _ in range(len(lst)-k):
    sol += que.get()

print(sol)
