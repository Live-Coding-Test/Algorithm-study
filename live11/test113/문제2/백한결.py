import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    N = int(input())

    graph = defaultdict(dict)

    for _ in range(N):
        food = input().strip().split()
        K = int(food[0])
        foods = food[1:]

        current_node = graph
        for f in foods:
            if f not in current_node:
                current_node[f] = defaultdict(dict)
            current_node = current_node[f]

    dfs(graph, 0)

def dfs(node, depth):
    for key in sorted(node.keys()):
        print('--' * depth + key)
        dfs(node[key], depth + 1)

if __name__ == '__main__':
    main()