import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    T = str(input().strip())

    makeT(S, T)

def makeT(current, T):
    if len(current) > len(T):
        return
    if current == T:
        print(1)

    makeT(current + 'A', T)
    makeT((current + 'B')[::-1], T)


if __name__ == '__main__':
    main()