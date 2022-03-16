#괄호
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a = input()
    a = a.strip('\n')

    xcount = 0
    ycount = 0

    for i in a:
        if i == '(':
            xcount += 1
        elif i == ')':
            ycount += 1
        if xcount < ycount:
            print("NO")
            break

    if xcount == ycount:
        print("YES")
    elif xcount > ycount:
        print("NO")
