import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()  # [1, 2, 3, 5, 7, 9, 10, 11, 12]
start = 0
end = len(arr) - 1
cnt = 0

while start < end:
    sum = arr[start] + arr[end]
    if sum == x:
        cnt += 1
        start += 1
        end -= 1
    elif sum < x:
        start += 1
    else:
        end -= 1

print(cnt)