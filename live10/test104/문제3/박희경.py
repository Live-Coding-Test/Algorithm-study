from collections import *

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    while q:
        now, cnt = q.popleft()
        if now == target:
            return cnt
        
        for word in words:
            tmp_cnt = 0
            for i in range(len(now)): 
                if now[i] != word[i]:
                    tmp_cnt += 1
            if tmp_cnt == 1: 
                q.append([word, cnt + 1])
