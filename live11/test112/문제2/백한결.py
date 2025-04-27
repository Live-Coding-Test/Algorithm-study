import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    S = input().strip()
    T = input().strip()
    found = False

    def bt(cur: str):
        nonlocal found
        if found:
            return

        if len(cur) < len(S):
            return

        if len(cur) == len(S):
            if cur == S:
                found = True
            return

        if cur.endswith('A'):
            bt(cur[:-1])

        if cur.startswith('B'):
            bt(cur[1:][::-1])

    bt(T)
    print(1 if found else 0)

if __name__ == '__main__':
    main()