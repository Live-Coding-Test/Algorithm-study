def solution(routes):
    # 진출 지점을 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    
    # 첫 번째 카메라 설치
    camera = -30001  # 모든 경로는 -30,000 ~ 30,000 이므로 초기값 설정
    count = 0

    for route in routes:
        if camera < route[0]:  # 현재 카메라가 진입 지점보다 앞에 있다면 새로 설치
            camera = route[1]  # 새로운 카메라는 해당 차량의 진출 지점에 설치
            count += 1  # 카메라 개수 증가

    return count
