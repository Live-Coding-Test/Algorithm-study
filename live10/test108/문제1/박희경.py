"""
최소 값이니까 큰 값을 빼는 것이 최선의 방법 => 더하기 먼저 
"""

import sys

input = sys.stdin.readline

ex = input()
separate_ex = ex.split('-')

result = 0
x =  sum(map(int, separate_ex[0].split('+')))   # map으로 합 구하기 
result += x

for x in separate_ex[1:]:
    x = sum(map(int, x.split('+')))
    result -= x
print(result)
