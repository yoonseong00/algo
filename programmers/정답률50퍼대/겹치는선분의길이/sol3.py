# 교집합의 합집합으로 구하기
def solution(lines):
    answer = [set(range(min(l), max(l))) for l in lines]

    print(answer[0])

    result = len(answer[0] & answer[1] | answer[0] & answer[2] | answer[1] & answer[2])

    return result

print(solution([[0, 1], [2, 5], [3, 9]]))