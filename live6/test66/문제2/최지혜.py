import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    area = list(map(int,input().split()))
    graph.append(area)

start = (0,0)

visited = [[0] * n for _ in range(n)] # 방문 여부 기록 리스트

def dfs(x, y):

    visited[x][y]=True # 현재 위치 방문 처리

    # 이동할 수 있는 방향 설정 (오른쪽 또는 아래쪽으로만 이동 가능)
    dx = [graph[x][y],0] # 오른쪽
    dy = [0,graph[x][y]] # 아래쪽

    
dfs(0, 0)

if visited[n-1][n-1] == True: # 도달 여부 확인
    print('HaruHaru')
else:
    print('Hing')