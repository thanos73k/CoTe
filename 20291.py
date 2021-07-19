n=int(input())
file=[]
save={}

for i in range(n):
    file.append(input())


for i in range(len(file)):
    ext=file[i].split('.')[1]
    if (ext in save)==False:
        save[ext]=1
    else:
        tmp=save[ext]
        tmp+=1
        save[ext]=tmp

ssave=sorted(save.items())

for key,value in ssave:
    print(key,value)