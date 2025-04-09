from collections import deque

def isAdjacent(word1, word2):
    diff_count = 0
    for a, b in zip(word1, word2):
        if a != b:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = set()
    queue = deque()
    queue.append((begin, 0))  # 현재 단어, count 수

    while queue:
        current, depth = queue.popleft()
        if current == target:
            return depth

        for word in words:
            if word not in visited and isAdjacent(current, word):
                visited.add(word)
                queue.append((word, depth + 1))

    return 0