import sys
from itertools import *

input = sys.stdin.readline

expr= list(map(str, input().rstrip()))

stack = []
pairs = []
for idx, char in enumerate(expr):
    if char == '(':
        stack.append(idx)
    elif char == ')':
        open_idx = stack.pop()
        pairs.append((open_idx, idx))   

res = set()
for i in range(1, len(pairs) + 1):
    for comb in combinations(pairs, i):
        temp = list(expr)
        for open_idx, close_idx in comb:
            temp[open_idx] = ''
            temp[close_idx] = ''
        res.add(''.join(temp))
    
for r in sorted(res):
    print(r)
