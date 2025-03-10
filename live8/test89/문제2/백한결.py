def main():
    N, M = map(int, input().split())

    A = list(map(int, input().strip().split()))[:N]

    left = 0
    sum = 0

    count = 0

    for right in range(N):
        sum += A[right]

        while sum >= M:
            if sum == M:
                count += 1
            sum -= A[left]
            left += 1

    print(count)


if __name__ == '__main__':
    main()