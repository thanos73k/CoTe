h,w = map(int, input().split())

save=list(map(int,input().split()))

max=0
idx=0

for i in range(len(save)):
    if save[i]>max:
        max=save[i]
        idx=i

total=0
tmp=0
for i in range(idx+1):
    if save[i]> tmp:
        tmp= save[i]

    total += tmp

tmp=0
for i in range(w-1,idx,-1):
    if tmp < save[i]:
        tmp= save[i]

    total += tmp


print(total -  sum(save))