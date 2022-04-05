#프린터 큐
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    imp = deque(map(int, input().split()))
    idx = deque(range(n))
    idx[m] = 'target'
    

    order = 0

    while True:
        if imp[0] == max(imp):
            order += 1
        
            if idx[0] == 'target':
                print(order)
                break
            else:
                imp.popleft()
                idx.popleft()
        else:
            imp.append(imp.popleft())
            idx.append(idx.popleft())