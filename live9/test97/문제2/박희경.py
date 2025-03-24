def solution(name):
    answer = 0
    
    min_move = len(name) - 1    # 한칸씩 이동하는 경우
    
    for i, char in enumerate(name):
        # 위 아래로 움직일 때
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 연속된 A 끝나는 인덱스 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        """
        len(name) - next : 'A' 구간이 끝난 후 남은 문자의 수
        1. 오른쪽으로 하나씩 가기 (최악의 경우)
        2. i까지 갔다가 → 되돌아와서(*2) → 남은 부분 끝까지 가기
        3. 뒷부분(next 이후)까지 갔다가 → 되돌아와서(*2) → 앞부분(i)까지 가기
        """
        min_move = min(min_move, 
                       2 * i + len(name) - next,    
                       i + 2 * (len(name) - next)   
                      )
        
    answer += min_move
        
    
    return answer