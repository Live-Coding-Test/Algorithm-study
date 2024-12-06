def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    answer = n - len(new_lost)
    for l in new_lost:
        # if l in new_reserve:
        #     answer += 1
        #     new_reserve.remove(l)
        if l-1 in new_reserve:
            answer += 1
            new_reserve.remove(l-1)
        elif l+1 in new_reserve:
            answer += 1
            new_reserve.remove(l+1)
    return answer