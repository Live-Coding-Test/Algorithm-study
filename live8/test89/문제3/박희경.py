def solution(numbers):
    numbers_str = list(map(str, numbers))

    # numbers의 원소는 1,000 이하이므로 3번 반복
    numbers_str = sorted(numbers_str, key=lambda x: x * 3, reverse=True)

    # numbers = [0, 0, 0] 라면 -> '000' 반환
    return str(int(''.join(numbers_str)))