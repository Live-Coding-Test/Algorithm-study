def main():
    N = int(input())
    A = list(map(int, input().strip().split()))[:N]

    A.sort()

    left = 0
    right = N-1

    min_pair = (A[left], A[right])
    min_num = float('inf')

    while left < right:
        sum = A[left] + A[right]

        if abs(sum) < abs(min_num):
            min_num = sum
            min_pair = (A[left], A[right])

        elif sum < 0:
            left += 1
        else:
            right -= 1

    print(min_pair[0], min_pair[1])


if __name__ == '__main__':
    main()