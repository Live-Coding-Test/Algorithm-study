import sys

input = sys.stdin.readline


def binary_search(arr, target):
    start, end = 0, m - 1
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:   # 먹이가 작은 상황
            cnt = mid + 1
            start = mid + 1
        else:                   # 먹이가 더 큰 상황
            end = mid - 1
    return cnt


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()
    result = 0
    for i in range(len(a)):
        result += binary_search(b, a[i])
    print(result)

"""
2
5 3
8 1 7 3 1
3 6 1
3 4
2 13 7
103 11 290 215
"""