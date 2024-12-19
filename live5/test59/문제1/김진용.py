import sys
input = sys.stdin.readline

n = int(input())
ary = list(map(int, input().split()))
sum_ary = [0]

for i in ary:
    sum_ary.append(sum_ary[-1] + i)
# print(sum_ary)

m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    print(sum_ary[j] - sum_ary[i-1])