 



# #dfs
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# def dfs(x,y):
#     if x<0 or x>=n or y<0 or y>=n:
#         return False
#     if apt[x][y] == 1:
#         global count
#         count += 1
#         apt[x][y] == 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx,ny)
#         return True
#     return False

# num = []
# n = int(input())
# apt = []
# for i in range(n):
#     apt.append(list(map(int,input())))

# count = 0
# result = 0 
# for i in range(n):
#     for j in range(n):
#         apt[i][j] = 1
#         num.append(dfs(i,j))
#         result += 1

# print(len(cnt))
# for i in range(len(cnt)):
#     print(cnt[i])