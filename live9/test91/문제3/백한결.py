def solution(answers):
    drop_math1 = [1, 2, 3, 4, 5]
    drop_math2 = [2, 1, 2, 3, 2, 4, 2, 5]
    drop_math3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result1, result2, result3 = 0, 0, 0

    answer = []

    for i in range(len(answers)):
        if drop_math1[i % len(drop_math1)] == answers[i]:
            result1 += 1
        if drop_math2[i % len(drop_math2)] == answers[i]:
            result2 += 1
        if drop_math3[i % len(drop_math3)] == answers[i]:
            result3 += 1

    max_score = max(result1, result2, result3)

    if result1 == max_score:
        answer.append(1)
    if result2 == max_score:
        answer.append(2)
    if result3 == max_score:
        answer.append(3)

    return answer
