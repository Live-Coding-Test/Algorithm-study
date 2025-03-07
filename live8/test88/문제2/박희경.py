import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = []
i, j = 0, 0
while i < n and j < m:
    if a[i] == b[j]:
        res.append(a[i])
        res.append(b[j])
        i += 1
        j += 1
    elif a[i] < b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1

# 한쪽은 다 탐색했는데 한 쪽은 남았을 경우
while i < n:
    res.append(a[i])
    i += 1
while j < m:
    res.append(b[j])
    j += 1

print(*res)
