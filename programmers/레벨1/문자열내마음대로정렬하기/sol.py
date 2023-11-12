def solution(strings, n):
    strings.sort()
    return strings.sort(strings, key=lambda x:x[n])