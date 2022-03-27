#덱
import sys
input = sys.stdin.readline
from collections import deque
a = []
deq = deque(a)

n = int(input())
for _ in range(n):
    c = input().split()
    if c[0] == 'push_front':
        deq.appendleft(c[1])
    elif c[0] == 'push_back':
        deq.append(c[1])
    elif c[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif c[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif c[0] == 'size':
        print(len(deq))
    elif c[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif c[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])

