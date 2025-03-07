def solution(numbers):
    answer = ""
    str_array = []
    cal_array = []

    for i in numbers:
        str_array.append(str(i))

    for i in range(len(str_array)):
        for j in range(i + 1, len(str_array)):
            cal_array.append(str_array[i] + str_array[j])

    return answer