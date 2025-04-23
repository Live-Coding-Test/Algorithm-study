"""
회의실 개수인 줄 알았는데 회의 개수네요..
"""
import sys

input = sys.stdin.readline

n = int(input())
times = []

for _ in range(n):
    times.append(list(map(int, input().split())))
    
# 종료 시간 기준 정렬 (같으면 시작 시간으로 정렬)
times.sort(key=lambda x: (x[1], x[0]))
"""
[[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], 
[5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
"""
cnt = 0
end_time = 0

for start, end in times:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)

