def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    nlost = [l for l in lost if l not in reserve]
    nreserve = [r for r in reserve if r not in lost]
    
    answer = n - len(nlost)
    
    for l in nlost:
        if l-1 in nreserve:
            answer += 1
            nreserve.remove(l-1)
        elif l+1 in nreserve:
            answer += 1
            nreserve.remove(l+1)
            
    return answer