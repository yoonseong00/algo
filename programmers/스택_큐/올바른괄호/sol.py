def solution(s):

    stack = []

    code = list(s)

    for char in code:
        if char == '(':
            stack.append(char)
        elif len(stack) and char ==')' and stack[-1] == '(':
            stack.pop()
        elif char == ')':
            stack.append(char)

    if len(stack) == 0:
        return True
    else:
        return False

# print(solution("()()"))
print(solution(")()("))