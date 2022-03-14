#N과 M(1)
import sys
input = sys.stdin.readline

n, m = list(map(int,input().split()))


def backtraking (s):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(i,n+1):
        if i in s:
            continue
        backtraking(s+[i])
backtraking([])