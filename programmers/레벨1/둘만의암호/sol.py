# def solution(s, skip, index):

#     answer = ''

#     for char in s:
#         a = ord(char)   # a = char의 유니코드
#         b = index

#         while b > 0:
#             a += 1
#             if a > ord('z'):    # a+1이 z를 넘어가면 a로 반환
#                 a = ord('a')
            
#             if chr(a) in skip:  # a+1이 된 상태의 a가 skip 안에 있으면 index에 +1
#                 b += 1
#             b -= 1
        
#         answer += chr(a)

#     return answer



def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for i in list(skip):
        alpha = alpha.replace(i,"")
    for i in s:
        answer += alpha[(alpha.find(i) + index) % len(alpha)]
    return answer

print(solution("aukks","wbqd",5))