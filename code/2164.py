#카드 2
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

n = deque(range(1,N+1))

def card(n):
    while len(n)>1:
        n.popleft()
        n.append(n.popleft())
    print(n[0])

card(n)

        



