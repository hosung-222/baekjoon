#파도반 수열
import sys
input = sys.stdin.readline

pado = [0 for _ in range(101)]
for i in range(1,101):
    if i == 1:
        pado[i] = 1
    elif i == 2:
        pado[i] = 1
    elif i == 3:
        pado[i] = 1
    elif i == 4:
        pado[i] = 2
    elif i == 5:
        pado[i] = 2
    else:
        pado[i] = pado[i-1] + pado[i-5]

t = int(input())
for i in range(t):
    n = int(input())
    print(pado[n])
