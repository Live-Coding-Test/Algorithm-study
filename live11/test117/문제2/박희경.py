import sys
from collections import *

input = sys.stdin.readline

graph = defaultdict(list)
n = int(input())
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)


# def parent(x):
#     x_root = set()
#     while x in graph[x]:
#         x_root.add(x)
#         x = graph[x]
#     x_root.add(x)


# parent(2)