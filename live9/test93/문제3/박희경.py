def solution(routes):
    answer = 0
    camera = float('-inf')
    
    routes.sort(key=lambda x: x[1])
    for i in range(len(routes)):
        if routes[i][0] > camera:   # 진입 지점이 카메라보다 뒤에 있는 경우 카메라 추가해야 함 
            answer += 1
            camera = routes[i][1]   # 진출 지점에 카메라 설치
    return answer