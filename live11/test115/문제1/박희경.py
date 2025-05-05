import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
stack = [int(input())]
max_num = stack[-1]
for _ in range(n - 1):
    num = int(input())
    if stack[-1] < num:
        cnt += num - stack[-1]
        max_num = max(max_num, num)
    stack.pop()
    stack.append(num)
cnt += max_num * len(stack) - sum(stack)
print(cnt)