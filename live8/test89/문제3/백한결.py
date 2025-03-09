def solution(numbers):
    str_array = list(map(str, numbers))

    sorted_array = sorted(str_array, key=lambda x: x * 3, reverse=True)

    answer = ''.join(sorted_array)

    return '0' if answer[0] == '0' else answer