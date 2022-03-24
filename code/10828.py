import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    do = input().split()
    if do[0] == 'push':
        a.append(do[1])
    elif do[0] == 'pop':
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop())
    elif do[0] == 'size':
        print(len(a))
    elif do[0] == 'empty':
        if len(a) == 0:
            print(1)
        else:
            print(0)

    elif do[0] == 'top':
        if len(a) == 0:
            print(-1)
        else:

            print(a[len(a)-1])