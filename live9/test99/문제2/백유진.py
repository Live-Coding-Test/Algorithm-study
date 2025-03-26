from itertools import permutations
n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = []
for p in permutations(arr, m):
  result.append(p)

result.sort()

for r in result:
  print(*r)