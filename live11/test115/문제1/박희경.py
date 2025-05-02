import sys

input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

cnt = 0
stack = []
for num in a:
    if not stack:
        stack.append(num)
    else:
        if num > stack[-1]:
