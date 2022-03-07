#나이순 정렬
from operator import itemgetter
import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    age,name = input().split()
    a.append([int(age),name])

a = sorted(a,key = itemgetter(0))

for age,name in a:
    print(age,name)
