def solution(queue1, queue2):
    # 합이 애당초 홀수면 불가능 (반으로 나누어지지 않음)
    total = sum(queue1) + sum(queue2)
    if total % 2 != 0:
        return -1

    totalQueue = queue1 + queue2

    start, end = 0, len(queue1)
    current_sum = sum(queue1)

    for count in range(len(totalQueue) * 2):
        if current_sum == total // 2:
            return count

        elif current_sum < total // 2:
            if end >= len(totalQueue):
                return -1
            current_sum += totalQueue[end]
            end += 1
        else:
            current_sum -= totalQueue[start]
            start += 1

    return -1