import sys
from itertools import *

input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for perm in permutations(arr, m):
    print(*perm)