#미로 탐색
from collections import deque

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx>=n or ny<0 or ny >= m:
                continue

            if miro[nx][ny] == 0:
                continue

            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx,ny))

    return miro[n-1][m-1]


n, m = map(int,input().split())

miro = [list(map(int,input())) for _ in range(n)]
print(bfs(0,0))
