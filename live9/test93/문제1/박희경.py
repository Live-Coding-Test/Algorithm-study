"""
1 (st = [1]) -> 9 (st = [9]) -> 2 -> 4 (st = [9, 4])
"""
def solution(number, k):
    answer = 0
    number = list(map(str, number.rstrip()))
    
    stack = []

    for num in number:
        if not stack:
            stack.append(num)
            continue
        if k > 0:
            while stack[-1] < num:  # 다음 수가 더 클 때
                stack.pop()
                k -= 1
                if not stack or k <= 0:
                    break
        stack.append(num)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)