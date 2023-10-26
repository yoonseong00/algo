def solution(s):

    answer = []
    
    count = {}

    for idx, spell in enumerate(s): # 인덱스 번호와 글자 뽑아오기
        if spell in count:  # 글자가 만약에 카운트에 있다면 현재 인덱스 번호 - 같은 단어가 있는 단어의 인덱스
            print(count[spell])
            answer.append(idx - count[spell])
        else:
            answer.append(-1)   # 본인이 처음이라면 -1 부여
        count[spell] = idx  # answer에 숫자를 넣었다면 count에 현재 인덱스 번호 넣기

    # print(answer)
    # print(count)
    
    return answer

    


print(solution("banana"))