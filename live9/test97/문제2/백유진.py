def solution(name):
    answer = 0
    
    min_cursor = len(name) - 1
    
    for idx, alphabet in enumerate(name):
        answer += min(ord(alphabet) - 65, 91 - ord(alphabet))
        
        end = idx+1
        while end < len(name) and name[end] == 'A':
            end += 1
        min_cursor = min(min_cursor, idx*2 + len(name)-end, (len(name)-end)*2 + idx)
        
    answer += min_cursor
    
    return answer