import sys

input = sys.stdin.readline

n, t = map(int, input().split())
hold = []
for _ in range(n):
    hold.append(list(map(int, input().split())))

hold.sort() # [[0, 2], [1, 2], [3, 2], [4, 1], [6, 3]]
