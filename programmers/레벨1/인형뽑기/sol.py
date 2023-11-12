def solution(board, moves):
    answer = 0
    kakao = []

    for move in moves:
        for index, num in enumerate(board):
            if num[move-1] != 0:
                # 뽑기통 안에 인형이 이미 있는 상태에서 만약 맨 위에 값이랑 현재 뽑은 값이 같으면
                if kakao and num[move-1] == kakao[-1]:
                    answer += 2 # 애니팡
                    kakao.pop() # 맨 위에 있는 값 삭제
                # 뽑기통 안에 아무것도 없거나 중복이 아닌 경우
                else:    
                    kakao.append(num[move-1])

                board[index][move-1] = 0
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))