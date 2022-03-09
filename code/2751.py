#수정렬하기 2
import sys
input = sys.stdin.readline
n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)

numbers.sort()

for i in numbers:
    print(i)
