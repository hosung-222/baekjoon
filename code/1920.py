import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int,input().split()))

m = int(input())
ain = list(map(int,input().split()))

for i in ain:
    if i in a:
        print(1)
    else:
        print(0)