import sys

input = sys.stdin.readline

m, n = map(int, input().split())


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for j in range(m, n + 1):
    if is_prime(j):
        print(j)
