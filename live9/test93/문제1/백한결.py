def solution(number, k):
    max_num = []

    for i in number:
        while max_num and k > 0 and max_num[-1] < i:
            max_num.pop()
            k -= 1
        max_num.append(i)

    answer = ''.join(max_num[:len(number) - k])

    return answer