size= int(input())

save= list(map(int,input().split()))

save.sort()

sol=save[size-1]

for i in range(size-1):
    sol += (save[i]/2)

print( "%g" %(sol))