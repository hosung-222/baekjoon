#나는야 포켓몬 마스터 이다솜

import sys

n, m = map(int,input().split()) #n:포켓몬갯수 m:문제갯수
pocketmon = {}
key = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    pocketmon[i] = name
    key[name] = i

for _ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit() == True:
        print(pocketmon[int(q)-1])
    else:
        print(key[q]+1)



