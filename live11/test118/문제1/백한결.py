import sys
import heapq

def main():
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        K = int(input())
        fileSize = list(map(int, input().split()))[:K]

        heapq.heapify(fileSize)
        total = 0

        while len(fileSize) >= 2:
            first = heapq.heappop(fileSize)
            second = heapq.heappop(fileSize)
            cost = first + second
            total += cost

            heapq.heappush(fileSize, cost)

        print(total)


if __name__ == '__main__':
    main()