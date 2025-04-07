def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    if n >= 2:
        dp[2] = 2

    # 마지막에 세로로 1개 두는 경우 -> 한 자리가 비워져 있어야 함
    # 마지막에 가로로 2개 두는 경우 -> 두 자리가 비워져 있어야 힘
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

    return dp[n]