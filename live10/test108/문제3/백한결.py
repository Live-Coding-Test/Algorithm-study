import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
count = 0

def main():
    input = sys.stdin.readline
    N, W = map(int, input().split())

    tree = defaultdict(list)

    for _ in range(N-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    def dfs(node, parent):
        global count
        isLeaf = True
        for child in tree[node]:
            if child != parent:
                isLeaf = False
                dfs(child, node)
        if isLeaf:
            count += 1

    dfs(1, -1)

    print(W / count)

if __name__ == '__main__':
    main()