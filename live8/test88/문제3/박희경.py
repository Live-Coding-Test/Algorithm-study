def solution(n, lost, reserve):
    # 도난 당한 학생이 여벌을 가지고 있을 경우 고려
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    answer = n - len(lost_set)

    for i in sorted(lost_set):
        if i - 1 in reserve_set:
            reserve_set.remove(i - 1)
            answer += 1
        elif i + 1 in reserve_set:
            reserve_set.remove(i + 1)
            answer += 1

    return answer