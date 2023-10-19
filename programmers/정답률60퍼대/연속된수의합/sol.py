def solution(num, total):   #num은 리스트 인덱스 갯수   total은 내가 만들어야할 숫자

    # 결과 리스트의 인덱스 개수가 짝수일땐 total/num이 가운데 있다.
    average = total // num
    #홀수이면... 
    # 3번째 예시를 보면 몫이 2번째 몫 = 3
    # 4번째 예시를 보면 몫이 3번째 아 왜 다르냐 몫 = 1

    # 맨 왼쪽: 평균보다 1이 작음    #맨 오른쪽: 평균보다 2가큼
    # 맨 왼쪽: 평균보다 2가 작음    #맨 오른쪽: 평균보다 2가큼

    #average - (num-1)//2 일단 얘가 왼쪽 그러면 부호 바꿔서 오른쪽도?
    #안되네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    #average + (num+2)//2 얘가 오른쪽

    return [i for i in range(average - (num-1)//2, average + (num+2)//2)]

print(solution(3, 12))

def solution(num, total):
    num_total = 0
    for i in range(num):
        num_total += i
    n = int((total - num_total) / num)

    answer = []
    for i in range(n, n+num):
        answer.append(i)

    return answer