def solution(name):
    upDownmove = 0

    # 조이스틱 위 아래 (최솟값)
    for spell in name:
        upDownmove += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)

    # 조이스틱 오 왼
    # 조이스틱을 오른쪽으로만 계속 움직이는 경우
    rightLeftmove = len(name) - 1

    # 조이스틱으로 오른쪽을 가다가 'A'를 만난 경우
    for i in range(len(name)):
        # 조이스틱 움직이는 횟수
        next = i + 1
        while len(name) > next and name[next] == 'A':
            next += 1

        # 오른쪽으로 간 횟수, 오른쪽으로 가다가 A를 만나기 전까지의 움직임 횟수 중 최소의 2배 (앞으로 갔다가 뒤로 이동)
        # 오른쪽으로 간 횟수, 오른쪽으로 가다가 A를 만나기 전까지의 움직임 횟수 중 최대
        move = min(i, len(name) - next) * 2 + max(i, len(name) - next)
        rightLeftmove = min(rightLeftmove, move)

    count = upDownmove + rightLeftmove

    return count