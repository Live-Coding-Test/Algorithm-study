import itertools


def solution(brown, yellow):
    answer = []
    pair = []

    total = brown + yellow

    divisors = getDivisor(total)

    for comb in itertools.product(divisors, repeat=2):
        if (comb[0] - 2) * (comb[1] - 2) == yellow and comb[0] >= comb[1]:
            pair.append(comb)

    pair.sort(reverse=True)

    answer.append(pair[0][0])
    answer.append(pair[0][1])

    return answer


def getDivisor(num):
    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors
