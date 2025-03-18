def solution(routes):
    routes.sort(key=lambda x: x[1])

    count = 0
    camera = -30001

    for i in range(len(routes)):
        if routes[i][0] > camera:
            count += 1
            camera = routes[i][1]

    return count