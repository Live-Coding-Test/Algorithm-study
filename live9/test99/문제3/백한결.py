def solution(s):
    count = 0

    rightGaulHoList = ["()", "[]", "{}"]

    for i in range(len(s)):
        stack = []
        rotated = s[i:] + s[:i]

        isPerfect = False

        for j in rotated:
            if j == "(" or j == "[" or j == "{":
                stack.append(j)

            elif j == ")" or j == "]" or j == "}":
                if stack:
                    total = stack[-1] + j

                    if total in rightGaulHoList:
                        stack.pop()
                        isPerfect = True
                    else:
                        isPerfect = False
                        break

                else:
                    isPerfect = False
                    break

        if isPerfect and not stack:
            count += 1

    return count