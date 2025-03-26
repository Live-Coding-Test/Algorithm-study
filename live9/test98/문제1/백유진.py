from itertools import product
n, m = map(int, input().split())
arr = list(map(int, input().split()))

dx = [1, 2]

max = float("-inf")

for p in product(dx, repeat=m):
  now = -1
  snow = 1
  for i in p:
    if i == 1:
      now += 1
      if now < n:
        snow += arr[now]
    elif i == 2:
      now += 2
      if now < n:
        snow //= 2
        snow += arr[now]
  if snow > max:
    max = snow

print(max)