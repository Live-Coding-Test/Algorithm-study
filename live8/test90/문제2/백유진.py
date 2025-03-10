from itertools import combinations

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for comb in combinations(arr, m):
    print(' '.join(map(str, comb)))