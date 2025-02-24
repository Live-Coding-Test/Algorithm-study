import sys

input = sys.stdin.readline


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    k = int(input())
    if is_prime(k):
        print(0)
    else:
        plus, minus = k, k
        cnt = 0
        while True:
            if is_prime(plus):
                break
            plus += 1
            cnt += 1
        while True:
            if is_prime(minus):
                break
            minus -= 1
            cnt += 1
        print(cnt)
