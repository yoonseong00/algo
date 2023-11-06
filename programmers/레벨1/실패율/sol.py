def solution(N, stages):
    stage_len = len(stages)
    answer = []

    for i in range(1, N+1):
        count = 0
        for j in range(len(stages)):
            if stages[j] == i:
                count += 1
        if count > 0:
            answer.append(count/stage_len)
        else:
            answer.append(0)
        stage_len = stage_len - count


    a = sorted(answer, reverse=True)

    result = []

    for j in range(len(answer)):
        result.append(answer.index(a[j])+1)
        answer[answer.index(a[j])] = 1000000
    
    return result



print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))