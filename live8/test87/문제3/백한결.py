def solution(dirs):
    x, y = 0, 0
    visit_route = set()

    moving = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

    for route in dirs:
        next_x, next_y = x + moving[route][0], y + moving[route][1]

        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            visit_route.add(((x, y), (next_x, next_y)))
            visit_route.add(((next_x, next_y), (x, y)))

            x, y = next_x, next_y

    return len(visit_route) // 2