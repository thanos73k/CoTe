size = int(input())
save=[]
sum=0

for _ in range(size):
    save.append(int(input()))

save.sort(reverse=True)

for i in range(size):
    tmp= (save[i]-i)
    if tmp>0:
        sum += tmp


print(sum)
