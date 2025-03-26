import itertools

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))[:N]

    A.sort()

    for i in itertools.permutations(A, M):
        print(*i)

if __name__ == "__main__":
    main()