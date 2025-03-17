def solution(name):
    answer = 0
    
    
    for idx, alphabet in enumerate(name):
        answer += min(ord(alphabet) - 65, 91 - ord(alphabet))
        print(ord(alphabet) - 65)
        print(91 - ord(alphabet))
        
        end = idx+1
        while end < len(name) and name[end] == 'A':
            end += 1
        print(idx+1, end)
        
        answer += min(end-(idx+1), )
            
    return answer