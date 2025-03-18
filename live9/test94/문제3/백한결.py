def solution(stones, k):
    start = 1
    end = max(stones)
    max_friends = 0

    while start <= end:
        mid = (start + end) // 2

        if checkUnderZero(stones, k, mid):
            max_friends = mid
            start = mid + 1
        else:
            end = mid - 1

    return max_friends


# 징검다리 수에서 건너는 사람 수를 빼서 연속된 0이하의 수가 k를 초과하는지 검사
def checkUnderZero(stones, k, friends):
    count = 0

    for stone in stones:
        if stone - friends < 0:
            count += 1
        else:
            count = 0

        if count >= k:
            return False

    return True