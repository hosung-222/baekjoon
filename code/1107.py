#리모컨
target = int(input())
ans = abs(100-target) # + or -로만 이동할때 (최대값)
m = int(input())
if m: #고장난게 있을경우에만 input 실행
    b = set(input().split())
else:
    b = set()

for num in range(1000001):
    for n in str(num):
        if n in b: #눌러서 만들수 없는 숫자 포함이면 종료
            break
    else:
        #기존값과 버튼을 누르고 + - 버튼으로 간 횟수중 최솟값
        ans = min(ans, len(str(num))+abs(num - target))

print(ans)

