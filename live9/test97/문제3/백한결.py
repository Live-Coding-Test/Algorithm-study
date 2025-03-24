def solution(distance, rocks, n):
    rocks.sort()

    rocks = [0] + rocks + [distance]

    left = 1
    right = distance

    answer = 0

    while left <= right:
        mid = (left + right) // 2

        removedRock = 0
        prev = rocks[0]

        for i in range(1, len(rocks)):
            if rocks[i] - prev < mid:
                removedRock += 1
            else:
                prev = rocks[i]

        if removedRock > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer