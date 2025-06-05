import sys

def main():
    input = sys.stdin.readline

    N = int(input())
    K = int(input())

    sensors = list(map(int, input().split()))

    if K >= N:
        print(0)
        return

    sensors.sort()

    diffs = []
    for i in range(N-1):
        diff = sensors[i+1] - sensors[i]
        diffs.append(diff)

    diffs.sort(reverse=True)

    result = sum(diffs[K-1:])

    print(result)

if __name__ == '__main__':
    main()