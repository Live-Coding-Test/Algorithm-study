n, k = map(int, input().split())

ary = list(map(int, input().split()))

max_visited = -1
days_total = 0

start = 0
end = k - 1

visited = sum(ary[start:end])

while end < n:
    visited += ary[end]

    if visited == max_visited:
        days_total += 1
    elif visited > max_visited:
        days_total = 1

    max_visited = max(max_visited, visited)

    visited -= ary[start]
    start += 1
    end += 1

if sum(ary) == 0:
    print("SAD")
else:
    print(max_visited)
    print(days_total)