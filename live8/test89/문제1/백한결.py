def main():
    min_count = float('inf')

    N = int(input())

    array = [int(input()) for _ in range(N)]

    array.sort()

    for i in range(len(array)):
        for j in range(i, len(array)):
            min_val = array[i]
            max_val = array[j]

            current_length = j - i + 1

            required_length = max_val - min_val + 1

            if required_length <= 5:
                need_number = 5 - current_length
            else:
                need_number = float('inf')

            min_count = min(min_count, need_number)
    print(min_count)


if __name__ == '__main__':
    main()