import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

start, end = 0, 0
total = a[0]
cnt = 0
while start <= end:
    if total % m == 0:
        cnt += 1

    total -= a[start]
    start += 1
    end += 1
    if end < n:
        total += a[end]