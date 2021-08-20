size= int(input())

save=list(map(int,input().split()))

total= int(input())



start, end = 0, max(save)

while start <= end:
    mid = (start + end)//2
    sum = 0

    for i in save:
        if i >=mid:
            sum +=mid
        else:
            sum +=i

    if sum <= total:
        start= mid+1

    else:
        end=mid-1

print(end)
