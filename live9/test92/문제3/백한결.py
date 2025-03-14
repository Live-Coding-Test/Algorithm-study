def solution(book_time):
    books = []

    for start, end in book_time:
        books.append((hour_to_minutes(start), 1))
        books.append((hour_to_minutes(end) + 10, -1))

    books.sort()

    current_rooms = 0
    needed_rooms = 0

    for time, type in books:
        current_rooms += type
        needed_rooms = max(needed_rooms, current_rooms)

    return needed_rooms


def hour_to_minutes(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute
