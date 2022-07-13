#패션왕 신해빈
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    clo = {}
    for _ in range(n):
        wear = list(input().split())
        if wear[1] in clo:
            clo[wear[1]].append(wear[0])
        else:
            clo[wear[1]] = [wear[0]]

    cnt = 1
    for k in clo:
        cnt *=(len(clo[k])+1)

    print(cnt-1)