n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

def dfs(start_index, start_val, plus, minus, mul, div):
  stack = [(start_index, start_val, plus, minus, mul, div)]
  max_result = -float('inf')
  min_result = float('inf')

  while stack:
    index, current, p, m, mu, d = stack.pop()
    if index == n:
      max_result = max(max_result, current)
      min_result = min(min_result, current)
      continue

    num = arr[index]

    if p:
      stack.append((index + 1, current + num, p - 1, m, mu, d))
    if m:
      stack.append((index + 1, current - num, p, m - 1, mu, d))
    if mu:
      stack.append((index + 1, current * num, p, m, mu - 1, d))
    if d:
      if current < 0:
        next_val = -(-current // num)
      else:
        next_val = current // num
      stack.append((index + 1, next_val, p, m, mu, d - 1))

  return max_result, min_result

max_val, min_val = dfs(1, arr[0], *op)

print(max_val)
print(min_val)