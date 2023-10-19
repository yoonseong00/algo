def solution(spell, dic):

    count = []
    
    for i in dic:
        for j in spell:
            if j in i:
                count.append(i)
    if count in dic:
        return 1
    else:
        return 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))