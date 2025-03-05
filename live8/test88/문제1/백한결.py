def solution(sequence, k):
    answer = [0, 0]
    sum = 0
    min = 1000000000

    left = 0

    for right in range(len(sequence)):
        sum += sequence[right]

        while sum > k and right >= left:
            sum -= sequence[left]
            left += 1

        if sum == k:
            if right - left < min:
                min = right - left
                answer = [left, right]

    return answer