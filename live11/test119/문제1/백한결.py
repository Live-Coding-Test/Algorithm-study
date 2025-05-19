import heapq
import sys
from collections import defaultdict


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    problems = defaultdict(list)
    aheadResolveProblems = [0] * (N+1)

    for i in range(M):
        A, B = map(int, input().split())
        problems[A].append(B)
        aheadResolveProblems[B] += 1

    result = []
    heap = []

    for i in range(1, N+1):
        if aheadResolveProblems[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        now = heapq.heappop(heap)
        result.append(now)

        for next in problems[now]:
            aheadResolveProblems[next] -= 1
            if aheadResolveProblems[next] == 0:
                heapq.heappush(heap, next)

    print(*result)

if __name__ == '__main__':
    main()

# 1234
# 1. 4는 2보다 먼저 푸는 것이 좋음 -> 1 4 2 3
# 2. 3은 1보다 먼저 푸는 것이 좋음 -> 3 1 4 2