def solution(s):
    count = 0

    rightGaulHoList = ["()", "[]", "{}"]

    for i in range(len(s)):
        stack = []
        rotated = s[i:] + s[:i]

        print(rotated)

        for j in rotated:
            if j == "(" or j == "[" or j == "{":
                stack.append(j)

            elif j == ")" or j == "]" or j == "}":
                if stack:
                    total = stack[-1] + j

                    if total == "()" or total == "[]" or total == "{}":
                        count += 1
                else:
                    break

    return count