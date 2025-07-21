from collections import *

def solution(n, info):
    answer = []
    
    q = deque()
    q.append((0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))   # 현재 과녁, 상황
    max_gap = 0
    
    while q:
        score, arrow = q.popleft()
        
        if sum(arrow) == n:
            apeach, ryon = 0, 0
            for i in range(11):
                if info[i] != 0 or arrow[i] != 0:
                    if info[i] >= arrow[i]:
                        apeach += 10 - i 
                    else: 
                        ryon += 10 - i
            if apeach < ryon:
                gap = ryon - apeach
                if max_gap > gap: 
                    continue
                if max_gap < gap:
                    max_gap = gap
                    answer.clear
                answer.append(arrow)
    ... 
    return answer