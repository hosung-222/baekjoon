# DSLR
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    q = deque()
    q.append((a,""))
    visit = [False]*10000

    while q:
        num, path = q.popleft()
        visit[num] = True
        if num == b:
            print(path)
            break

        num2 = (2*num)%10000
        if not visit[num2]:
            visit[num2] = True
            q.append((num2,path+"D"))

        num2 = (num-1)%10000
        if not visit[num2]:
            visit[num2] = True
            q.append((num2,path+'S'))

        num2 = (10*num+(num//1000))%10000
        if not visit[num2]:
            visit[num2] = True
            q.append((num2,path+'L'))

        num2 = (num//10+(num%10)*1000)%10000
        if not visit[num2]:
            visit[num2] = True
            q.append((num2,path+"R"))


