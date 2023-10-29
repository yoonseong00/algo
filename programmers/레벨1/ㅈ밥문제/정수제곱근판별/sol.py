def solution(n):
    answer = 0

    if n % (n**(0.5)) == 0:
        answer = ((n**(0.5))+1)**2
    else:
        answer = -1
    return answer