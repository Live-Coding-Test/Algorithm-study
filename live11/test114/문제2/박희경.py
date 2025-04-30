import sys


input = sys.stdin.readline

n = int(input())
radius = []
for _ in range(n):
    x, r = map(int, input().split())
    radius.append((x-r, x+r))

radius.sort()

flag = 'YES'
stack = []
for start, end in radius:
    if not stack:
        stack.append((start, end))
    else:
        pre_start, pre_end = stack.pop()
        if pre_start >= start or pre_end == start:  # 맞닿아 있을 때
            flag = 'NO'
            break
        if pre_end > start and pre_end <= end:  # 겹칠 때
            flag = 'NO'
            break
print(flag)
