def solution(babbling):
    answer = 0
    
    for char in babbling:
        for i in ["aya", "ye", "woo", "ma"]:
            if i*2 not in char:
                char=char.replace(i, ' ')
        
        if len(char.strip()) == 0:
            answer += 1
    
    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))