import sys


def binary_search(arr, target):
    start, end = 0, max(arr)

    while start <= end:
        mid = (start + end) // 2
        high = 0
        for i in arr:
            if i > mid:
                high += i - mid
        if high < target:     # 높이를 낮출 필요가 있음
            end = mid - 1
        else:                 # target이랑 일치해도 최대 높이를 구해야하니까
            start = mid + 1
    return end


input = sys.stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))

h.sort()  # 10, 15, 17, 20
print(binary_search(h, m))

"""
4 7
20 15 10 17

5 20
4 42 40 26 46
"""
