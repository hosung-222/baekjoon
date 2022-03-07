import sys
input = sys.stdin.readline

n = int(input())

array = []

for i in range(n):
    x = input()
    if [len(x),x] not in array:
        array.append([len(x),x])

array.sort()
for i,x in array:
    print(x,end='')
