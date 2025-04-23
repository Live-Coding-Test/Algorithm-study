import sys

input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True) 
boxes.sort(reverse=True)  

res = 0
if cranes[0] < boxes[0]:
    print(-1)
else:
    while boxes:
        for c in cranes:
            if boxes and c < boxes[-1]: # 시간초과 해결하는 한 줄..
                continue
            for b in boxes:
                if c >= b:
                    boxes.remove(b)
                    break
        res += 1
    print(res)
