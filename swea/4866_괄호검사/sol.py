import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    code = list(input())

    stack = []     

    for char in code:
            if char == '(' or char == '{':
                stack.append(char)
            elif len(stack) and char ==')' and stack[-1] == '(':
                stack.pop()
            elif len(stack) and char =='}' and stack[-1] == '{':
                stack.pop()
            elif char == '}' or char == ')':
                stack.append(char)

    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    print(f'#{tc} {answer}')


