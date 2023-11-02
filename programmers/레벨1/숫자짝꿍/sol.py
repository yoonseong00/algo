# def solution(X, Y):
#     answer = ''

#     for i in x:
#         if i in y:
#             answer += i
#             y.replace(i, ' ')

#     result = sorted(answer, reverse=True)

#     count = ''

#     for j in result:
#         count += j

    
#     if len(result) == 0:
#         return '-1'
#     elif result[0] == '0':
#         return '0'
#     else:
#         return count

def solution(X, Y):
    answer = []

    for i in (set(X)&set(Y)):
        for j in range(min(X.count(i), Y.count(i))):
            answer.append(i)   

    result = sorted(answer, reverse=True)
    
    if len(result) == 0:
        return '-1'
    elif result[0] == '0':
        return '0'
    else:
        return ''.join(result)

print(solution("12321","42531"))