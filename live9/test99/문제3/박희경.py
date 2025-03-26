from collections import *

def is_correct(arr):
    stack = []
    for a in arr:
        if a in '([{':
            stack.append(a)
        elif a == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif a == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
        elif a == '}':
            if not stack or stack[-1] != '{':
                return False
            stack.pop()

    return not stack

def solution(s):
    answer = 0
    queue = deque(s)
    
    for _ in range(len(queue)):
        if is_correct(queue):
            answer += 1
        queue.rotate(-1)     
    return answer