def solution(survey, choices):

    answer = ''

    mbti = {
        'R' : 0, 'T' : 0,
        'C' : 0, 'F' : 0,
        'J' : 0, 'M' : 0,
        'A' : 0, 'N' : 0,
    }

    for mb, num in zip(survey, choices):
        if num > 4:
            mbti[mb[1]] += num - 4
        if num < 4:
            mbti[mb[0]] += 4 - num

    mbti_list = list(mbti.items())

    for i in range(0, 8, 2):
        if mbti_list[i][1] < mbti_list[i+1][1]:
            answer += mbti_list[i+1][0]
        else:
            answer += mbti_list[i][0]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))