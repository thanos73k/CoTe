save=[]
n, m=map(int, input().split())
bulb=list(map(int, input().split()))

for i in range(m):
    value=list(map(int,input().split()))
    save.append(value)

for i in range(m):
    if save[i][0]==1:
        bulb[save[i][1]-1]= save[i][2]

    elif save[i][0] == 2:
        for j in range(int(save[i][1])-1,int(save[i][2])):
            if bulb[j]==0:
                bulb[j]=1
            else:
                bulb[j]=0

    elif save[i][0] == 3:
        for j in range(int(save[i][1])-1, int(save[i][2])):
            bulb[j]=0


    elif save[i][0] == 4:
        for j in range(int(save[i][1])-1, int(save[i][2])):
            bulb[j]=1

for i in range (0, n):
    print(bulb[i], end = ' ')