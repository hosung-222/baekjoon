#랜선 자르기
import sys
input = sys.stdin.readline

k, n = map(int,input().split())
l = []
for i in range(k):
    lan = int(input())
    l.append(lan)

start, end = 1, max(l)

while start <= end:
    mid = (start+end)//2
    lines = 0
    for i in l:
        lines += i //mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)