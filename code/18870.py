#좌표압축
import sys
input = sys.stdin.readline

n = int(input())

a = [int(x) for x in input().split()]
set_a = set(a)
list_a = list(set_a)
list_a.sort()
dic = {list_a[i]: i for i in range(len(list_a))}


for i in a:
    print(dic[i],end=" ")