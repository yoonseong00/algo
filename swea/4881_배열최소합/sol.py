import sys
sys.stdin = open('input.txt')

T = int(input())

def matrix_sum(row, sum): # row = 행 sum = 합
    global min_num

    # 모든 반복이 끝나고 나면 결과값을 리턴
    if row==N:
        if sum < min_num:
            min_num = sum

    for col in range(N):  
        if check_list[col]==0:    # 열 idx가 다를때만 진행
            check_list[col] = 1   #지나간 곳이라는 표시
            matrix_sum(row+1, sum+matrix[row][col])   # 합이 진행 됐으면 다음 행으로 넘어가고 기존합에서[n][j]의 값을 더한 값을 리턴
            check_list[col] = 0   #다시 뒤로 돌아가기 위해 체크리스트 해제


for tc in range(1, T+1):

    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    check_list = [0] * N    # 방문했던 곳을 체크하기 위한 체크리스트

    min_num = 10 * N    #나올 수 있는 경우의 수 중 최대값

    matrix_sum(0, 0)    # 0번째 행부터 시작, 현재까지 합한 값(아직 합을 시작안했으니 0)

    print(min_num)
