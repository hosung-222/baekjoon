#AC
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',') #괄호 제외하고 [1~-1]까지 ','제외 입력
    arr = deque(arr)

    r = 0  #reverse 횟수 계산

    if n == 0:
        arr = []
    
    for i in range(len(p)):
        if p[i] == 'R':
            r += 1 #매번 뒤집으면 시간초과 됨으로 r = 홀수일경우만 한번에 revers
        elif p[i] == 'D':
            if len(arr) == 0:
                print('error')
                break
            else:
                if r % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop() #뒤집기 전이니  뒤에서빼주면 같은 효과
        
    else:
        if r % 2== 0: #r = 짝수인 경우 뒤집을 필요 x
            print('['+",".join(arr)+"]")
        else: # r = 홀수인 경우 한번만 뒤집기
            arr.reverse()  #deque는 sort사용불가 하지만 reverse사용 가능
            print('['+",".join(arr)+"]")

  