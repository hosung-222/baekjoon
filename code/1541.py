#잃어버린 괄호

m = input().split('-')

num = []

for i in m:
    cnt = 0
    s = i.split("+")
    for j in s:
        cnt += int(j)
    num.append(cnt)
sum = num[0]

for i in range(1,len(num)):
    sum -= num[i]
print(sum)
