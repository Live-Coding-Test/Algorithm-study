def solution(lands):
    dp = lands[0]

    for i in range(1, len(lands)):
        new_dp = [0] * 4
        for j in range(4):
            # 같은 열이 아닌 요소 중 가장 큰 값과 현재 값과 더하기 (누적해서)
            new_dp[j] = lands[i][j] + max(dp[k] for k in range(4) if k != j)
        dp = new_dp

    return max(dp)