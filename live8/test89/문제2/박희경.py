import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
i, j = 0, 0
total = 0
while j < n:
    total += a[j]
    while total >= m:
        if total == m:
            cnt += 1
        total -= a[i]
        i += 1
    j += 1

print(cnt)
