def solution(numbers):
    answer = float('-inf')

    numbers_copy = numbers.copy()
    numbers_copy = sorted(map(str, numbers_copy), reverse=True)
    print(numbers_copy)

    # 시간 초과
    # for perm in permutations(numbers, len(numbers)):
    #     num = ''.join(map(str, perm))
    #     answer = max(answer, int(num))

    return ''.join(numbers_copy)