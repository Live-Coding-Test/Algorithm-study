def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def main():
    N, M = map(int, input().split())
    points = list(map(int, input().split()))
    segments = [tuple(map(int, input().split())) for _ in range(M)]

    points.sort()

    for start, end in segments:
        left = lower_bound(points, start)
        right = upper_bound(points, end)

        print(right - left)

if __name__ == '__main__':
    main()