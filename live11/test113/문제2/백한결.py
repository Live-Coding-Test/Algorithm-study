import sys
from collections import defaultdict


def main():
    input = sys.stdin.readline
    N = int(input())

    graph = defaultdict(list)

    for _ in range(N):
        food = list(map(str, input().strip().split()))
        K = int(food[0])
        foods = food[1:]

        current_node = graph

        for f in foods:
            if f not in current_node:
                current_node[f] = defaultdict(list)
            current_node = current_node[f]


if __name__ == '__main__':
    main()