import sys

input = sys.stdin.readline


def binarySearch(arr, target):  # arr: 생명체 B, target: 생명체 A (포식자)
    start = 0
    end = len(arr) - 1
    cnt = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:  # 먹이가 더 작은 상황
            # print(target, "-", arr[mid])
            cnt = mid
            start = mid + 1
        else:                   # 먹이랑 크기가 같거나 큰 상황
            end = mid - 1
    return cnt


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()    # e.g. [1, 1, 3, 7, 8]
    b.sort()    # e.g. [1, 3, 6]

    result = 0
    for aa in a:
        result += (binarySearch(b, aa) + 1)

    print(result)
