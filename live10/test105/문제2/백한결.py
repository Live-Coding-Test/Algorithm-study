from collections import defaultdict

def main():
    n = int(input())
    premise = defaultdict(list)

    for _ in range(n):
        a, b = input().strip().split(" is ")
        premise[a].append(b)

    m = int(input())
    questions = [input().strip().split(" is ") for _ in range(m)]

    for a, b in questions:
        visited = set()

        if dfs(premise, a, b, visited):
            print("T")
        else:
            print("F")

def dfs(graph, start, target, visited):
    if start == target:
        return True
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True

    return False

if __name__ == "__main__":
    main()