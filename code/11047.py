#동전 0
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
i = -1
cnt = 0
while True:
    if coin[i] == k:
        print(cnt+1)
        break
    elif coin[i] < k:
        k -= coin[i]
        i = 0
        cnt += 1
    i -= 1


