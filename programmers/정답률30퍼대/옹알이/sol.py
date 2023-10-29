# def solution(babbling):
#     answer = 0
    
#     for char in babbling:
#         count = 0
#         word = ''
#         for i in char:
#             word += i   # 스펠링 하나하나씩 word에 넣어서 만약에 단어가 완성된다면
#             if word in ["aya", "ye", "woo", "ma"]:
#                 word = ''   # word를 초기화 시키고
#                 count += 1  # 말할 수 있는 단어하나를 완성 시킨거니 count
        
#         if len(word) == 0 and count > 0:    # 모든 for문을 다 돌고 카운트값이 올라갔으면 단어 하나를 말한 것이니 answer에 +1
#             answer += 1
    
#     return answer

# print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))



def solution(babbling):
    # 1
    mlist1 = ["aya", "ye", "woo", "ma"]

    # 2
    mlist2 = []
    for i in mlist1:
        for j in mlist1:
            if i != j:
                mlist2.append(i+j)
                for k in mlist1:
                    if j != k:
                        mlist2.append(i+j+k)
                        for l in mlist1:
                            if k != l:
                                mlist2.append(i+j+k+l)
    print(mlist2)

                                
    # answer = 0
    # for i in babbling:
    #     if i in mlist1 or i in mlist2:
    #         answer += 1
    # return answer

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))