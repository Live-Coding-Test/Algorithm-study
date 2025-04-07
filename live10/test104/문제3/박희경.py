def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    alpha = []
    for word in words:
        alpha.append(list(map(str, word.rstrip())))
        
    def dfs(word, target):
        word = list(map(str, word.rstrip()))
        
        
    
    return answer