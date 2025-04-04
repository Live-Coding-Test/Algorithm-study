from collections import *

def solution(x, y, n):
    visited = set([x])

    q = deque([(0, x)])
    while q:
        cnt, x = q.popleft()
        if x == y:
            return cnt
        for nx in (x + n, x * 2, x * 3):
            if nx <= y and nx not in visited:
                visited.add(nx)
                q.append((cnt + 1, nx))
            
    return -1