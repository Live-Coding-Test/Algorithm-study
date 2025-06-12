import sys

def main():
    input = sys.stdin.readline
    G = int(input())
    P = int(input())

    parent = [i for i in range(G+1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    count = 0

    for _ in range(P):
        g = int(input())
        dockingGate = find(g)

        if dockingGate == 0:
            break
        parent[dockingGate] = find(dockingGate - 1)
        count += 1

    print(count)

if __name__ == '__main__':
    main()