# def solution(players, callings):
#     for calling in callings:
#         index = players.index(calling)
#         players.remove(calling)
#         players = players[:index-1] + [calling] + players[index-1:]

#     return players



# def solution(players, callings):
#     new_players = players[:] 

#     for calling in callings:
#         index = new_players.index(calling)
#         new_players = new_players[:index-1] + [calling] + new_players[index-1:index] + new_players[index+1:]

#     return new_players



# def solution(players, callings):
#     for calling in callings:
#         index = players.index(calling)
#         players.insert(index - 1, players.pop(index))

#     return players



def solution(players, callings):
    player_dict = {}

    for index, player in enumerate(players):
        player_dict[player] = index

    for calling in callings:
        # 불린 선수의 현재 등수
        index = player_dict[calling]
        # 앞 선수와 불린 선수의 인덱스 변경
        player_dict[calling] -= 1   
        player_dict[players[index - 1]] += 1
        # 위치 변경
        players[index-1], players[index] = players[index], players[index-1]

    return players


print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]	))