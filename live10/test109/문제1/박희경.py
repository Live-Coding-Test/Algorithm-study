import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

remain = [0] * m    # 나머지 개수 
prefix_sum = 0
for i in range(n):
    prefix_sum += a[i]
    remain[prefix_sum % m] += 1

res = remain[0]
# 나머지가 같은 구간 2개를 뽑으면 나머지가 0이 됨
for r in remain:
    # 조합; rC2 = r(r-1) / 2
    res += r * (r - 1) // 2

print(res)

"""
5 3
1 2 3 1 2
"""