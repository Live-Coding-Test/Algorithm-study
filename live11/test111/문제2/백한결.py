import sys

def main():
    input = sys.stdin.readline
    N = int(input())

    calendar = [0 for _ in range(366)]

    for _ in range(N):
        S, E = map(int, input().split())
        for date in range(S, E+1):
            calendar[date] += 1

    total = 0
    maxHeight = 0
    count = 0

    for date in range(len(calendar)):
        if calendar[date] != 0:
            maxHeight = max(calendar[date], maxHeight)
            count += 1
        else:
            total += count * maxHeight
            count = 0
            maxHeight = 0

    if count > 0:
        total += count * maxHeight

    print(total)

if __name__ == '__main__':
    main()