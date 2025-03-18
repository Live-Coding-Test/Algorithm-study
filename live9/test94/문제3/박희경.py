def solution(stones, k):
    answer = 0
    
    i, j = 0, 1
    while j < len(stones) and j-i <= k:
        if stones[j] == 0:
            j += 1
        i += 1
        j += 1
        # for i in range(len(stones)):
        #     if stones[i] == 0:
        #         jump += 1
        #         i += jump - 1
        #     else:
        #         stones[i] -= 1
        answer += 1
    # print(stones)
    
    return answer