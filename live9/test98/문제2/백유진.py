from itertools import permutations

x = input()

min = float("inf")

for p in permutations(x, len(x)):
  num = ''.join(p)
  if int(x) < int(num) < min:
    min = int(num)

if min == float("inf"):
  print(0)
else:
  print(min)