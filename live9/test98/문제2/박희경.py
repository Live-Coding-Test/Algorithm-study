import sys
from itertools import *

input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
x = int(''.join(arr))
res = x
arr.sort()

for perm in permutations(arr, len(arr)):
    if int(''.join(perm)) > res:
        res = int(''.join(perm))
        break
if res == x:
    print(0)
else:
    print(res)

