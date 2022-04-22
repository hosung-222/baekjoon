# 케빈 베이컨의 6단계 법칙
from collections import deque


def bfs(num, n):
    bacon = [0]*(n+1)
    visited = [num]
    queue = deque()
    queue.append(num)
    while queue:
        k = queue.popleft()
        for i in cabin[k]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                bacon[i] = bacon[k] + 1
    return sum(bacon)




n, m = map(int,input().split())
cabin = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    cabin[a].append(b)
    cabin[b].append(a)

result = []

for num in range(1, n+1):
    result.append(bfs(num,n))

print(result.index(min(result))+1)


