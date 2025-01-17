def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += str(i)*(food[i]//2) # 반씩 분배
    temp = ''.join(reversed(list(answer))) # 왼쪽 선수의 reverse가 오른쪽 선수가 먹는 것
    return answer+'0'+temp