#회의실 배정
import sys
input = sys.stdin.readline

n = int(input())

time = [[0]*2 for _ in range(n)]
for i in range(n):
    x, y = map(int,input().split())
    time[i][0] = x
    time[i][1] = y

time.sort(key= lambda x: x[0]) #시작시간순으로 정렬
time.sort(key= lambda x : x[1]) # 끝나는 시간순으로 정렬

cnt = 0
endTime = 0

for i , j in time:
    if i>= endTime:
        cnt += 1
        endTime = j

print(cnt)



