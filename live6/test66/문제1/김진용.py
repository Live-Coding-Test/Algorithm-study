import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

# print(paper)

cnt = {-1: 0, 0: 0, 1: 0}


def recur(x, y, n):
    color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                for a in range(3):
                    for b in range(3):
                        recur(x + (n // 3) * a, y + (n // 3) * b, n // 3)
                return

    cnt[color] += 1


recur(0, 0, n)

print(cnt[-1])
print(cnt[0])
print(cnt[1])
