n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

start = 0
end = 0

cum_sum = arr[start]

while end < len(arr):
  if cum_sum == m:
    answer += 1
    cum_sum -= arr[start]
    start += 1
  elif cum_sum < m:
    end += 1
    if end < len(arr):
      cum_sum += arr[end]
  else:
    cum_sum -= arr[start]
    start += 1

print(answer)