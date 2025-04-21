def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    prefix = 0
    count = [0] * M
    count[0] = 1

    result = 0

    for num in A:
        prefix = (prefix + num) % M
        result += count[prefix]
        count[prefix] += 1

    print(result)

if __name__ == '__main__':
    main()