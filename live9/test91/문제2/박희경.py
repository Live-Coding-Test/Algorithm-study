import sys
from itertools import *

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = float('-inf')
for perm in permutations(a, n):
    total = 0
    for i in range(n-1):
        total += abs(perm[i] - perm[i+1])
    ans = max(ans, total)

print(ans)
