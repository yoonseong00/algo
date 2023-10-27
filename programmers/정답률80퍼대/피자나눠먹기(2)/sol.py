def solution(n):
    for i in range(6,606,6):
        if i%n == 0:
            answer = i/6
            break

    return answer