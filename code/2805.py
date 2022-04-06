#나무 자르기
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

tree = list(map(int,input().split()))

start = 1
last = max(tree)
while start <= last:
    
    mid = (start+last) //2
    count = 0
    for i in tree:
        if i > mid:
            count += (i - mid)


    if count >= m:
        start = mid+1
    
    else:
        last = mid-1

print(last)





