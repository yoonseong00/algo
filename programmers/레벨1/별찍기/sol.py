def solution(a, b):
    a, b = map(int, input().strip().split(' '))
    
    answer = ('*'*a + '\n')*b

    print(answer)

print(solution(5,3))
