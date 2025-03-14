from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

max = 0

for per in permutations(arr):
  cum = 0
  for i in range(n-1):
    cum += abs(per[i] - per[i+1])
  if cum > max:
    max = cum

print(max)