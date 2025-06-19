import sys

def main():
    input = sys.stdin.readline

    N = int(input())

    result = []

    def dfs(num):
        result.append(num)
        last_digit = num % 10
        for i in range(last_digit):
            dfs(num * 10 + i)


if __name__ == '__main__':
    main()