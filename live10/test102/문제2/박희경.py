import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

max_profit = 0
min_price = float('inf')

for a in arr:
    min_price = min(a, min_price)
    max_profit = max(a - min_price, max_profit)

print(max_profit)