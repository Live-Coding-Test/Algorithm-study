from collections import deque

def main():
    N, M = map(int, input().split())
    a = list(map(int, input().strip().split()))[:N]

    print(bfs(N, M, a))


def bfs(N, M, a):
    queue = deque()

    # 시작위치 0, 눈덩이 크기 1, 시간 0초
    queue.append((0, 1, 0))

    visited = set()
    visited.add((0, 1, 0))

    maxSize = 1

    while queue:
        location, size, time = queue.popleft()

        maxSize = max(maxSize, size)

        if time == M:
            continue

        # 눈동이를 한 칸 이동시킬 경우
        nextLocation = location + 1
        if nextLocation < N:
            plusSize = size + a[nextLocation]
            current = (nextLocation, plusSize, time+1)
            if current not in visited:
                visited.add(current)
                queue.append(current)

        # 눈덩이를 두 칸 이동시킬 경우
        nextLocation = location + 2
        if nextLocation < N:
            plusSize = size // 2 + a[nextLocation]
            current = (nextLocation, plusSize, time+1)
            if current not in visited:
                visited.add(current)
                queue.append(current)

    return maxSize


if __name__ == '__main__':
    main()