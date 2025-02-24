"""
sum(k // result) == n
이때 최대 result 구하기
"""

import sys

input = sys.stdin.readline


def binary_search(arr):
    start, end = 1, max(arr)
    while start <= end:
        mid = (start + end) // 2  # 반으로 자른 길이
        cnt = 0
        for i in cm:
            cnt += i // mid
        if cnt > n:  # 길이를 늘릴 필요가 있음
            start = mid + 1
        else:
            end = mid - 1
    return end


k, n = map(int, input().split())
cm = []
for _ in range(k):
    cm.append(int(input()))

cm.sort()  # [457, 539, 743, 802]
print(binary_search(cm))


"""
4 11
802
743
457
539
"""