from collections import deque
import math

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    total = sum1 + sum2

    if total % 2 == 1:
        return -1
    
    goal = total // 2
    
    max_ops = len(q1)*3

    cnt = 0
    
    while cnt <= max_ops:
        if sum1 == goal:
            return cnt
        elif sum1 > goal:
            val = q1.popleft()
            sum1 -= val
            q2.append(val)
        else:
            val = q2.popleft()
            sum2 -= val
            sum1 += val
            q1.append(val)
        cnt += 1
    
    return -1