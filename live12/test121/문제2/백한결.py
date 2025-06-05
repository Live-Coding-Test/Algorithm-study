import sys

def main():
    input = sys.stdin.readline

    N = int(input())
    heights = list(map(int, input().split()))

    result = 0

    for i in range(N):
        visible = 0

        minSlope = float('inf')
        for j in range(i-1, -1, -1):
            slope = (heights[i] - heights[j]) / (i - j)
            if slope < minSlope:
                minSlope = slope
                visible += 1

        maxSlope = -float('inf')
        for j in range(i+1, N):
            slope = (heights[j] - heights[i]) / (j - i)
            if slope > maxSlope:
                maxSlope = slope
                visible += 1

        result = max(result, visible)

    print(result)

if __name__ == '__main__':
    main()