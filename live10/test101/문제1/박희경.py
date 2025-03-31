"""
dp[1] = 1
dp[2] = 2 (1+1, 2)
dp[3] = 4 (1+1+1, 1+2(*2), 3)
dp[4] = 7
dp[5] = 13
dp[6] = 24
dp[7] = 44
dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
"""
import sys

input = sys.stdin.readline


dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])

