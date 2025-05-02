import sys

def main():
    input = sys.stdin.readline
    size = int(input())
    A = list(map(int, input().split()))
    result = [-1] * size
    stack = []

    for i in range(size):
        while stack and A[stack[-1]] < A[i]:
            index = stack.pop()
            result[index] = A[i]
        stack.append(i)

    print(*result)

if __name__ == '__main__':
    main()