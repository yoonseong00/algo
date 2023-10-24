def solution(absolutes, signs):

    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += int(absolutes[i])
        elif signs[i] == False:
            answer -= int(absolutes[i])

    return answer

print(solution([4,7,12], [True,False,True]))