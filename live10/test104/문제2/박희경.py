import sys

input = sys.stdin.readline

n = int(input())
friends = [list(map(str, input().rstrip())) for _ in range(n)]
relation = [[0] * n for _ in range(n)]


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if (friends[i][k] == 'Y' and friends[k][j] == 'Y') or friends[i][j] == 'Y':
                relation[i][j] = 1

print(relation)
max_count = 0
for r in relation:
    max_count = max(max_count, sum(r))
print(max_count)
