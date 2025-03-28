import sys
from itertools import *

input = sys.stdin.readline

n = int(input())
roman = [1, 5, 10, 50]

res = set()
for comb in combinations_with_replacement(roman, n):
    if sum(comb) not in res:
        res.add(sum(comb))

print(len(res))
