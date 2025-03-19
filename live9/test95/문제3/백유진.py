from itertools import combinations
def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    
    for h in range(1, total+1):
        if total%h == 0:
            w = total//h
            if (w-2)*(h-2) == yellow:
                return [w, h]
    
    return answer