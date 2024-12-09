import sys
from collections import *

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    cnt = 0
    q = deque(docs)
    while q:
        # target_idx = compare(q[0], q)
        priority = max(q)
        cur = q.popleft()
        m -= 1  # 앞 당기기

        if cur == priority:
            cnt += 1
            if m < 0:   # 해당 문서가 맨 앞에 있을 때
                print(cnt)
                break
        else:
            q.append(cur)
            if m < 0:
                m = len(q) - 1  # 맨 앞에서 맨 뒤로




"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
"""

