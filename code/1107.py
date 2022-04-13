#리모컨
target = int(input())
ans = abs(100-target)
m = int(input())
if m:
    b = set(input().split())
else:
    b = set()

for num in range(1000001):
    for n in str(num):
        if n in b:
            break
    
    ans = min(ans, len(str(num))+abs(num - target))

print(ans)

