import heapq

def time_to_minute(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(book_time):
    
    book = sorted([[time_to_minute(start), time_to_minute(end) + 10] for start, end in book_time])
    
    room = []
    for start, end in book:
        if room:
            early_end = room[0]   # 가장 빠른 퇴실 시간 
            if start >= early_end:   # 입실 시간이 가장 빠른 퇴실 시간 이후라면 갱신
                heapq.heappop(room)
        heapq.heappush(room, end)

    return len(room)