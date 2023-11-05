def solution(keymap, targets):
    btn_count = {}
    
    # 버튼생성
    for keys in keymap:
        for index, key in enumerate(keys):
            if key not in btn_count:
                btn_count[key] = index +1
            else:
                btn_count[key] = min(btn_count[key], index+1)

    
    answer = []
    for target in targets:
        count = 0
        for t in target:
            if t not in btn_count:
                count = -1
                break
            else:
                count += btn_count[t]
        
        answer.append(count)

    return answer


print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))