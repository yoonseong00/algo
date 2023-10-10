def solution(n):
    
    answer = 0

    # while n>0:                       #몫과 나머지를 활용해 구하는 방법
    #     a = n // 10 
    #     b = n % 10

    #     n = a
    #     answer += b

    for i in str(n):
        answer += int(i)
    

    return answer

print(solution(1234))
print(solution(930211))