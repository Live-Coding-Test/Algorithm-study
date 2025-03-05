def solution(dirs):
    answer = 0
    x, y = 0, 0
    udrl = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    history = set()
    
    for dir in dirs:
        dy = udrl[dir][0]
        dx = udrl[dir][1]
        
        ny = y + dy
        nx = x + dx
        
        if -5 <= ny <=5 and -5 <= nx <= 5:
            history.add(((ny, nx),(y, x)))
            history.add(((y, x),(ny, nx)))
            
            y = ny
            x = nx
            
    print(history)
            
    return len(history)/2