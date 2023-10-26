def solution(a, b):

    answer = []

    if a < b:
        for i in range(a, b+1):
            answer.append(i)

        return sum(answer)
    elif a > b:
        for i in range(b, a+1):
            answer.append(i)
        return sum(answer)
    else:
        return a


print(solution(5,3))