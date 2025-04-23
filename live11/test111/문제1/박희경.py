"""
내가 생각한건 거리 * 사람수로 해서 구해보려했으나 
사람 수의 절반이 넘어가는 지점의 마을 위치를 찾는 문제 (그리디였음)
"""
import sys

input = sys.stdin.readline

n = int(input())
village = []
for _ in range(n):
    village.append(list(map(int, input().split())))

village.sort(key = lambda x: x[0])
mid = (sum(p for _, p in village)) // 2

count = 0
for position, people in village:
    count += people
    if count >= mid:
        print(position)
        break
