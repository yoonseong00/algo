def solution(slic, n):

    if n % slic != 0:
        return 1 + (n // slic)
    else:
        return n // slic