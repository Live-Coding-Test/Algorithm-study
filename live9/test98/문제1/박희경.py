import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [1] + list(map(int, input().split()))

def snow(size, time, idx):
    global res

    if time > m:
        return
    if time <= m:
        res = max(res, size)
    if idx + 1 <= n:
        snow(size + a[idx + 1], time + 1, idx + 1)
    if idx + 2 <= n:
        snow(size // 2 + a[idx + 2], time + 1, idx + 2)

res = 0
snow(1, 0, 0)
print(res)

"""
10 5
1 3 4 5 6 7 8 10 12 14
"""