from collections import *

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    q1_sum = sum(q1)
    q2_sum = sum(q2)

    if (q1_sum + q2_sum) % 2 != 0:
        return -1
    max_try = len(q1) * 3
    
    while q1 and q2 and answer <= max_try:
        if q1_sum == q2_sum:
            break
        elif q1_sum > q2_sum:
            q1_sum -= q1[0]
            q2.append(q1[0])
            q2_sum += q1.popleft()
        else:
            q2_sum -= q2[0]
            q1.append(q2[0])
            q1_sum += q2.popleft()
        answer += 1
    
    if q1_sum != q2_sum:
        return -1
    return answer