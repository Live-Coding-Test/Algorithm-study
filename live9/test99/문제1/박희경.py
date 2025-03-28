import sys
from itertools import *

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

operator_cnt = list(map(int, input().split()))

max_value = float('-inf')
min_value = float('inf')


def bf(value, idx):
    global max_value, min_value
    if idx == n:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return
    if operator_cnt[0] > 0: 
        operator_cnt[0] -= 1
        bf(value + a[idx], idx + 1)
        operator_cnt[0] += 1        # 놓친 부분

    if operator_cnt[1] > 0:
        operator_cnt[1] -= 1
        bf(value - a[idx], idx + 1)
        operator_cnt[1] += 1

    if operator_cnt[2] > 0:
        operator_cnt[2] -= 1
        bf(value * a[idx], idx + 1)
        operator_cnt[2] += 1

    if operator_cnt[3] > 0:
        operator_cnt[3] -= 1
        bf(int(value / a[idx]), idx + 1)    # 놓친 부분
        operator_cnt[3] += 1

bf(a[0], 1)
print(max_value)
print(min_value)