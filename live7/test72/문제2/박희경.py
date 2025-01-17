import sys
from itertools import *

input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    s = arr[1:]

    if arr == [0]:
        break

    for comb in combinations(s, 6):
        print(*comb)
    print()