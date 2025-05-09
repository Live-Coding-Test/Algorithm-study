import sys
from collections import *

input = sys.stdin.readline

n, t = map(int, input().split())
holds = set()
y_dict = defaultdict(list)

for _ in range(n):
    x, y = map(int, input().split())
    holds.add((x, y))
    y_dict[y].append(x)

visited = set()

q = deque([(0, 0, 0)])
while q:
    x, y, cnt = q.popleft()
    if y == t:
        print(cnt)
        break

    for ny in range(y - 2, y + 3):
        if ny not in y_dict:
            continue
        for nx in y_dict[ny]:
            if abs(nx - x) <= 2 and (nx, ny) in holds and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, cnt + 1))

else:
    print(-1)
