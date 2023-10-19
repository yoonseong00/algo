import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    string = input()
    stack = []

    for i in string:
    
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

    print(f'#{tc} {len(stack)}') 

