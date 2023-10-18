import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # N = 2차원 배열의 크기 N^2 , M = M^2의 범위만큼 합을 구해야 함.

    matrix = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열이라 N만큼의 범위 설정을 안해주면 'too many values to unpack' 이라는 에러가 나온다.

    Num_list = []

    for i in range(N-M+1):      #구간합에서 했던 for문 그대로 인용 = 전체크기에서 구간만큼 빼주기
        for j in range(N-M+1):  
            max_num = 0
            for row in range(M):    # M 만큼 행과열로 범위 나누기
                for col in range(M):
                    max_num += matrix[i+row][j+col] # i+M만큼씩의 값들의 합을 max_num에 저장
            Num_list.append(max_num)
        
    print(f'#{tc} {max(Num_list)}')






