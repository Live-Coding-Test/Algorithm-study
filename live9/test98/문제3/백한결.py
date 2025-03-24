def solution(prices):
    answer = [0] * len(prices)

    stack = []

    for i, price in enumerate(prices):
        # 가격이 떨어지는 순간을 찾고 그 때까지의 시간을 계산
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # for문이 끝난 후 떨어지지 않은 가격
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - (j + 1)

    return answer