import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()  # -99 -2 -1 4 98
ans = float('inf')

start, end = 0, n - 1
while start < end:
    total = arr[start] + arr[end] 
    diff = abs(total)
    
    if diff < ans:
        ans = diff
        answer = (arr[start], arr[end])

    if total == 0:
        break
    elif total < 0:
        start += 1
    else:
        end -= 1

print(*answer)  