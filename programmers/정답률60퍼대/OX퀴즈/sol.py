def solution(quiz): #어차피 + - 밖에 없으니 굳이 함수로는 안해도 될 듯
    answer = []

    for i in quiz:
        x, y = i.split('=')
        x = x.split()
        print(x)
        if x[1] == '+': # 더하기 연산
            if int(x[0]) + int(x[2]) == int(y):
                answer.append('O')
            else:
                answer.append('X')
        elif x[1] == '-': # 빼기 연산
            if int(x[0]) - int(x[2]) == int(y):
                answer.append('O')
            else:
                answer.append('X')
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))