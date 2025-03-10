import sys
from itertools import *

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(i for i in range(1, n + 1))

for comb in combinations(arr, m):
    print(*comb)
