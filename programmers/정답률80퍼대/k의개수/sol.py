from collections import Counter

def solution(i, j, k):
    answer = 0
    num_list = []

    for i in range(i, j+1):
        i = str(i)
        num_list.append(i)
    
    k = str(k)
    for j in num_list:
        num = Counter(j)
        answer += num[k]

    return answer

print(solution(1,13,1))