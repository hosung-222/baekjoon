# 2*n 타일링
n =  int(input())
sol = [0]*n


for i in range(1,n+1):
    if i == 1:
        sol[i-1] = 1
    elif i == 2:
        sol[i-1] = 2
    else:
        sol[i-1] = sol[i-2] + sol[i-3]
    

print(sol[-1])