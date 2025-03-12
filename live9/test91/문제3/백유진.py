def solution(answers):
    answer = []
    
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    result1 = 0
    result2 = 0
    result3 = 0
    
    for idx, ans in enumerate(answers):
        print(ans)
        if ans == arr1[idx%5]:
            result1 += 1
        if ans == arr2[idx%8]:
            result2 += 1
        if ans == arr3[idx%10]:
            result3 += 1
            
    max_score = max(result1, result2, result3)
    
    if result1 == max_score:
        answer.append(1)
    if result2 == max_score:
        answer.append(2)
    if result3 == max_score:
        answer.append(3)
    
    return answer