import sys

input = sys.stdin.readline


# 도시 개수, 도로 개수, 거리 정보, 출발 도시
n, m, k, x = map(int, input().split())
distance = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    distance[a][b] = 1

for mid in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j: continue
            if distance[i][mid] != float('inf') and distance[mid][j] != float('inf'):
                distance[i][j] = min(distance[i][j], distance[i][mid] + distance[mid][j])

print(distance[x])
if k not in distance[x]:
    print(-1)
for dist in distance[x]:
    if dist == k:
        print(distance[x].index(dist))


"""
4 4 2 1
1 2
1 3
2 3
2 4
"""