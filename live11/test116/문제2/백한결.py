import sys

def main():
    input = sys.stdin.readline
    n, T = map(int, input().split())

    stones = set()

    for _ in range(n):
        x, y = map(int, input().split())
        stones.add((x, y))



if __name__ == '__main__':
    main()