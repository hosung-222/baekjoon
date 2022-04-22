#DFS 와 BFS
from collections import deque
import sys
input = sys.stdin.readline
def dfs(v):
    print(v, end = ' ')
    visit[v] = True
    for i in graph[v]:
        if visit[i] == False:
            dfs(i)

def bfs(n):
    visit[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True


n, m , v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, n+1):
    graph[i].sort()


visit = [False] * (n+1)
dfs(v)
print()
visit = [False] * (n+1)
bfs(v)