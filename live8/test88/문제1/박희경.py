def solution(sequence, k):
    answer = []

    i, j = 0, 0
    total = sum(sequence[i: j + 1])
    while i + j < len(sequence) * 2 - 1:
        if i <= j:
            if total == k:
                answer.append([i, j])
                total -= sequence[i]
                i += 1
                j += 1
                if j < len(sequence):
                    total += sequence[j]
            elif total < k:
                j += 1
                if j < len(sequence):
                    total += sequence[j]
            else:
                total -= sequence[i]
                i += 1

    # res = []
    # if len(answer) == 1:
    #     return answer[0]
    # min_diff = float("inf")
    # for ans in answer:
    #     diff = ans[1] - ans[0]
    #     if diff < min_diff:
    #         res = ans
    #         min_diff = diff
    # return res
    answer = sorted(answer, key=lambda x: x[1] - x[0])  # 코드 개선
    return answer[0]
