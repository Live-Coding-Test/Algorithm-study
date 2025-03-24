def solution(distance, rocks, n):
    answer = 0
    
    rocks.append(distance)
    rocks.sort()
    
    start, end = 0, distance
    while start <= end:
        mid = (start + end) // 2    # 최소 거리 
        
        current = 0     # 출발지점
        remove_cnt = 0
        
        for rock in rocks:
            diff = rock - current   # 바위 간의 거리 
            if diff < mid:          # 최소 거리로 설정한 값(mid)보다 작다면 제거하기
                remove_cnt += 1
            else:
                current = rock
            if remove_cnt > n:
                break
        
        if remove_cnt > n:  # mid 값이 컸다는 의미니까
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
            
                
    
    return answer