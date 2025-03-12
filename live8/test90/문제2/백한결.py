from itertools import *


def main():

    # 백트래킹을 이용한 방법
    N, M = map(int, input().split())

    def backtrack(start, sequence):
        if len(sequence) == M:
            print(' '.join(map(str, sequence)))
            return

        for i in range(start, N+1):
            backtrack(i+1, sequence+[i])

    backtrack(1, [])

    # combinations를 이용한 방법
    N, M = map(int, input().split())

    for c in combinations(range(1, N+1), M):
        print(' '.join(map(str, c)))


if __name__ == '__main__':
    main()