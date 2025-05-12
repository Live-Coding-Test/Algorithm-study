import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    file_size = list(map(int, input().split()))
    heapq.heapify(file_size)

    res = 0
    while len(file_size) > 1:
        cost = heapq.heappop(file_size) + heapq.heappop(file_size)
        res += cost
        heapq.heappush(file_size, cost)
    print(res)
    