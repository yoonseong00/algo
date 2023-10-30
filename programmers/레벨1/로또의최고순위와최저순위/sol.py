def solution(lottos, win_nums):

    lotto = [6,6,5,4,3,2,1]

    count = lottos.count(0)

    answer = 0

    for i in lottos:
        if i in win_nums:
            answer += 1

    return lotto[count + answer],lotto[answer]