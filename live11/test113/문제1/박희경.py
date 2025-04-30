import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    number = []
    for _ in range(n):
        number.append(list(map(str, input().rstrip())))
    number.sort()
    
    res = "YES"
    for k in range(len(number) - 1):
        idx = 0
        while number[k][idx] == number[k+1][idx]:
            idx += 1
            if idx >= min(len(number[k]), len(number[k+1])):
                res = 'NO'
                break
            

    print(res)
