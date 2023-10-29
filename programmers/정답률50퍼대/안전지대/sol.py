# 0,0에 지뢰가 있다고 가정을 해보면
# (-1,1)(0,1)(1,-1)(-1,0)(1,0)(-1,-1)(0,-1)(1, -1)
def solution(board):

    land_mine = len(board)

    # 0,0을 기준으로 지뢰가 있는 위치
    mine_x = [-1,-1,0,1,1,1,0,-1]   # 순서는 왼쪽부터 시계방향으로 진행
    mine_y = [0,1,1,1,0,-1,-1,-1]

    land_list = [] # 현재 지뢰가 있는 위치

    # 지뢰가 있는 위치 찾기
    for row in range(land_mine):
        for col in range(land_mine):
            if board[row][col] == 1:
                land_list.append((row,col))

    # 지뢰 주변에 1 표시
    for row, col in land_list:
        for i in range(8):  #지뢰가 설치된 위치 기준 주변 8칸은 위험지대이므로 8번 바리게이트? 치기
            bomb_x = row + mine_x[i]  # x축에 대한 바리게이트
            bomb_y = col + mine_y[i] # y축에 대한 바리게이트 ㅇㅋㅇㅋ
            # 만약에? 바리게이트의 범위가 기존 리스트보다 넘으면... 안되니까 범위 설정
            if 0 <= bomb_x < land_mine and 0 <= bomb_y < land_mine:
                board[bomb_x][bomb_y] = 1


    answer = 0
    # 리스트 전체에서 0인 케이스를 카운트
    for k in board:
        answer += k.count(0)


    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))