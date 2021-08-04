n=int(input())
v=int(input())

graph = [[] for _ in range(n+1)]

for i in range(v):
  node, node2 = map(int, input().split())
  graph[node].append(node2)
  graph[node2].append(node)

check=[0]*(n+1)

def dfs(n):
    if check[n] == 0:
        check[n] = 1
        for j in graph[n]:
            dfs(j)

dfs(1)
print(sum(check)-1)
