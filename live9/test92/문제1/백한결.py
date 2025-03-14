import heapq


def solution(scoville, K):
    count = 0

    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) <= 1:
            count = -1
            break
        first_min_num = heapq.heappop(scoville)
        second_min_num = heapq.heappop(scoville)

        mix_num = first_min_num + (second_min_num * 2)

        heapq.heappush(scoville, mix_num)
        count += 1

    return count