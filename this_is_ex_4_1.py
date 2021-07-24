size=int(input())
save =input().split()
x,y = 1,1

dx=[0,0,-1,1]
dy=[-1,1,0,0]

m_type=['L','R','U','D']

for i in range(len(save)):

    for j in range(4):
        if save[i]==m_type[j]:
            nx=x +dx[j]
            ny=y +dy[j]

    if nx<1 or ny<1 or nx>size or ny>size:
            continue
    x,y = nx, ny

print(x,y)