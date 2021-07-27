n,k = map(int, input().split())
save=[]
cnt=0

for _ in range(n):
    save.append(int(input()))

save.sort(reverse=True)

for i in range(n):
    tmp = k//save[i]

    if tmp !=0:
        k -= save[i]*tmp
        cnt += tmp

print(cnt)