from queue import PriorityQueue
import sys

que = PriorityQueue()
size= int(sys.stdin.readline())
save=[]
cnt=0

for _ in range(size):
    tmp=list(map(int,sys.stdin.readline().split()))
    save.append(tmp)

save.sort()

for i in range(size):
    que.put(save[i][1])

    tmp=que.get()

    if que.qsize()!=0 and tmp > save[i][0]:
        que.put(tmp)
        cnt +=1

    elif que.qsize()==0:
        que.put(tmp)
        cnt +=1



print(cnt)