#구간 합 구하기
import sys
input = sys.stdin.readline


n, m = map(int,input().split())
num = list(map(int,input().split()))

sum_list = [0]
total = 0
for i in range(len(num)):
    total += num[i]
    sum_list.append(total)

for i in range(m):
    sum = 0
    x,y = map(int,input().split())
    print(sum_list[y] - sum_list[x-1])
