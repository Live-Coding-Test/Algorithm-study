import heapq

def solution(book_time):
    answer = 0
    # book_time.sort()
    
    def change_minute(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
    
    heap = list([change_minute(start), change_minute(end) + 10] for start, end in book_time)
    # 	[[850, 1160], [860, 920], [900, 1020], [1000, 1100], [1100, 1280]]
    
    heapq.heapify(heap)
    print(heap)
    
    while heap:
        start, end = heap[0]
        print(heap)
        next_start, next_end = heapq.heappop(heap)
        if start <= next_start <= end:
            answer += 1
            start = next_start
            end = next_end
        else: 
            break
        
    
    return answer