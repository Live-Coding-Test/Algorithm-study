from itertools import *

def main():
    N = int(input())
    A = list(map(int, input().strip().split()))[:N]

    all_p = list(permutations(A))

    sum = 0

    max_sum = 0

    for p in range(len(all_p)):
        for i in range(len(all_p[p])-1):
            sum += abs(all_p[p][i] - all_p[p][i+1])

        if sum > max_sum:
            max_sum = sum

        sum = 0

    print(max_sum)


if __name__ == '__main__':
    main()