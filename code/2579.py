#계단오르기
import sys
input = sys.stdin.readline

n = int(input())
score = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(n):
    score[i] = int(input())

dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[1]+score[2], score[0]+score[2])

for i in range(3,n):
    dp[i] = max(score[i]+score[i-1]+dp[i-3], score[i]+dp[i-2])

print(dp[n-1])
