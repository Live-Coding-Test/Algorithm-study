"""
우선순위 큐 사용하고 개수와 마지막 종료 날짜 곱하면 되지 않을끼....
"""
import sys
import heapq

input = sys.stdin.readline

n = int(input())
schedule = []
heapq.heapify(schedule)
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(schedule, (e, s))

while schedule:
    heapq.heappop(schedule)
    if 