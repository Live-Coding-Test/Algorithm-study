def solution(answers):
    answer = []
    
    one = [1, 2, 3, 4, 5] * 10000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 10000
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000
    
    score = {1: 0, 2: 0, 3: 0}
    
    for i in range(len(answers)):
        if one[i] == answers[i]:
            score[1] += 1
        if two[i] == answers[i]:
            score[2] += 1
        if three[i] == answers[i]:
            score[3] += 1
    
    score = sorted(score.items(), key=lambda x: x[1], reverse=True)
    
    high_score = score[0][1]
    for s in score:
        if s[1] >= high_score:
            answer.append(s[0])
        
    return answer