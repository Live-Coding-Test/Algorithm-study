import sys

input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))

    dic_x = set(x)
    x.sort()  # -4, -1, 0, 2, 4

    cnt = 0

    for i in range(n):                 # ??..?
        for j in range(i + 1, n):
            dist = x[j] - x[i]          # 두 점 사이 거리 (x[j]: 중간점)
            if x[j] + dist in dic_x:
                cnt += 1

    print(cnt)
"""
2
5
2 0 -4 -1 4
5
1 3 2 5 4
"""
