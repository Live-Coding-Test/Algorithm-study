import sys
from itertools import combinations


def main():
    input = sys.stdin.readline

    expression = str(input().strip())
    stack = []
    pair = []

    for index, char in enumerate(expression):
        if char == '(':
            stack.append(index)
        elif char == ')':
            start = stack.pop()
            pair.append((start, index))

    result = set()

    for i in range(1, len(pair)+1):
        for comb in combinations(pair, i):
            temp = list(expression)
            for s, e in comb:
                temp[s] = temp[e] = ''
            result.add(''.join(temp))

    for res in sorted(result):
        print(res)

if __name__ == '__main__':
    main()