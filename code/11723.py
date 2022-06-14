#집합
import sys
input = sys.stdin.readline

s = set() #중복 허용 x
m = int(input())
for _ in range(m):
    x = input().strip().split()

    if len(x) == 1:
        if x[0] == 'all':
            s = set([i for i in range(1,21)])
        else:
            s = set()
        continue

    menu = x[0]
    num = int(x[1])
    if menu == 'add':
        s.add(num)
    elif menu == 'remove':
        s.discard(num) #discard 사용시 num이 s에 없어도 오류 x
    elif menu == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    elif menu == 'toggle':
        if num in s:
            s.discard(num)
        else:
            s.add(num)
    