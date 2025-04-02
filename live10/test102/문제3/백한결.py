from collections import deque

def solution(x, y, n):
    answer = 0
    dp = [-1] * (y + 1)

    dp[x] = 0

    queue = deque([x])

    while queue:
        current = queue.popleft()

        for nextNum in (current + n, current * 2, current * 3):
            if nextNum > y:
                continue
            if dp[nextNum] == -1:
                dp[nextNum] = dp[current] + 1
                queue.append(nextNum)

    return dp[y]
