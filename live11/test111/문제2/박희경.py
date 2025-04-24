import sys

input = sys.stdin.readline

n = int(input())
years = [0] * 366
for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        years[i] += 1

# [0, 0, 1, 1, 2, 3, 2, 2, 1, 1, 0, 1, 2, ...]

chunk = []
group = []
for i in range(1, len(years)):
    if years[i] != 0:
        chunk.append(years[i])
    else:
        if chunk:
            group.append(chunk[:])
            chunk.clear()
if chunk:
    group.append(chunk[:])
    
res = 0
for g in group:
    res += max(g) * len(g)

print(res)