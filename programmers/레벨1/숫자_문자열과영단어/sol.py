def solution(s):
    
    kakao_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

    
    for key in kakao_dic:
        s = s.replace(key, kakao_dic[key])
    return int(s)

print(solution("one4seveneight"))