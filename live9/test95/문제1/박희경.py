def solution(k, dungeons):
    dungeons = [d for d in dungeons if k >= d[0]]

    def calculate_fatigue(dungeons, tmp, cnt):
        max_cnt = cnt
        for r, c in dungeons:
            if r <= tmp:
                new_dungeons = dungeons[:] # 복사
                new_dungeons.remove([r, c]) 
                max_cnt = max(max_cnt, calculate_fatigue(new_dungeons, tmp - c, cnt + 1))
        return max_cnt

    
    return calculate_fatigue(dungeons, k, 0)