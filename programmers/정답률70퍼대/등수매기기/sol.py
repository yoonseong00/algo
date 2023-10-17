def solution(score):
    answer = []

    for i in range(len(score)):
        score_sum = score[i][0] + score[i][1]
        mean = score_sum / 2

        answer.append(mean)

        sorted_mean = sorted(answer, reverse = True)# 점수가 높은순으로 reverse = True (내림차순) 정렬
        
        ranks = [sorted_mean.index(s) + 1 for s in answer] # 등수는 1부터 시작되니까 + 1 넣어줌 
    
    return ranks

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]	))