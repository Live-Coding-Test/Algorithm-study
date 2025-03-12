import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort()    
reverse_a = sorted(a, reverse=True)

arr = []
for i in range(n):
    arr.append(a[i])
    arr.append(reverse_a[i])
    # 이미 존재한다면 반복문 끝

print(arr)

"""
6
20 1 15 8 4 10
"""