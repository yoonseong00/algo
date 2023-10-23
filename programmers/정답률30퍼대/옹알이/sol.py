def solution(babbling):
    answer = 0
    
    for char in babbling:
        count = 0
        word = ''
        for i in char:
            word += i   # 스펠링 하나하나씩 word에 넣어서 만약에 단어가 완성된다면
            if word in ["aya", "ye", "woo", "ma"]:
                word = ''   # word를 초기화 시키고
                count += 1  # 말할 수 있는 단어하나를 완성 시킨거니 count
        
        if len(word) == 0 and count > 0:    # 모든 for문을 다 돌고 카운트값이 올라갔으면 단어 하나를 말한 것이니 answer에 +1
            answer += 1
    
    return answer

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))