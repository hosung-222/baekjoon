#절대값 힙
import sys
import heapq
input = sys.stdin.readline

heap = []

n = int(input())
for i in range(n):
    x = int(input())
    
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    
    else:
        heapq.heappush(heap,(abs(x),x))