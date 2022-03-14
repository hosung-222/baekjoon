from math import factorial
n, k = map(int,input().split())


    

if k < 0 or k > n:
    print(0)

elif 0 <= k <= n:
    print(factorial(n) // (factorial(k)*(factorial(n-k))) )
