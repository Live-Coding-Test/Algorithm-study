def solution(people, limit):
    answer = 0
    sorted_people = sorted(people)
    start = 0
    end = len(people)-1
    
    while start <= end:
        if sorted_people[start] + sorted_people[end] <= limit:
            start += 1
        end -= 1
        answer += 1
    return answer