import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visitant = list(map(int, input().split()))

start, end = 0, x - 1
sum_visitant = max_visitant = sum(visitant[0:x])
cnt = 1

while end < n - 1:
    sum_visitant -= visitant[start]
    start += 1
    end += 1
    sum_visitant += visitant[end]

    if max_visitant < sum_visitant:
        max_visitant = sum_visitant
        cnt = 1
    elif max_visitant == sum_visitant:
        cnt += 1

if max_visitant == 0:
    print("SAD")
else:
    print(max_visitant)
    print(cnt)



"""
5 2
1 4 2 5 1
"""