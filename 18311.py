n, k=map(int, input().split())
point=list(map(int, input().split()))

sum=0
cnt=0
check=False

for i in point:
    sum += i
    cnt+=1

    if sum>k:
        print(cnt)
        check=True
        break
if check==False:
    tmp=k-sum

    sum=0
    cnt = len(point)+1
    for i in reversed(point):
        sum += i
        cnt -= 1

        if sum>tmp:
            print(cnt)
            break
