#듣보잡
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
hear = {}
result = []
for i in range(n):
    name = input()
    hear[name] = i

for i in range(m):
    name = input()
    if name in hear:
        result.append(name)
    
result.sort()
print(len(result))
for i in result:
    print(i,end = '')