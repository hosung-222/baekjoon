#종이의 개수
n = int(input())

paper = [list(map(int,input().split())) for _ in range(n)]

minues = 0
zero = 0
one = 0

def dfs(x,y,n):
    global minues, zero, one
    check = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != check:
                for k in range(3):
                    for l in range(3):
                        dfs(x +k*n//3, y+ l*n//3, n//3)
                return
    if check == -1:
        minues += 1
    elif check == 0:
        zero += 1
    elif check == 1:
        one += 1

dfs(0,0,n)
print('{}\n{}\n{}'.format(minues,zero,one))