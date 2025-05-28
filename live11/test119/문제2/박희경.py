import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

i, j = 0, 0
prefix_sum = arr[0]
res = float('inf')

while True:
    if j >= n: 
        break
    if prefix_sum >= s:
        res = min(res, j-i+1)
        prefix_sum -= arr[i]
        i += 1
    else:
        j += 1
        if j < n:
            prefix_sum += arr[j]

if res != float('inf'):
    print(res)
else:
    print(0)