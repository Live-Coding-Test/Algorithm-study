import sys

input = sys.stdin.readline

n = int(input())


# 퀸이 공격을 받는지 체크
def attack(x):
    for i in range(x):
        # 같은 열 또는 대각선에 퀸이 있는 경우
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return True
    return False

# 시작 행
def bt(start):
    global cnt

    if start == n:
        cnt += 1
        return
    else:
        for i in range(n):
            row[start] = i
            if not attack(start):
                bt(start + 1)

row = [0] * n
cnt = 0
bt(0)

print(cnt)