# def solution(n):

#     answer = 0

#     for i in range(1, n+1):
#         if n % i == 0:
#             answer += 1

#     return answer

def solution(n): # 효율성을 위해 위처럼 1~n을 계산하는 것이 아닌 절반만 계산해서 2배를 하는 방법

    answer = 0

    for num in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            answer += 2

        if num * num == n:
            answer -= 1
    return answer


print(solution(20))