# def solution(word):
#     words = list(word)
#     answer = []                                   #range 범위를 조정해서 구하는 방법
#     for i in range(len(words) - 1, -1, -1):
#         answer.append(words[i])
    ##############################################################################
#     return answer

    # answer = []           #reverse를 사용해 뒤집기
    # my_string.reverse()
    # answer = my_string
    #########################################################################
# def solution(num_list):
#     answer = []

#     for i in range(len(num_list)):
#         # num_list[i]
#         answer.append(num_list[len(num_list)-i-1])

#     return answer
##################################################################################
def solution(num_list):
    answer = []                           #insert 함수를 이용한 배열 뒤집기

    for num in num_list:
        answer.insert(0, num)

    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))