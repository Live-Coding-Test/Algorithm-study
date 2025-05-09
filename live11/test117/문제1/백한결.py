import sys

def main():
    input = sys.stdin.readline

    N = int(input())
    towers = list(map(int, input().split()))
    stack = []
    result = []

    for i in range(len(towers)):
        while stack and towers[stack[-1]] < towers[i]:
            stack.pop()

        if stack:
            result.append(stack[-1] + 1)
        else:
            result.append(0)

        stack.append(i)

    print(*result)

if __name__ == '__main__':
    main()