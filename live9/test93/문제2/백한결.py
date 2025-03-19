def solution(name):
    count = 0

    for a in name:
        count += min(ord(a) - ord('A'), ord('Z') - ord(a) + 1)

    min_move = len(name) - 1

    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        move = min(i, len(name) - next) * 2 + max(i, len(name) - next)
        min_move = min(min_move, move)

    count += min_move

    return count


print(solution("JEROEN"))
