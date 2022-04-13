#피보나치 함수
import sys
input = sys.stdin.readline

# def fibonacci(n):
#     global zcount, ocount
#     if n==0:
#         # print(0)
#         zcount += 1
#         return 0
        
#     elif n == 1:
#         # print(1)
#         ocount += 1
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# t = int(input())

# for _ in range(t):
#     zcount = 0
#     ocount = 0
#     fibonacci(int(input()))
#     print(zcount,ocount)


#new code


t = int(input())

for _ in range(t):
    f0 = [1,0]
    f1 = [0,1]
    n = int(input())
    if n>1:
        for i in range(n-1):
            f0.append(f1[-1])
            f1.append(f0[-2]+f1[-1])
         
    print(f0[n],f1[n])
