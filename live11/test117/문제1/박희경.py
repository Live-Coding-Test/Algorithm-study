import sys

input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))

stack = []  # 탑 번호
res = [0] * n

for i in range(n):
    while stack and towers[stack[-1]] < towers[i]:  # 왼쪽 탑이 더 낮으면
        stack.pop()
    if stack:
        res[i] = stack[-1] + 1
    stack.append(i)
print(*res)

