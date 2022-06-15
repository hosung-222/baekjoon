#연결 요소의 개수
import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

#dfs풀이
def dfs(x):
    visited[x] = True

    for i in c[x]:
        if not visited[i]:
            dfs(i)


n, m = map(int,input().split())
c = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    u, v = map(int,input().split())
    c[u].append(v)
    c[v].append(u)

cnt = 0

for i in range(1,n+1):
    if not visited[i]:
        if not c[i]:
            cnt += 1
        
        else: 
            dfs(i)
            cnt += 1

print(cnt)

#bfs풀이
from collections import deque
def bfs(n):
    queue = deque([n])
    visited[x] = True

    while queue:
        x = queue.popleft()
        for i in g[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

n,m = map(int,input().split())
c = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(n):
    u,v = map(int,input().split())
    c[u].append(v)
    c[v].append(u)

cnt = 0

for i in range(1,n+1):
    if not visited[i]:
        if not c[i]:
            cnt += 1

        else:
            cnt += 1
            bfs(i)
    
print(cnt)