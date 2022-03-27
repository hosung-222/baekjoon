#요세푸스 문제 0

# from collections import deque
# n, k = map(int, input().split())
# s = deque([])
# for i in range(1, n + 1):
#     s.append(i)
# print('<', end='')

# while s:
#     for i in range(k - 1): 
#         s.append(s[0])  #맨 앞의 수를 맨뒤로 옮김
#         s.popleft()     #옮긴수 삭제
#     print(s.popleft(), end='') #제거해야하는 위치가 제일 앞으로와있는상태임으로 삭제
#     if s:               #요소가 있으면 ,를 붙여준다
#         print(', ', end='')
# print('>')





import sys
input  = sys.stdin.readline

n, k = map(int,input().split())
x = k
a = [i for i in range(1,n+1)]
y = []
print("<",end='')
while True:
    
    if len(a) == 1:
        print(a[0],end='')
        break
    if k != len(a)*2 and k!=len(a)*3:
        if k> len(a):
            k = k % len(a)
    else:
        k = len(a)

    print(a.pop(k-1), end =', ')
    k = k-1+x

print(">")
