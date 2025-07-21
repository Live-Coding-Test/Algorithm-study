from itertools import permutations


def solution(numbers):
    numberSet = set()

    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            numberSet.add(num)

    count = 0

    for num in numberSet:
        if num < 2:
            continue
        isPrime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                isPrime = False
                break

        if isPrime:
            count += 1

    return count