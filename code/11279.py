#최대 힙
import heapq
arr = []
n = int(input())

for i in range(n):
    x = int(input())
    
    if x == 0:
        if arr:
            print(-heapq.heappop(arr))
        else:
            print(0)
    
    else:
        heapq.heappush(arr,-x)

