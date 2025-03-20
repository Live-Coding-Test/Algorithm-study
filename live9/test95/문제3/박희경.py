# 처음 푼 풀이
from itertools import *

def solution(brown, yellow):
    answer = []
    yellow_list = set()
    if yellow == 1: yellow_list.add(1)
    for i in range(1, yellow // 2 + 1):
        if yellow % i == 0:
            yellow_list.add(i)
            yellow_list.add(yellow // i)
    
    for x, y in product(yellow_list, repeat=2):
        if x * y == yellow and x >= y:
            if x * 2 + y * 2 + 4 == brown:
                answer.append(x + 2)
                answer.append(y + 2)
    
    return answer

# 다른 풀이 보니 중복 순열을 굳이 쓸 필요 없음
def solution(brown, yellow):
 for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            if (i + yellow // i) * 2 == brown - 4:
                return [yellow // i + 2, i + 2]