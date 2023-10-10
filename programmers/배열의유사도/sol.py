def solution(s1, s2):
    
    a = set(s1) & set(s2)

    answer = len(a)

    return answer

print(solution(["a", "b", "c"],["com", "b", "d", "p", "c"]))