import sys

input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split()))

values.sort()
start = 0
end = n - 1
min_diff = 1000000000
answer = {}

while start < end:
    sum = values[start] + values[end]
    key = sum
    value = [values[start], values[end]]
    answer[key] = value

    if sum == 0:
        print(values[start], values[end])
        break
    elif abs(sum) == 1:
        print(values[start], values[end])
        break
    else:
        if sum > 0:
            end -= 1
        else:
            start += 1
        min_diff = min(min_diff, abs(sum))


if min_diff != 1000000000:
    print(*answer.get(min_diff))

# 다른 테스트 케이스
# 5
# -9 -7 -2 -1 4 5