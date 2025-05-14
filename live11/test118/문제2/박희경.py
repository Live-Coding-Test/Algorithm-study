import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

heapq.heapify(cards)
total = 0
while len(cards) > 1:
    sum = heapq.heappop(cards) + heapq.heappop(cards)
    total += sum
    heapq.heappush(cards, sum)

print(total)