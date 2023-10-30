def solution(k, m, score): 
    # k = socre 중 가장 높은 수 , m  =  묶어야할 범위

    answer = 0


    score.sort(reverse = True)

    for i in range(0, len(score), m):
        if len(score[i:i+m]) == m:
            answer += min(score[i:i+m]) * m

    return answer

print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))