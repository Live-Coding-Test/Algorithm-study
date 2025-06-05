import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

res, cnt = 0, 1
for i in range(n):
    if i % 2 != 0:
        if i == n - 1: abs(sensor[i] - sensor[i-1])
        else:
            res += min(abs(sensor[i] - sensor[i-1]), abs(sensor[i+1] - sensor[i]))
    else:
        if cnt < k:
            cnt += 1
    
print(res)