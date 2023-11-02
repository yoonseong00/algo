def solution(dartResult):
    answer = []

    dart = ''

    for i in dartResult:
        if i.isdigit():
            dart += i
        elif i == 'S':
            dart = int(dart) ** 1
            answer.append(dart)
            dart = ''
        elif i == 'D':
            dart = int(dart) ** 2
            answer.append(dart)
            dart = ''
        elif i == 'T':
            dart = int(dart) ** 3
            answer.append(dart)
            dart = ''
        elif i == '*':
            if len(answer) > 1:
                answer[-1] *=2
                answer[-2] *=2 
            else:
                answer[-1] *=2
        elif i == '#':
            answer[-1] *= -1


    return sum(answer)