from collections import deque

def main():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    print(bfs(N, M, a))

def bfs(N, M, a):
    queue = deque()

    # 시작위치 0, 눈덩이 크기 1, 시간 0초
    queue.append((-1, 1, 0))
    maxSize = 1

    while queue:
        location, size, time = queue.popleft()

        # 시간 초과 or 마지막 칸 도달
        if time == M or location == N - 1:
            maxSize = max(maxSize, size)
            continue

        # 눈동이를 한 칸 이동시킬 경우
        nextLoc1 = location + 1
        if nextLoc1 < N:
            nextSize1 = size + a[nextLoc1]
            queue.append((nextLoc1, nextSize1, time + 1))

        # 눈덩이를 두 칸 이동시킬 경우
        nextLoc2 = location + 2
        if nextLoc2 < N:
            nextSize2 = size // 2 + a[nextLoc2]
            queue.append((nextLoc2, nextSize2, time + 1))


    return maxSize

if __name__ == '__main__':
    main()