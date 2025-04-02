from collections import *

def solution(x, y, n):
    answer = 0
    result = []

    q = deque([x])
    while q:
        x = q.popleft()
        calculate = [x + n, x * 2, x * 3]
        cnt = 0
        for i in range(3):
            cnt += 1
            nx = calculate[i]
            if nx == y:
                return cnt
            else:
                q.append(nx)

    return answer