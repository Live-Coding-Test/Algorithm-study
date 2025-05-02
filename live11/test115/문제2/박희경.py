import sys


input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

stack = []
res = [-1] * n
for i in range(n - 1, -1, -1):  # 역순으로
    while stack and stack[-1] <= a[i]:
        stack.pop()

    if stack:
        res[i] = stack[-1]

    stack.append(a[i])

print(*res)


"""
4
3 5 2 7
"""