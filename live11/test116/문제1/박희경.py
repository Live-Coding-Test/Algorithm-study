import sys
from collections import *

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    tree = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[b] = a
    x, y = map(int, input().split())

    x_roots = set()
    while x in tree:
        x_roots.add(x)
        x = tree[x]
    x_roots.add(x)
    
    while y not in x_roots:
        y = tree[y]   

    print(y)