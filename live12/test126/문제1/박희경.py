from itertools import *

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def solution(numbers):
    answer = 0
    num_set = set()
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            num_set.add(num)
            
    for p in num_set: 
        if is_prime(p): 
            answer += 1
    
    return answer