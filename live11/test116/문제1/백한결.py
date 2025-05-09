import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        N = int(input())
        parent = [0] * (N+1)
        depth = [0] * (N+1)
        tree = [[] for _ in range(N+1)]
        isChild = [False] * (N+1)
        for _ in range(N-1):
            a, b = map(int, input().split())
            parent[b] = a
            tree[a].append(b)
            isChild[b] = True

        root = 0
        for i in range(1, N+1):
            if not isChild[i]:
                root = i
                break

        def dfs(node, d):
            depth[node] = d
            for child in tree[node]:
                dfs(child, d + 1)

        dfs(root, 0)

        a, b = map(int, input().split())

        while depth[a] > depth[b]:
            a = parent[a]
        while depth[a] < depth[b]:
            b = parent[b]

        while a != b:
            a = parent[a]
            b = parent[b]

        print(a)

if __name__ == '__main__':
    main()