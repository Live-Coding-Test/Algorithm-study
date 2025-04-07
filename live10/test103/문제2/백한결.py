def main():
    N = int(input())

    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(1, N+1):
        if i >= 3 and dp[i - 3] != float('inf'):
            dp[i] = min(dp[i], dp[i - 3] + 1)
        if i >= 5 and dp[i - 5] != float('inf'):
            dp[i] = min(dp[i], dp[i - 5] + 1)

    if dp[N] == float('inf'):
        dp[N] = -1

    print(dp[N])


if __name__ == "__main__":
    main()