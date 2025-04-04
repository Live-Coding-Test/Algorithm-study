"""
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5
dp[5] = dp[n-1] + dp[n-2]
"""

def solution(n):
    
    dp = [0] * (n + 1)
    
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007

    return dp[n]