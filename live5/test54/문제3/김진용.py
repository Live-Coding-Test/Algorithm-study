def solution(n, lost, reserve):
    dic = {}

    for student in range(1, n + 1):
        if student in reserve and student in lost:
            dic[student] = 1
        elif student in lost:
            dic[student] = 0
        elif student in reserve:
            dic[student] = 2
        else:
            dic[student] = 1

    for n in dic:
        if n - 1 in dic:
            if dic[n - 1] == 0 and dic[n] == 2:
                dic[n] -= 1
                dic[n - 1] = 1
        if n + 1 in dic:
            if dic[n + 1] == 0 and dic[n] == 2:
                dic[n] -= 1
                dic[n + 1] = 1

    result = 0
    for i in dic.values():
        if i >= 1:
            result += 1

    return result


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 3, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
