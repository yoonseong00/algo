def solution(name, yearning, photo):

    answer = []

    memory = dict(zip(name, yearning))  # name과yearning을 dict으로 이름과 값으로 묶기

    for i in photo:

        point = 0

        for pho in i:

            point += memory.get(pho, 0) # 만약 photo에 있는 값이 name에 포함이 된다면 그 인덱스에 맞는 yearning에 있는 점수를 point에 추가

        answer.append(point)    # 최종 point 값을 answer에 추가

    return answer