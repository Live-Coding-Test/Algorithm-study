import sys

input = sys.stdin.readline

n = int(input())
employee = set()

for _ in range(n):
    name, log = map(str, input().split())

    if log == "enter":
        employee.add(name)
    elif log == "leave":
        employee.remove(name)

for e in sorted(employee, reverse=True):
    print(e)
