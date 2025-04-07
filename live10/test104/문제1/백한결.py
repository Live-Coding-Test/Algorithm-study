# P(1) = 1
# P(2) = 1
# P(3) = 1
# P(4) = 2
# P(5) = 2
# P(6) = 3
# P(7) = 4
# P(8) = 5
# P(9) = 7
# P(10) = 9


def main():
    T = int(input())

    for _ in range(T):
        N = int(input())

        if N <= 3:
            print(1)
            continue

        P = [0 for _ in range(max(N, 5))]

        P[0] = 1
        P[1] = 1
        P[2] = 1
        P[3] = 2
        P[4] = 2

        for j in range(5, N):
                P[j] = P[j-1] + P[j-5]


        print(P[N-1])


if __name__ == "__main__":
    main()