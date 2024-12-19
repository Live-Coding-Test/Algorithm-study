import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

prefix_sum = [0] * (n + 1)
for i in range(1, len(arr) + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

for _ in range(m):
    i, j = map(int, input().split())

    print(prefix_sum[j] - prefix_sum[i - 1])



"""
5
10 20 30 40 50
5
1 3
2 4
3 5
1 5
4 4
==
3
1 0 -1
6
1 1
2 2
3 3
1 2
2 3
1 3
"""