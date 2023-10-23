# 선분의 길이가 [-2,0] 처럼 주어지고 겹치는 부분찾기
# 그러면.. 리스트의 범위만큼 숫자들을 배열해서 겹치는 부분의 숫자를 또 새로운 리스트에 넣어서 len를 구하면 되겠지?

def solution(lines):
    # lines 각 인덱스에 있는 리스트
    line1 = lines[0]
    line2 = lines[1]
    line3 = lines[2]
    # 리스트에 있는 0번째부터 1번째 인덱스까지의 범위만큼 리스트 출력
    list_1 = [i for i in range(int(line1[0]), int(line1[1]+1))]
    list_2 = [i for i in range(int(line2[0]), int(line2[1])+1)]
    list_3 = [i for i in range(int(line3[0]), int(line3[1])+1)]
    # 교집합 찾기
    answer1 = set(list_1) & set(list_2)
    answer2 = set(list_1) & set(list_3)
    answer3 = set(list_2) & set(list_3)
    answer4 = set(list_1) & set(list_2) & set(list_3)



    # 겹치는 수가 하나면 겹치는 선이 아니므로 제외
    if len(answer1) < 2:   
        answer1.clear()
    if len(answer2) < 2:
        answer2.clear()
    if len(answer3) < 2:
        answer3.clear()
    if len(answer4) < 2:
        answer4.clear()


    result = []
    # 만약 겹치는 케이스가 2개 이상이면 result에 append
    if len(answer1) >= 2:
        for i in answer1:
            result.append(i)
    if len(answer2) >= 2:
        for i in answer2:
            result.append(i)
    if len(answer3) >= 2:
        for i in answer3:
            result.append(i)
        

    # 결과값에 값이 중복되면 안되니까 set

    answer = 0
    # res에 값이 있다면
    if len(res) > 0:
        if len(res) % 2 == 0:           #만약 길이가 짝수면 절반 만큼이 걸친건 절반이 길이
            answer += (len(res) // 2)
        else:
         answer += len(res) +  -1

    return answer
    

print(solution([[0, 1], [2, 5], [3, 9]]))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))
print(solution([[0, 4], [3, 8], [5, 8]]))
print(solution([[0,3], [2, 8], [5, 8]]))