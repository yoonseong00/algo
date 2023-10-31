def solution(rank, attendance):

    result = []

    for idx , value in enumerate(rank):
        if attendance[idx] == True:
            result.append([rank[idx], idx])

    result.sort(key = lambda x : x[0])

    # print(result)

    answer = (result[0][1] * 10000) + (result[1][1] * 100) + result[2][1]

    return answer

print(solution([3, 7, 2, 5, 4, 6, 1],[False, True, True, True, True, False, False]))