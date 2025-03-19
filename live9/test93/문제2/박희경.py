def solution(name):
    answer = 0
    
    # 기본 최소 좌우 이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    for i, alpha in enumerate(name):
        answer += min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1)

        # 연속된 A의 끝나는 위치 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min([
                        min_move,                     # 기존 오른쪽으로 끝까지 가는 경우
                        2 * i + len(name) - next,     # 처음부터 i까지 갔다가 뒤로 "돌아가기(*2)"
                        i + 2 * (len(name) - next)    # A 지나서 끝까지 갔다가 "돌아오기(*2)"
                    ])
        
    answer += min_move
    return answer