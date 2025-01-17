def solution(food):
    answer = ''

    for i in range(1, len(food)):
        if food[i] // 2 > 0:
            for _ in range(food[i] // 2):
                answer += str(i)

    return answer + '0' + answer[::-1]