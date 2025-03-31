from itertools import *

def main():
    N = int(input())

    romaNum = [1, 5, 10, 50]

    numSet = set()

    for prod in combinations_with_replacement(romaNum, N):
        numSet.add(sum(prod))

    print(len(numSet))


if __name__ == "__main__":
    main()