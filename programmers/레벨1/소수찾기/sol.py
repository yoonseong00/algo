from itertools import permutations

def sosu(num):
    if num <2:
        return False
    
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False

    return True

def solution(n):
    answer = 0

    for i in range(1, n+1):
        if sosu(i):
            answer += 1

    return answer