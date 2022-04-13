#유기농 배추
t = int(input())
dx = [1,-1,0,0] #x축이동
dy = [0,0,-1,1] #y축이동

def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4): #좌우상하 검색
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and land[q][w] == 1: #땅을 안벗어나고 배추가 심어져있을때
                land[q][w] = 0 #0으로 바꿔줌
                queue.append([q, w])

for _ in range(t):
    m, n, k = map(int,input().split())
    land = [[0]*m for _ in range(n)]
    count = 0
    print(land)
    for _ in range(k):
        a, b = map(int,input().split())
        land[b][a] = 1

    for j in range(n):
        for k in range(m):
            if land[j][k] == 1:
                bfs(j,k)
                land[j][k] = 0
                count += 1
    
    print(count)

