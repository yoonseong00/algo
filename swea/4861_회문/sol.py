import sys
sys.stdin = open('input.txt')

T = int(input())

# 회문인지 판별하는 함수
def find():

    result = []
    # 가로 찾기
    for i in range(N):
        for j in range(N-M+1):
            if matrix[i][j:j+M] == matrix[i][j : j+M][: : -1]: # 회문이 맞는지 확인
                result.append(matrix[i][j : j+M])   # 회문이라면 result에 append
                return result
    # 세로 찾기
    for i in range(N-M+1):
        for j in range(N):
            col_list = []   #세로열에 대한 데이터를 받을 리스트
            for k in range(M):  # 세로열 만들기
                col_list.append(matrix[i+k][j])
            if col_list == col_list[ : : -1]:   # 회문이 맞는지 확인
                result.append(''.join(col_list))    # 맞다면 col_list를 result에 append
                return result
            

for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # N= NxN 크기의 글자판 , M = 길이가 M인 회문 찾기

    matrix = [input() for _ in range(N)]    

    answer = find()

    ans = ''.join(answer)   # 리스트로 받은 문자를 문자열로 변환


    print(f'#{tc} {ans}')