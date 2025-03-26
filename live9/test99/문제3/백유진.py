def solution(s):
    answer = 0
    
    for i in range(len(s)):
        ns = s[i:] + s[:i]
        
        stack = []
        isValid = True
        
        for n in ns:
            if n == '(' or n == '{' or n == '[':
                stack.append(n)
            else:
                if not stack:
                    isValid = False
                    break
                top = stack[-1]
                if n == ')' and top == '(' or n == '}' and top == '{' or n == ']' and top == '[':
                    stack.pop()
                else:
                    isValid = False
                    break
        if isValid and not stack:
            answer += 1
                
    return answer