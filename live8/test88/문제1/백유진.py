def solution(sequence, k):
    answer = []
    
    start = 0
    end = 0
    
    min = float("inf")
    
    cum_sum = sequence[0]
    
    while end < len(sequence):
        if cum_sum < k:
            end += 1
            if end < len(sequence):
                cum_sum += sequence[end]
        elif cum_sum > k:
            cum_sum -= sequence[start]
            start += 1
        else:
            if end - start < min:
                min = end - start
                answer = [start, end]
            
            cum_sum -= sequence[start]
            start += 1
        
    return answer