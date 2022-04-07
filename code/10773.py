#제로
k = int(input())

stack =[]

for _ in range(k):
    m = int(input())
    if m == 0 :
        stack.pop()
    
    else:
        stack.append(m)

sum = 0
for i in stack:
    sum += i
print(sum)
