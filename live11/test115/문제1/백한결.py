import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    A = []

    for _ in range(n):
        num = int(input())
        A.append(num)

    print(list(A))

if __name__ == '__main__':
    main()