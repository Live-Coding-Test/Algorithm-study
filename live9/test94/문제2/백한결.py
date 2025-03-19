import heapq

def solution(book_time):

    book_time.sort()

    start = []
    end = []

    for time in book_time:
        start.append(hourToMinute(time[0]))
        end.append(hourToMinute(time[1]) + 10)

    rooms = []
    heapq.heapify(rooms)

    for i in range(len(book_time)):
        if rooms and rooms[0] <= start[i]:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end[i])

    return len(rooms)

def hourToMinute(time):
    hour, minute = time.split(":")

    minutes = int(hour) * 60 + int(minute)

    return minutes