def solution(people, limit):
    answer = 0
    people.sort()

    start, end = 0, len(people) - 1
    while start < end:
        mid = (start + end) // 2
        total = people[start] + people[mid]
        if total > limit:
            mid = end - 1
        else:
            mid = start + 1

    return answer