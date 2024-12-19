import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ary = []
for _ in range(n):
    ary.append(list(map(int, input().split())))
print(ary)

simple_sum = [0]

for i in range(n):
    for j in range(m):
        simple_sum.append(simple_sum[-1] + ary[i][j])
print(simple_sum)

sum_ary = [[0] for i in range(n)]
print(sum_ary)

c = 0
for i in range(n):
    for j in range(m):
        c += 1
        sum_ary[i].append(simple_sum[c])
print(sum_ary)

m = int(input())
for _ in range(m):
    i, j, x, y = map(int, input().split())
    if i != x or j != y:
        print(sum_ary[x][y] - sum_ary[)