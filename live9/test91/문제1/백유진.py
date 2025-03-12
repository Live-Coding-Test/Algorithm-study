n = int(input())
arr = list(map(int, input().split()))

arr.sort()

start = 0
end = n-1

min = float("inf")
answer = []

while start < end:
  cum = arr[start] + arr[end]
  if cum == 0:
    answer.append([arr[start], arr[end]])
    break
  elif cum < 0:
    if abs(cum) < min:
      min = abs(cum)
      answer.append([arr[start], arr[end]])
    start += 1
  else:
    if abs(cum) < min:
      min = abs(cum)
      answer.append([arr[start], arr[end]])
    end -= 1

result = answer.pop()
result.sort()
print(*result)

