"""
인접하는 집의 색상이 같지 않다.
dp
"""
import sys

input = sys.stdin.readline

cost = []
n = int(input())
for _ in range(n):
    cost.append(list(map(int, input().split())))
    

dp = cost.copy()


for i in range(1, n):
    


"""
3
26 40 83
49 60 57
13 89 99
"""