from queue import PriorityQueue
import sys
size=int(sys.stdin.readline())
sol=0

que = PriorityQueue()

for _ in range(size):
    que.put(int(sys.stdin.readline()))

while 1:
    if que.qsize() == 1:
        break

    tmp1=que.get()
    tmp2=que.get()

    sol +=( tmp1+ tmp2)

    que.put(tmp1 + tmp2)

print(sol)