import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
print(arr)  # [1, 1, 1, 2, 2, 2, 3, 3, 4, 5]
start = 0
end = 2
cnt = 0

while end < n:
    if sum(arr[start:end]) == m:
        cnt += 1
    elif sum(arr[start:end + 1]) > m:
        start = end

print(cnt)
