import sys

input = sys.stdin.readline


def binary_search(cables):
    start, end = 1, max(cables)
    while start <= end:
        mid = (start + end) // 2  # 반으로 자른 길이
        cnt = 0
        for cable in cables:
            cnt += cable // mid
        if cnt < n:  # 길이를 줄일 필요가 있음
            end = mid - 1
        else:
            start = mid + 1     # 놓친 부분) 최대를 구해야 하니까..!
    return end


k, n = map(int, input().split())
cm = []
for _ in range(k):
    cm.append(int(input()))

print(binary_search(cm))


"""
4 11
802
743
457
539
"""