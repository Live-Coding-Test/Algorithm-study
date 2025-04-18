"""
중복순열 시간 초과 . . . 
dp[k][n] = dp[k-1][0] + dp[k-1][1] + ... + dp[k-1][n]
dp[k][n] = dp[k-1][n] + dp[k][n-1]
"""

import sys
from itertools import *

input = sys.stdin.readline
n, k = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(k + 1)]

# n이 무엇이든 k=1개로 만들 수 있는 개수는 1개
for i in range(n + 1):
    dp[1][i] = 1

for i in range(2, k + 1):
    for j in range(n + 1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[k][n])