def solution(n, a, b):
    cnt = 0
    while True:
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)
        cnt += 1
        if a == b:
            break
    return cnt


print(solution(8, 4, 7))
