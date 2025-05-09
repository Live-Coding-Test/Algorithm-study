import sys
from collections import defaultdict


def main():
    input = sys.stdin.readline

    N = int(input())
    graph = defaultdict(list)

    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)

    print(graph)

if __name__ == '__main__':
    main()