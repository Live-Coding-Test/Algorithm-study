def main():
    n = int(input())

    array = list(map(int, input().strip().split()))[:n]

    x = int(input())

    array.sort()

    count = 0
    left, right = 0, n - 1

    while left < right:
        sum = array[left] + array[right]

        if sum == x:
            count += 1
            left += 1
            right -= 1
        elif sum < x:
            left += 1
        else:
            right -= 1


    print(count)


if __name__ == '__main__':
    main()