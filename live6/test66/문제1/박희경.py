import sys

input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
minus_one = zero = one = 0


def same_paper(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[x][y] != paper[i][j]:
                return False
    return True


def cut_paper(x, y, size):
    global minus_one, zero, one
    current_num = paper[x][y]
    if same_paper(x, y, size):
        if current_num == -1:
            minus_one += 1
        elif current_num == 0:
            zero += 1
        else:
            one += 1
    else:
        new_size = size // 3
        for i in range(3):
            for j in range(3):
                cut_paper(x + i * new_size, y + j * new_size, new_size)


cut_paper(0, 0, n)
print(minus_one)
print(zero)
print(one)
