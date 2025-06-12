import sys

input = sys.stdin.readline

g = int(input())
p = int(input())

gate = [i for i in range(g + 1)]

# gi 이하에서 가장 가까운 사용 가능한 지점 찾기
def find(x):
    if gate[x] != x: # 이미 다른 비행기가 도킹한 경우
        gate[x] = find(gate[x])
    return gate[x]

def union(x, y):
    x = find(x)
    y = find(y)
    gate[x] = y

cnt = 0
for _ in range(p):
    gi = int(input())
    first = find(gi)
    if first == 0: # 도킹 불가
        break
    union(first, first-1)
    cnt += 1

print(cnt)


"""
4
6
2
2
3
3
4
4
"""