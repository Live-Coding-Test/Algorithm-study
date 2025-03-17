import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    
    res = 0
    while True: 
        min_value = heapq.heappop(heap)
        if len(heap) == 0 and min_value < K:
            return -1
        if min_value < K:
            res = min_value + (heapq.heappop(heap) * 2)
            heapq.heappush(heap, res)
            answer += 1
        else:
            break
    
    return answer