def solution(A, B):

    for i in range(len(A)):
        if A == B:
            return i
        else:
            A = A[-1] + A[:-1]
    return -1
    

print(solution('hello', 'ohell'))
print(solution('apple', 'elppa'))
print(solution('atat', 'tata'))
print(solution('abc', 'abc'))