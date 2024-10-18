n = int(input())
ary = list(map(int, input().split()))
x = int(input())

ary.sort()
# print(ary)

a = 0
b = len(ary) - 1
# print(a, b)

result = 0

while a < b:
    if ary[a] + ary[b] == x:
        result += 1
        a += 1
        b -= 1
    elif ary[a] + ary[b] < x:
        a += 1
    else:
        b -= 1
print(result)