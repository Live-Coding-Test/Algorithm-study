import heapq

def solution(book_time):
    reservations = []
    for start, end in book_time:
        h, m = map(int, start.split(":"))
        start_min =  h * 60 + m
        h, m = map(int, end.split(":"))
        end_min = h * 60 + m + 10  # 청소 시간 포함
        reservations.append((start_min, end_min))
    reservations.sort()
    
    rooms = []
    
    for start, end in reservations:
        if rooms and rooms[0] <= start:
            # 기존 방 사용 가능
            heapq.heappop(rooms)
        # 새 방 배정 (또는 기존 방 갱신)
        heapq.heappush(rooms, end)
    
    return len(rooms)
