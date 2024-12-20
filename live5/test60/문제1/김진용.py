import sys
input = sys.stdin.readline
string = list(input().rstrip())
order = int(input())
string_2 = []

for _ in range(order):
    o = list(input().split())

    if o[0] == 'L':
        if string:
            string_2.append(string.pop())
    elif o[0] == 'D':
        if string_2:
            string.append(string_2.pop())
    elif o[0] == 'B':
        if string:
            string.pop()
    elif o[0] == 'P':
        string.append(o[1])

string.extend(reversed(string_2))
print(''.join(string))
