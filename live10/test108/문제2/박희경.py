"""
중복순열 시간 초과 . . . 
dp 힌트 

n = 1일 때 k가 뭐든 k개
n = 2일 때 
"""

import sys
from itertools import *

input = sys.stdin.readline
n, k = map(int, input().split())

arr = [i for i in range(0, n + 1)]

res = 0
for perm in product(arr, repeat=k):
    if sum(perm) == n:
        print(perm)
        res += 1

print(res)
