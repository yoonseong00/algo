def solution(numlist, n): # numlist = 숫자 배열 리스트, n = 기준(n에서 가까운 수부터 나열 if 4기준 3,5라면 큰 수인 5를 우선 배열)
    
    return sorted(numlist , key = lambda x : (abs(x-n), -x)) 
    # 오름차순으로 정렬을 하고 절대값(거리)가 작은 순대로 정렬, 만약 숫자가 같다면 x값이 더 큰 값이 앞으로 오게끔 설정

                
print(solution([1,2,3,4,5,6], 4))
print(solution([10000,20,36,47,40,6,10,7000], 30))



def solution(numlist, n):
    answer = []
    my_list = []
    numlist2 = numlist
    for i in numlist:
        my_list.append(abs(i - n))

    my_list = sorted(my_list)

    for i in range(len(numlist)):
        if (n + my_list[i]) in numlist2:
            answer.append(n + my_list[i])
            numlist2.remove(n + my_list[i])
        elif (n - my_list[i]) in numlist2:
            answer.append(n - my_list[i])
    return answer