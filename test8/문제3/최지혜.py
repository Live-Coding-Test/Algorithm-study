def factorial(n): # 팩토리얼 함수
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

t = int(input())

for _ in range(t):
    n, m = map(int, input().split()) # 테스트케이스 입력받기
    bridge = factorial(m) // (factorial(n) * factorial(m - n)) # mCn 공식 적용
    print(bridge)