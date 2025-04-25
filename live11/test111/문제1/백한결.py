import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    pair = []
    totalA = 0

    for _ in range(N):
        X, A = map(int, input().split())
        pair.append((X, A))
        totalA += A

    pair.sort(key=lambda x:x[0])

    medium = (totalA+1) // 2

    sumA = 0

    for x, a in pair:
        sumA += a

        if sumA >= medium:
            print(x)
            break


if __name__ == '__main__':
    main()