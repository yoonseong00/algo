# 1,2 1,3 2,3 부분에서 겹치는 선분(점2개씩의 묶음)을 구하기
# 만약 3개의 리스트에서 동시에 겹치는 부분은 빼주기

def solution(lines):

    lines = sorted(lines) # 가장 작은 곳에서부터 정렬

    dic = {}

    for start, end in lines:
        # print(start)
        # print(end)
        while start < end:  #시작점부터 끝점까지의 길이 1만큼씩을 dic 추가
            if (start, start+1) not in dic: # 만약 start의 범위가 dic 안에 없으면 값 추가
                dic[(start, start+1)] = 1
            else:                          # 값이 있다는 말 = 겹치는 점이다 ---> 이렇게 3개가 겹치는 걸 굳이 빼주거나 할 필요가 사라짐
                dic[(start, start+1)] += 1
            start += 1
        
    count = 0

    for i in dic.values():
        if i> 1:    # dic.value 값 중 겹치는 지점 즉, 2 이상인 것들을 count

            count += 1

    return count


print(solution([[0, 5], [3, 9], [1, 10]]))