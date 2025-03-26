from collections import *

def solution(s):
    answer = -1
    queue = deque(s)
    
    for i in range(len(s)):
        queue.rotate(i)
    
    def correct(arr):
        st = []
        for a in arr:
            first = st[-1]
            
    return answer