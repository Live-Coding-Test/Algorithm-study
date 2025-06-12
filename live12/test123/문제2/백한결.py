import sys

def main():
    input = sys.stdin.readline

    N = int(input())

    for i in range(N):
        x, y = map(int, input().split())

if __name__ == '__main__':
    main()