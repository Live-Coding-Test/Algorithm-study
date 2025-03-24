import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

i = 1
dp = [0] * (n + 1)
dp[0] = 1

while m > 0 or i <= n:
    # print(i, m, dp)
    if dp[i-1] + a[i+1] > dp[i-1]//2 + a[i+2]:
        dp[i] = dp[i-1] + a[i+1]
        print("굴리기", dp)
        i += 1
    else:
        dp[i] =  dp[i-1]//2 + a[i+2]
        print("던지기", dp)
        i += 2
    m -= 1

print(dp)

"""
10 5
1 3 4 5 6 7 8 10 12 14
"""