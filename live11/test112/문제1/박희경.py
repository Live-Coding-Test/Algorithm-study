import sys
from collections import defaultdict

input = sys.stdin.readline

def bt(word, length):
    if length == len(word):
        print(''.join(word))
        return
    for a in alpha:
        # 해당 알파벳을 사용할 수 있다면
        if alpha[a]:
            alpha[a] -= 1
            bt(word + a, length)
            alpha[a] += 1 

n = int(input())
for _ in range(n):
    word = sorted(list(map(str, input().rstrip())))
    alpha = defaultdict(int)
    for w in word:
        alpha[w] += 1

    bt('', len(word))
