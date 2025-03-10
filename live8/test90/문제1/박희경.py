import sys

input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

i, j = 0, n - 1
cnt = 0
while i < j:
    total = a[i] + a[j]
    if total == x:
        cnt += 1
        i += 1
        j -= 1
    elif total > x:
        j -= 1
    else:
        i += 1

print(cnt)
