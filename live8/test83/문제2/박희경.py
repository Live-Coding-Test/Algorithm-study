import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

cards.sort()  # [-10, 2, 3, 6, 10]


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == target:
            return True
        elif cards[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


for i in range(len(arr)):
    if binary_search(0, n - 1, arr[i]):
        arr[i] = 1
    else:
        arr[i] = 0
print(*arr)
