import sys
n = int(sys.stdin.readline().strip())
tree = {}

for n in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

    