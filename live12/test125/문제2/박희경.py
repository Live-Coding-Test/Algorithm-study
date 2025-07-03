import sys
import copy

input = sys.stdin.readline


def flip(coins, line):
    for x, y in line:
        coins[x][y] = 'T' if coins[x][y] == 'H' else 'H'


def dfs(coins, lines, idx, count, min_count):
    flat = sum(coins, [])
    if flat.count('T') == 9 or flat.count('H') == 9:
        return min(count, min_count)
    if idx == len(lines):   # 더이상 뒤집을 줄이 없을 때
        return min_count
    
    result = dfs(copy.deepcopy(coins), lines, idx+1, count, min_count)  # 뒤집지 않고 다음 줄로 넘기는 경우

    # 뒤집고 넘기는 경우
    flipped = copy.deepcopy(coins)
    flip(flipped, lines[idx])
    result = min(result, dfs(flipped, lines, idx+1, count+1, min_count))

    return result

row_lines = [[(i, j) for j in range(3)] for i in range(3)]
col_lines = [[(j, i) for j in range(3)] for i in range(3)]
diag_lines = [[(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)]]
lines = row_lines + col_lines + diag_lines  # 나올 수 있는 모든 경우의 수

t = int(input())
for _ in range(t):
    coins = []
    for _ in range(3):
        coins.append(list(input().split()))
    res = dfs(coins, lines, 0, 0, float('inf'))
    if res != float('inf'):
        print(res)
    else: 
        print(-1)
