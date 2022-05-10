#숨박꼭질
from collections import deque

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:               #원하는 값일경우 출력후 탈출
            print(distance[x])
            break
        for i in (x-1,x+1,2*x):  #3가지 옵션 탐색
            if 0<= i <= max and not distance[i]:
                distance[i] = distance[x]+1
                queue.append(i)

        
n,k = map(int,input().split())
max = 10 ** 5
distance = [0] * (max+1)
bfs()