from itertools import permutations

def solution(k, dungeons):
    answer = float("-inf")
    
    for dungeon in permutations(dungeons, len(dungeons)):
        temp_k = k
        max = 0
        for min_p, minus_p in dungeon:
            if temp_k >= min_p:
                temp_k -= minus_p
                max += 1
        if max > answer:
            answer = max
    return answer