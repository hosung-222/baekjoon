#숫자 카드2

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
dic1 = dict()

for i in a:
    if i in dic1:
        dic1[i] += 1
    else:
        dic1[i] = 1


m = int(input())
b = list(map(int,input().split()))

for i in b:
    if i in dic1:
        print(dic1[i],end=' ')
    else:
        print(0, end=' ')



