import sys


def main():
    N, M = map(int, sys.stdin.readline().split())

    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    result = sorted(A + B)

    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()