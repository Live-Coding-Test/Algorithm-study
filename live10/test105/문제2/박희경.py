import sys

input = sys.stdin.readline

alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]
arr = [[0] * 26 for _ in range(26)]


n = int(input())
for _ in range(n):
    i, _, j = map(str, input().split())
    arr[alpha.index(i)][alpha.index(j)] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            if i == j: continue
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1


m = int(input())
for _ in range(m):
    i, _, j = map(str, input().split())
    if arr[alpha.index(i)][alpha.index(j)] == 1:
        print('T')
    else:
        print('F')


"""
3
a is b
b is c
c is d
3
a is d
a is c
d is a
"""