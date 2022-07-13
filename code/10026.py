#적록색약
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q.append([x,y])
    visit[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx< n and 0<=ny< n:
                if color[nx][ny] == color[x][y] and visit[nx][ny] == 0:
                    q.append([nx,ny])
                    visit[nx][ny] = 1
                
n = int(input())
color = [list(input()) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
q = deque()

cnt = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i,j)
            cnt += 1
print(cnt,end='')

for i in range(n):
    for j in range(n):
        if color[i][j] == 'R':
            color[i][j] = 'G'
    
visit = [[0]*n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i,j)
            cnt += 1
        
print(cnt)