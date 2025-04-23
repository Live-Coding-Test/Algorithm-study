import sys

def main():
    input = sys.stdin.readline
    N = int(input())

    timeStamp = []

    for _ in range(N):
        start, end = map(int, input().split())
        timeStamp.append((start, end))

    timeStamp.sort(key=lambda x: (x[1], x[0]))

    endTime = 0
    count = 0

    for start, end in timeStamp:
        if start >= endTime:
            endTime = end
            count += 1

    print(count)


if __name__ == '__main__':
    main()