import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dots = sorted(list(map(int, input().split())))

# 타겟을 찾는 최초 좌표 구하기
def lower_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

# 타겟을 포함한 좌표 구하기 (놓친 부분 : 나눠서 해야 하는구나)
def upper_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start


for _ in range(m):
    a, b = map(int, input().split())

    left = lower_bound(dots, a) 
    right = upper_bound(dots, b)
    print(right - left)

"""
5 5
1 3 10 20 30
1 10
20 60
3 30
2 15
4 8
"""