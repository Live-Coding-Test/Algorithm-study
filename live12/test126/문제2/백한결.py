def solution(n, info):
    maxDiff = -1
    answer = [-1]

    # DFS로 점수 구간을 하나씩 탐색하면서 라이언의 경우를 모두 탐색
    def dfs(index, arrowsLeft, ryanShots):
        nonlocal maxDiff, answer

        # 모든 구간을 다 고려했을 때
        if index == 11:
            if arrowsLeft > 0:
                ryanShots[10] += arrowsLeft

            ryanScore = 0
            apeachScore = 0

            # 각 점수 계산
            for i in range(11):
                if info[i] == 0 and ryanShots[i] == 0:
                    continue
                if ryanShots[i] > info[i]:
                    ryanScore += 10 - i
                else:
                    apeachScore += 10 - i

            # 라이언이 이긴 경우
            if ryanScore > apeachScore:
                diff = ryanScore - apeachScore
                if diff > maxDiff:
                    maxDiff = diff
                    answer = ryanShots[:]
                elif diff == maxDiff:
                    for i in range(10, -1, -1):
                        if ryanShots[i] > answer[i]:
                            answer = ryanShots[:]
                            break
                        elif ryanShots[i] < answer[i]:
                            break

            if arrowsLeft > 0:
                ryanShots[10] -= arrowsLeft
            return

        # 현재 점수를 얻기 위해 필요한 화살 수
        neededArrows = info[index] + 1
        if neededArrows <= arrowsLeft:
            # 이 점수를 가져가는 경우
            ryanShots[index] = neededArrows
            dfs(index + 1, arrowsLeft - neededArrows, ryanShots)
            ryanShots[index] = 0

        # 이 점수를 포기하는 경우
        dfs(index + 1, arrowsLeft, ryanShots)

    dfs(0, n, [0] * 11)
    return answer