#카잉 달력

t = int(input())

for _ in range(t):
    m,n,x,y = map(int,input().split())
    f = 1
    while x <= m*n:
        if (x-y)%n == 0:
            print(x)
            f = 0
            break
        x += m
    
    if f:
        print(-1)
        

        