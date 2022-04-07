#hashing
#소문자 a의 아스키 코드 97
import sys
L = int(sys.stdin.readline())
s = input()
sum = 0
for i in range(L):
    sum += ((ord(s[i])-96)*(31**i))
print(sum  % 1234567891)
