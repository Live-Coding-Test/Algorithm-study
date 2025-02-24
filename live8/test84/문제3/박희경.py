def solution(skill, skill_trees):
    answer = 0

    def is_possible(stack, skill):
        i, j = 0, 0
        while i < len(stack) and j < len(skill):
            if stack[i] == skill[j]:
                i += 1
                j += 1
            else:
                return False
        return True

    for skills in skill_trees:
        stack = []
        for s in skills:
            if s in skill:  # 순서가 중요한 스킬만
                stack.append(s)
        if is_possible(stack, skill):
            answer += 1
    return answer
