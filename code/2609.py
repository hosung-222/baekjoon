from math import gcd

a, b = map(int,input().split())

print(gcd(a,b))
print(a*b // gcd(a,b))


# a, b = map(int,input().split())

# def gcd(a,b):
#     while b:
#         a, b = b, a%b b
#     return a

