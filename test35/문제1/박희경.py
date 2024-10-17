import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()


# 필요한 숫자 개수 구하는 함수
def is_correct(array):
    start = 0
    max_cnt = 0

    for end in range(n):
        while array[end] - array[start] > 4:
            start += 1
        max_cnt = max(max_cnt, end - start + 1)
    return max_cnt


print(5 - is_correct(arr))