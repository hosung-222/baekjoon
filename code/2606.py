#바이러스

#dfs이용
def dfs(com, x):
    global cnt
    visited[x] = True
    
    for i in com[x]:
        if visited[i] == False:
            dfs(com,i)
            cnt += 1    
    return True
    


n = int(input())
c = int(input())
cnt = 0
com = [[] for _ in range(n+1)]

for _ in range(c):
    x, y  = map(int,input().split())
    com[x].append(y)
    com[y].append(x)

visited = [False] * (n+1)

dfs(com,1)
print(cnt)


# # bfs 이용
# from collections import deque

# def bfs(com, x):
#     cnt = 0
#     queue = deque()
#     queue.append(x)
#     while queue:
#         x = queue.popleft()
#         visted[x] = True

#         for i in com[x]:
#             if visted[i] == False:
#                 queue.append(i)
#                 visted[i] = True
#                 cnt += 1
#     print(cnt) 

# n = int(input())
# c = int(input())

# com = [[] for _ in range(n+1)]


# for _ in range(c):
#     x, y  = map(int,input().split())
#     com[x].append(y)
#     com[y].append(x)

# visted = [False]*(n+1)
# bfs(com , 1)


