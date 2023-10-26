def solution(number, limit, power):

    result = []

    for i in range(1, number+1):
        answer = 0
        for j in range(1, int(i**(0.5))+1): # 1부터 i의 제곱근까지만 돌리기
            if i % j ==0:
                answer += 1
                if j**2 != i:   # 8*8 같이 약수가 중복되는 것을 방지
                    answer += 1
            if answer > limit:  #answer가 limit보다 크면 바로 break를 하여 연산처리 줄이기
                answer = power
                break
        result.append(answer)

    return sum(result)


print(solution(5,3,2))
print(solution(10,3,2))