n = int(input())

arr = []

for i in range(n):
  arr.append(int(input()))

arr.sort()

start = 0
end = 0

max = float("-inf")

while end < n:
  if arr[end] - arr[start] > 4:
    start += 1
  else:
    if end - start + 1 > max:
      max = end - start + 1
    end += 1

print(5-max)