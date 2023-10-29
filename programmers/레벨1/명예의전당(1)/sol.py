def solution(k, score):

    answer = []

    honor = []

    for i in score:
        if len(honor) < k:
            honor.append(i)
        else:
            if min(honor) < i:
                honor.remove(min(honor))
                honor.append(i)
        answer.append(min(honor))

    return answer