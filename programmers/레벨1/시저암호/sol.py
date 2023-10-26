def solution(s, n):
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    answer = []

    for i in s:
        if i == ' ':    # 공백은 밀어도 공백이니 answer 그대로 추가
            answer.append(' ')
        # 대문자 판별
        elif i.isupper() == True:
            plus = up.find(i) + n   # i의 인덱스 번호를 찾고 그 인덱스 번호에 n만큼 추가
            answer.append(up[plus % len(up)])
        # 앞에 있는 상황에 다 안걸리면 소문자
        else:
            plus = up.find(i) + n
            answer.append(low[plus % len(up)])

    return ''.join(answer)

print(solution('AB', 1))