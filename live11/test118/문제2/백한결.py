import sys
import heapq

def main():
    input = sys.stdin.readline

    N = int(input())
    cardSize = []

    for _ in range(N):
        card = int(input())
        cardSize.append(card)

    heapq.heapify(cardSize)
    total = 0

    while len(cardSize) >= 2:
        first = heapq.heappop(cardSize)
        second = heapq.heappop(cardSize)
        cost = first + second
        total += cost

        heapq.heappush(cardSize, cost)

    print(total)

if __name__ == '__main__':
    main()