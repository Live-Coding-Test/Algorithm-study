import sys


def binary_search(arr, target):
    start, end = 0, max(arr)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in arr:
            if i > mid:
                total += mid
            else:
                total += i
        if total > target:
            end = mid - 1
        else:
            start = mid + 1
    return end


input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
m = int(input())

budget.sort()   # 110 120 140 150
print(binary_search(budget, m))


"""
4
120 110 140 150
485

5
70 80 30 40 100
450
"""