a,b = map(int, input().split())
cnt=0

while True:

    if a >= b:
        cnt = -1
        break
    elif b%2 ==0:
        b= b//2
        cnt +=1
        if a == b:
            break

        continue

    elif str(b)[len(str(b))-1] =='1':

        tmp= str(b)[:len(str(b))-1]
        b=int(tmp)
        cnt +=1

        if a == b:
            break
        continue
    else:
        cnt = -1
        break

if cnt != -1:
    print(cnt+1)
else:
    print(cnt)