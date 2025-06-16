import sys

input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    x, y = map(int, input().split())
    lines.append([x, y])

lines.sort()

length = 0
start, end = lines[0][0], lines[0][1]
for i in range(1, n):
    if lines[i][0] <= end and lines[i][1] <= end: # 완전 겹치는 경우
        continue
    elif lines[i][0] <= end and lines[i][1] > end: # 약간 겹치는 경우 (끝점이 더 길 경우)
        end = lines[i][1]
    else:   # 안 겹치는 경우
        length 