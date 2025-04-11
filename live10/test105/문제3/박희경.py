def solution(order):
    i = 0
    stack = []
    
    for box in range(1, len(order) + 1):
        if box == order[i]:
            i += 1
        else:
            stack.append(box)
        while stack and stack[-1] == order[i]:
            stack.pop()
            i += 1
    
    return i