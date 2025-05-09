import sys
from collections import defaultdict, deque


def main():
    input = sys.stdin.readline
    n, T = map(int, input().split())

    stones = set()
    yMap = defaultdict(list)

    for _ in range(n):
        x, y = map(int, input().split())
        stones.add((x, y))
        yMap[y].append(x)

    for y in yMap:
        yMap[y].sort()

    visited = set()
    queue = deque()
    queue.append(((0, 0), 0)) # 위치 (x, y), 이동 횟수

    while queue:
        (x, y), count = queue.popleft()

        if y == T:
            print(count)
            return

        for ny in range(y-2, y+3):
            if ny < 0 or ny > T:
                continue
            for nx in range(x-2, x+3):
                if (nx, ny) in stones and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), count + 1))

    print(-1)

if __name__ == '__main__':
    main()