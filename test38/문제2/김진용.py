# from itertools import *
# N, M = map(int, input().split())
# ary = list(map(int, input().split()))
# result = []
# for i in permutations(ary, M):
#     result.append(i)
# result.sort()
# for i in result:
#     print(*i)


N, M = map(int, input().split())
ary = list(map(int, input().split()))
ary.sort()


def bt(depth):
    if depth == M:
        print(*stk)
        return

    for v in range(len(ary)):
        if ary[v] not in stk:
            stk.append(ary[v])
            bt(depth + 1)
            stk.pop()


stk = []
visited = [False] * N

bt(0)
