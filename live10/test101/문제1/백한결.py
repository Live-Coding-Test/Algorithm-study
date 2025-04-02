dp = [-1] * 11

def main():
    T = int(input())

    for i in range(T):
        n = int(input())

        print(recursion(n))


def recursion(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    if dp[n] != -1:
        return dp[n]

    dp[n] = recursion(n-1) + recursion(n-2) + recursion(n-3)

    return dp[n]

if __name__ == "__main__":
    main()