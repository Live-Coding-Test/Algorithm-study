import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
operators_cnt = list(map(int, input().split()))

max_value = -sys.maxsize
min_value = sys.maxsize


def backtrack(value, idx):
    global max_value, min_value

    if idx == n:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return

    # 덧셈
    if operators_cnt[0] > 0:
        operators_cnt[0] -= 1
        backtrack(value + a[idx], idx + 1)
        operators_cnt[0] += 1
    # 뺄셈
    if operators_cnt[1] > 0:
        operators_cnt[1] -= 1
        backtrack(value - a[idx], idx + 1)
        operators_cnt[1] += 1
    # 곱셈
    if operators_cnt[2] > 0:
        operators_cnt[2] -= 1
        backtrack(value * a[idx], idx + 1)
        operators_cnt[2] += 1
    # 나눗셈
    if operators_cnt[3] > 0:
        operators_cnt[3] -= 1
        backtrack(int(value / a[idx]), idx + 1)
        operators_cnt[3] += 1


backtrack(a[0], 1)
print(max_value)
print(min_value)
