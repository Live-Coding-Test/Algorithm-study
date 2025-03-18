def solution(dirs):
    answer = set()
    
    move = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }

    x, y = 0, 0
    for dir in dirs:
        nx, ny = x + move[dir][0], y + move[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x, y = nx, ny
        
    return len(answer) // 2