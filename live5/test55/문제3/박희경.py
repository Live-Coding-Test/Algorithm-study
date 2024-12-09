from collections import *


def solution(k, tangerine):
    answer = 0
    type = defaultdict(int)
    for t in tangerine:
        type[t] += 1
    sorted_type = sorted(type.items(), key=lambda x: x[1], reverse=True)

    for i in range(len(sorted_type)):
        if k > 0:
            k -= sorted_type[i][1]
            answer += 1
        elif k <= 0:
            break

    return answer