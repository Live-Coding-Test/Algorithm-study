"""
투포인터 -> 몇 테스트케이스에서 시간 초과
스택에 저장한 인덱스 : 아직 뒤에 있는 큰 수를 만나지 못한 인덱스
"""


def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, num in enumerate(numbers):
        # 뒤에서 큰 수 만났을 때     case2) stack = [0, 1]
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num  # 뒤에서 큰 수로 변환 case2) stack = [0]
        stack.append(idx)  # 가까이 뒤에 큰 수가 없다면

    return answer