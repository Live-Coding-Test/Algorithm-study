import sys

input = sys.stdin.readline

s = list(map(str, input().rstrip()))
p = list(map(str, input().rstrip()))


i = 0  
count = 0

while i < len(p):
    max_len = 0
    
    for j in range(len(s)):
        l = 0
        while i + l < len(p) and j + l < len(s) and p[i + l] == s[j + l]:
            l += 1
        max_len = max(max_len, l)

    i += max_len
    count += 1

print(count)

"""
xy0z
zzz0yyy0xxx

abaabba
aaabbbabbbaaa
"""