from collections import *


def solution(prices):
    answer = []

    queue = deque(prices)
    while queue:
        sec = 0
        price = queue.popleft()
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)

    return answer