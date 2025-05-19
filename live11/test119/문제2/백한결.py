import sys

def main():
    input = sys.stdin.readline

    N, S = map(int, input().split())
    sequence = list(map(int, input().split()))

    start = 0
    end = 0
    current_sum = 0
    result = float('inf')

    while end != N:
        if current_sum >= S:
            result = min(result, end - start)
            current_sum -= sequence[start]
            start += 1
        else:
            current_sum += sequence[end]
            end += 1

    print(result if result != float('inf') else 0)

if __name__ == '__main__':
    main()