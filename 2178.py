n, m = map(int, input().split())
save= []
queue=[]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    save.append(list(input()))

save[0][0] = 1
queue=[[0,0]]

while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and save[x][y] == "1":
            queue.append([x, y])
            save[x][y] = save[a][b] + 1
print(save[n - 1][m - 1])
