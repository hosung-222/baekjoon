#쿼드 트리
n = int(input())
tree = [list(map(int,input())) for _ in range(n)]

def quadtree(x,y,n):
    if n == 1:
        return str(tree[x][y]) #x: 세로 y: 가로
    result = []
    for i in range(x, x+n):
        for j in range(y, y+n):
            if (tree[i][j] != tree[x][y]): #모두 같은수가 아닐시 4등분
                result.append('(')
                result.extend(quadtree(x, y, n//2)) #왼쪽 위 
                result.extend(quadtree(x, y+n//2, n//2))# 오른쪽 위
                result.extend(quadtree(x+n//2, y ,n//2))#왼쪽 아래
                result.extend(quadtree(x + n//2 , y+ n//2 ,n//2))# 오른쪽 아래
                result.append(')')

                return result
            
    return str(tree[x][y])

print(''.join(quadtree(0, 0, n)))
 