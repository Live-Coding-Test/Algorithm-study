import heapq

def solution(book_time):

    def hour_to_minute(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
    
    book = sorted(list([hour_to_minute(start), hour_to_minute(end) + 10] for start, end in book_time))
    
    room = []
    for start, end in book:
        #  현재 예약 시작 시간보다 가장 빨리 퇴실 시간 + 10분보다 이후라면 예약 가능 (갱신)
        if room and start >= room[0]:   
            heapq.heappop(room)
    
        # 현재 예약 종료 시간을 힙에 추가 (새로운 방 사용)
        heapq.heappush(room, end)
        
    return len(room)