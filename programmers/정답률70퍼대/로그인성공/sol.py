def solution(id_pw, db):

    for i in db:
       if id_pw[0] == i[0]:
        if id_pw[1] == i[1]:
            return "login"
        return "wrong pw"
    return "fail"

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]	))
print(solution(["programmer01", "15789"],[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"],[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))