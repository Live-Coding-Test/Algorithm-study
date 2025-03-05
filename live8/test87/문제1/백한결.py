def solution(numbers):
    answer = []
    bigNumber = []

    for i in range(len(numbers) - 1, -1, -1):
        while bigNumber and bigNumber[-1] <= numbers[i]:
            bigNumber.pop()

        if bigNumber:
            answer.append(bigNumber[-1])
        else:
            answer.append(-1)

        bigNumber.append(numbers[i])

    answer.reverse()

    return answer


numbers = [9, 1, 5, 3, 6, 2]

print(solution(numbers))
