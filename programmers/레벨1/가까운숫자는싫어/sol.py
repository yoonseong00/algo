def solution(arr):

    answer = []

    for i in arr:
        if not answer:
            answer.append(i)
        else:
            if answer[-1] != i:
                answer.append(i)
            else:
                continue

    return answer

print(solution([1,1,3,3,0,1,1]))