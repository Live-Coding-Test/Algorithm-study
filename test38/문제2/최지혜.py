N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]  # N개의 숫자를 리스트로 입력 받기

numbers.sort() # 숫자를 오름차순으로 정렬

def bt(depth):
    # 종료 조건: depth가 M에 도달하면 현재까지의 박스를 출력
    if depth == M:
        print(' '.join(map(str,box)))
        return

    for i in range(N): # 가능한 숫자들 중에서 선택하기
        if numbers[i] in box: # 이미 선택한 숫자는 건너뛰기
            continue
        box.append(numbers[i]) # 현재 숫자를 수열에 추가
        bt(depth + 1) # 재귀 호출을 통해 다음 깊이로 이동
        box.pop()

box = []
bt(0)