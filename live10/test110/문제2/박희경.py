import sys

input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort()   # 6, 8, 9
boxes.sort()    # 2, 2, 4, 5, 7

if max(cranes) < max(boxes):
    print(-1)

i, j = 0, 0
while j < m:
    if cranes[i] >= boxes[j]:
        