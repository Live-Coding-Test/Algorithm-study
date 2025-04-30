import sys


input = sys.stdin.readline

n = int(input())
radius = []
for _ in range(n):
    x, r = map(int, input().split())
    radius.append((x-r, x+r))

radius.sort()
flag = 'YES'
for i in range(len(radius) - 1):
    if radius[i][0] < radius[i+1][0]:
        if radius[i][1] > radius[i+1][1]:   # 안에 있는 경우
            continue
        else:
            flag = 'NO'
    if radius[i][1] < radius[i+1][0]:
        continue

print(flag)