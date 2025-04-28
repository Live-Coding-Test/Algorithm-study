import sys

input = sys.stdin.readline

result = 0
def bt(word, length):
    global result
    if len(word) == length:
        if word == s:
            result = 1
            return
        return
    if word[-1] == 'A':
        bt(word[:-1], length)
    if word[0] == 'B': 
        bt(word[1:][::-1], length)
    
s = input().rstrip()
t = input().rstrip()
bt(t, len(s))

print(result)
"""
A
BABA

A
ABBA
"""