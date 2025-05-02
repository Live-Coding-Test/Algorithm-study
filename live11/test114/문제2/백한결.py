import sys
input = sys.stdin.readline

def main():
    N = int(input())
    events = []
    for i in range(N):
        x, r = map(int, input().split())
        events.append((x - r, i, 0))
        events.append((x + r, i, 1))

    events.sort(key=lambda e: e[0])

    for i in range(1, len(events)):
        if events[i][0] == events[i-1][0]:
            print("NO")
            return

    stack = []
    for _, idx, typ in events:
        if typ == 0:
            stack.append(idx)
        else:
            if not stack or stack[-1] != idx:
                print("NO")
                return
            stack.pop()

    print("YES")

if __name__ == "__main__":
    main()