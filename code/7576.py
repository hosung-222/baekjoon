#토마토
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0, 0 , -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >= n or ny< 0 or ny >= m:
                continue
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append([nx,ny])

#입력 받기
m ,n = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]

queue = deque([])
res = 0 #결과값 저장

for i in range(n): #익은 토마토 찾아서 큐에 추가
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

bfs()
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res,max(i))

print(res-1) #원래 토마토가 1이니 1을 빼준 값이 날짜


