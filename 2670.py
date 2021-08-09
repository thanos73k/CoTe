size=int(input())
save=[]

for _ in range(size):
    save.append(float(input()))

for i in range(1,size):
    save[i]= max(save[i-1]*save[i],save[i])

print("{:.3f}".format(max(save)))
