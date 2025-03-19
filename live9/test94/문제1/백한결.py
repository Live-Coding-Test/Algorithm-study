def solution(dirs):
    visited = set()
    current = (0, 0)

    move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

    for dir in dirs:
        x = current[0] + move[dir][0]
        y = current[1] + move[dir][1]

        if -5 <= x <= 5 and -5 <= y <= 5:
            visited.add(tuple(sorted([current, (x, y)])))
            print(visited)
            current = (x, y)

    count = len(visited)

    return count