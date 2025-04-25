import sys

def main():
    input = sys.stdin.readline
    N = int(input())

    for i in range(N):
        word = str(input().strip())

        word = sorted(list(word))

        result = []
        backtracking(word, [], [False] * len(word), result)

        for r in result:
            print(r)

def backtracking(word, path, visited, result):
    if len(path) == len(word):
        result.append("".join(path))
        return

    for i in range(len(word)):
        if visited[i]:
            continue
        if i > 0 and word[i] == word[i-1] and not visited[i-1]:
            continue

        visited[i] = True
        path.append(word[i])
        backtracking(word, path, visited, result)
        path.pop()
        visited[i] = False

if __name__ == '__main__':
    main()