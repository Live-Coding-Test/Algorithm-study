n, k = map(int, input().split())
result = 0
while n != k:
    if (n>k):
        n -= 1
        result += 1
    elif (n<k):
        n -= 1
        result += 1
        n *= 2
