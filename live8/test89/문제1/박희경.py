import sys

input = sys.stdin.readline

n = int(input())
arr = set()
for _ in range(n):
    arr.add(int(input()))

arr = sorted(arr)

i = 0
cnt = 0
for j in range(n):
    while arr[j] - arr[i] > 4:
        i += 1
    cnt = max(cnt, j - i + 1)


print(5 - cnt)
