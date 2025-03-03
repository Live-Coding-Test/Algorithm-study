def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[j] > numbers[i]:
                answer.append(numbers[j])
                break
        if len(answer) != i+1:
            answer.append(-1)
            
    return answer