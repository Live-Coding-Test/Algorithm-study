n, m = map(int, input().split())
ary = list(map(int, input().split()))

start = 0
end = 1
cnt = 0
while end <= n and start <= end:
    total = sum(ary[start:end])

    if total == m:
        cnt += 1
        end += 1
    elif total > m:
        start += 1
    else:
        end += 1
print(cnt)

